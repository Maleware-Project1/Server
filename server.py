from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import repository, schemas

from database import SessionLocal, Base, engine

# Create the table in the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Dependency
def get_db() -> Session:
    """
    Returns a database session.

    Returns:
        Session: The database session object.
    """
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to the caller
    finally:
        db.close()  # Close the session when done

@app.post("/symmetric_keys/", response_model=schemas.SymmetricKey)
def create_symmetric_key(symmetric_key: schemas.SymmetricKeyCreate, db:  Session = Depends(get_db)):
    """
    Create a new symmetric key.

    Args:
        symmetric_key (schemas.SymmetricKeyCreate): The symmetric key data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        schemas.SymmetricKey: The created symmetric key.
    """
    return repository.create_symmetric_key(db=db, symmetric_key=symmetric_key)

@app.get("/symmetric_keys/{id}", response_model=schemas.SymmetricKey)
def get_symmetric_key(id: str, db:  Session = Depends(get_db)):
    """
    Retrieve a symmetric key by id.

    Args:
        id (str): The id of the symmetric key.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        schemas.SymmetricKey: The retrieved symmetric key.
    """
    db_symmetric_key = repository.get_symmetric_key(db=db, id=id)
    if db_symmetric_key is None:
        raise HTTPException(status_code=404, detail="symmetric key not found")

    return db_symmetric_key

@app.get("/symmetric_keys/list/{mac_address}", response_model=list[schemas.SymmetricKey])
def get_symmetric_keys_by_mac_address(mac_address: str, limit: int = 100, db:  Session = Depends(get_db)):
    """
    Retrieve symmetric keys by MAC address.

    Args:
        mac_address (str): The MAC address to filter the symmetric keys.
        limit (int, optional): The maximum number of symmetric keys to retrieve. Defaults to 100.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        list[schemas.SymmetricKey]: The retrieved symmetric keys.
    """
    db_symmetric_keys = repository.get_symmetric_keys_by_mac_address(db=db, mac_address=mac_address, limit=limit)
    if db_symmetric_keys is None:
        raise HTTPException(status_code=404, detail="no symmetric keys found for the given MAC address")

    return db_symmetric_keys