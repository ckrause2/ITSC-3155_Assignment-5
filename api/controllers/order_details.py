from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_detail):
    # Create a new instance of the Order_Detail model with the provided data
    db_order_detail = models.Order_Detail(
        customer_name=order_detail.customer_name,
        description=order_detail.description
    )
    # Add the newly created Order_Detail object to the database session
    db.add(db_order_detail)
    # Commit the changes to the database
    db.commit()
    # Refresh the Order_Detail object to ensure it reflects the current state in the database
    db.refresh(db_order_detail)
    # Return the newly created Order_Detail object
    return db_order_detail


def read_all(db: Session):
    return db.query(models.Order_Detail).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.Order_Detail).filter(models.Order_Detail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    # Query the database for the specific order_detail to update
    db_order_detail = db.query(models.Order_Detail).filter(models.Order_Detail.id == order_detail_id)
    # Extract the update data from the provided 'order_detail' object
    update_data = order_detail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order_detail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order_detail record
    return db_order_detail.first()


def delete(db: Session, order_detail_id):
    # Query the database for the specific order_detail to delete
    db_order_detail = db.query(models.Order_Detail).filter(models.Order_Detail.id == order_detail_id)
    # Delete the database record without synchronizing the session
    db_order_detail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
