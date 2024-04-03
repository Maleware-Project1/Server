from fastapi import FastAPI, Depends
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

# Create a new symmetric key
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

# Retrieve a symmetric key by id
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
    return repository.get_symmetric_key(db=db, id=id)
