import uuid
import models, schemas

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
    db_symmetric_key = models.SymmetricKey(id=str(uuid.uuid1()), mac_address=symmetric_key.mac_address, key=symmetric_key.key)
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
