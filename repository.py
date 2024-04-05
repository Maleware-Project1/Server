import uuid
import models, schemas, utils

from sqlalchemy.orm import Session

def create_symmetric_key(db: Session, symmetric_key: schemas.SymmetricKeyCreate):
    """
    Create a new symmetric key in the database.

    Args:
        db (Session): The database session.
        symmetric_key (schemas.SymmetricKeyCreate): The symmetric key data.

    Returns:
        models.SymmetricKey: The created symmetric key.
    """
    fernet_key = utils.create_Fernet_key().decode("utf-8")
    db_symmetric_key = models.SymmetricKey(id=str(uuid.uuid1()), mac_address=symmetric_key.mac_address, key=fernet_key)
    db.add(db_symmetric_key)
    db.commit()
    db.refresh(db_symmetric_key)
    return db_symmetric_key

def get_symmetric_key(db: Session, id: str):
    """
    Retrieve a symmetric key from the database by its ID.

    Args:
        db (Session): The database session.
        id (str): The ID of the symmetric key to retrieve.

    Returns:
        models.SymmetricKey: The retrieved symmetric key.
    """
    symmetric_key = db.query(models.SymmetricKey).filter(models.SymmetricKey.id == id).first()
    return symmetric_key

def get_symmetric_keys_by_mac_address(db: Session, mac_address: str, limit: int = 100):
    """
    Retrieve symmetric keys from the database based on the given MAC address.

    Args:
        db (Session): The database session object.
        mac_address (str): The MAC address to filter the symmetric keys.
        limit (int, optional): The maximum number of symmetric keys to retrieve. Defaults to 100.

    Returns:
        List[models.SymmetricKey]: A list of symmetric keys matching the MAC address.
    """
    # Query the database to retrieve symmetric keys based on the MAC address and limit the results
    symmetric_keys = db.query(models.SymmetricKey).filter(models.SymmetricKey.mac_address == mac_address).limit(limit).all()
    return symmetric_keys

