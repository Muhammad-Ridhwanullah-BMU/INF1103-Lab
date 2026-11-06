import re
class Supplier():

    EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    def __init__(self,supplier_id:str, name:str, contact_email:str):
        
        if not isinstance(supplier_id, str) or not supplier_id.strip():
            raise ValueError("Supplier ID cannot be empty.")
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Supplier name cannot be empty.")
        
        if not isinstance(contact_email, str) or not contact_email.strip():
            raise ValueError("Supplier email cannot be empty.")
        
        if not re.match(self.EMAIL_PATTERN, contact_email):
            raise ValueError(f"'{contact_email}' is not a valid email format.")
        
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def supplier_information(self):
        print(
            f"Supplier ID: {self.__supplier_id} | "
            f"Supplier Name: {self.__name} | "
            f"Contact Email: {self.__contact_email}"
        )