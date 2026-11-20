import ast
import contextlib
import inspect
import io
import os
from pathlib import Path
import tempfile
import textwrap
import unittest
from unittest.mock import patch

from App import get_positive_float
from BulkDiscount import BulkDiscount
from CHASDiscount import CHASDiscount
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from NoDiscount import NoDiscount
from Order import Order
from OrderLine import OrderLine
from PercentageDiscount import PercentageDiscount
from PhysicalProduct import PhysicalProduct
from Product import Product
from ProductFactory import ProductFactory
from ProductLoader import load_products
from Supplier import Supplier


class Lab9Section7Tests(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier('S001', 'Example Supplier', 'supplier@example.com')
        self.product = ProductFactory.create('physical', 'P001', 'Desk Lamp',
                                             250.0, 10, self.supplier, weight=1.0)

    def make_order(self, discount):
        order = Order('O001', discount)
        order.add_order_line(self.product, 1)
        return order

    def test_01_bulk_discount_total(self):
        self.assertAlmostEqual(self.make_order(BulkDiscount(200, 20)).calculate_total(), 230)

    def test_02_change_strategy(self):
        order = self.make_order(BulkDiscount(200, 20))
        self.assertAlmostEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_03_no_discount_argument_defaults(self):
        order = Order('O_DEFAULT')
        order.add_order_line(self.product, 1)
        self.assertIsInstance(order.discount, NoDiscount)
        self.assertEqual(order.calculate_total(), 250)

    def test_04_new_chas_strategy(self):
        for colour, expected in [('green', 225), ('orange', 212.5), ('blue', 200)]:
            with self.subTest(colour=colour):
                self.assertAlmostEqual(self.make_order(CHASDiscount(colour)).calculate_total(), expected)

    def test_05_no_discount_branches_in_order_calculate_total(self):
        tree = ast.parse(textwrap.dedent(inspect.getsource(Order.calculate_total)))
        self.assertFalse(any(isinstance(n, (ast.If, ast.IfExp)) for n in ast.walk(tree)))

    def test_06_factory_creates_products(self):
        p = ProductFactory.create('physical', 'P101', 'Lamp', 25, 3, self.supplier, weight=0.5)
        d = ProductFactory.create('digital', 'D101', 'Book', 10, 3, self.supplier, download_size=5)
        self.assertIsInstance(p, Product)
        self.assertIsInstance(p, PhysicalProduct)
        self.assertIsInstance(d, Product)
        self.assertIsInstance(d, DigitalProduct)

    def test_07_factory_unknown_type_error(self):
        with self.assertRaisesRegex(ValueError, 'Unknown product type: service'):
            ProductFactory.create('service', 'S001', 'Installation', 30, 5, self.supplier)

    def test_08_app_and_filehandler_use_factory_not_concrete_constructors(self):
        for filename in ('App.py', 'FileHandler.py'):
            with self.subTest(filename=filename):
                tree = ast.parse(Path(__file__).with_name(filename).read_text(encoding='utf-8'))
                calls = [n for n in ast.walk(tree)
                         if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                         and n.func.id in {'PhysicalProduct', 'DigitalProduct'}]
                self.assertEqual(calls, [])

    def test_09_price_zero_and_negative_rejected(self):
        for price in (0, -1):
            with self.subTest(price=price), self.assertRaises(ValueError):
                ProductFactory.create('physical', 'P200', 'Lamp', price, 1, self.supplier, weight=1)

    def test_10_negative_stock_rejected(self):
        with self.assertRaises(ValueError):
            ProductFactory.create('digital', 'D200', 'Book', 2, -1, self.supplier, download_size=1)

    def test_11_nonpositive_order_quantity_rejected(self):
        for quantity in (0, -2):
            with self.subTest(quantity=quantity), self.assertRaises(ValueError):
                OrderLine(self.product, quantity)

    def test_12_bad_input_reprompted(self):
        output = io.StringIO()
        with patch('builtins.input', side_effect=['abc', '-5', '12.50']):
            with contextlib.redirect_stdout(output):
                value = get_positive_float('Price: ')
        self.assertEqual(value, 12.5)
        self.assertIn('Please enter a valid number', output.getvalue())
        self.assertIn('Please enter a number greater than zero', output.getvalue())

    def test_13_nan_input_rejected_and_reprompted(self):
        output = io.StringIO()
        with patch('builtins.input', side_effect=['nan', '12.50']):
            with contextlib.redirect_stdout(output):
                value = get_positive_float('Price: ')
        self.assertEqual(value, 12.5)

    def test_14_missing_products_csv_handled(self):
        inventory = Inventory()
        with tempfile.TemporaryDirectory() as tmp:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                load_products(os.path.join(tmp, 'missing.csv'), inventory, self.supplier)
        self.assertEqual(len(inventory.products), 0)
        self.assertIn('Products file not found:', output.getvalue())
        self.assertTrue(output.getvalue().rstrip().endswith('Load attempt finished.'))

    def test_15_bad_csv_rows_skipped_valid_rows_loaded(self):
        rows = ('product_type,product_id,name,price,stock_quantity\n'
                'physical,P001,Desk Lamp,25.00,10\n'
                'digital,D001,Photo Editor,49.90,100\n'
                'service,S001,Installation,30.00,5\n'
                'physical,P002,Office Chair,abc,3\n'
                'physical,P003,Monitor Stand,39.50,7\n')
        inventory = Inventory()
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, 'products.csv')
            Path(path).write_text(rows, encoding='utf-8')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                load_products(path, inventory, self.supplier)
        self.assertEqual(len(inventory.products), 3)
        self.assertIn('Skipped row 4:', output.getvalue())
        self.assertIn('Skipped row 5:', output.getvalue())
        self.assertIn('Loaded 3 product(s).', output.getvalue())
        self.assertTrue(output.getvalue().rstrip().endswith('Load attempt finished.'))

    def test_16_no_bare_or_catch_all_exception_handlers(self):
        for filename in ('App.py', 'FileHandler.py', 'ProductLoader.py'):
            with self.subTest(filename=filename):
                tree = ast.parse(Path(__file__).with_name(filename).read_text(encoding='utf-8'))
                for node in ast.walk(tree):
                    if isinstance(node, ast.ExceptHandler):
                        self.assertIsNotNone(node.type, f'Bare except in {filename}')
                        if isinstance(node.type, ast.Name):
                            self.assertNotIn(node.type.id, ('Exception', 'BaseException'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
