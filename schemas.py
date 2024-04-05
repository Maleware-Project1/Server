from pydantic import BaseModel

class SymmetricKey(BaseModel):
    """
    Represents a symmetric key.

    Attributes:
        id (str): The ID of the symmetric key.
        mac_address (str): The MAC address associated with the symmetric key.
        key (str): The actual key value.
    """
    id: str
    mac_address: str
    key: str

class SymmetricKeyCreate(BaseModel):
    """
    Represents the creation of a symmetric key.

    Attributes:
        mac_address (str): The MAC address associated with the symmetric key.
    """
    mac_address: str