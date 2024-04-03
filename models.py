from sqlalchemy import Column, String
import database 

class SymmetricKey(database.Base):
    """
    Represents a symmetric key used for encryption and decryption.

    Attributes:
        id (str): The unique identifier of the symmetric key.
        mac_address (str): The MAC address associated with the symmetric key.
        key (str): The actual symmetric key value.
    """
    __tablename__ = "symmetric_keys"

    id = Column(String, primary_key=True)  # Unique identifier for the symmetric key
    mac_address = Column(String)  # MAC address associated with the symmetric key
    key = Column(String)  # Actual symmetric key value

