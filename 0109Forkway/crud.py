from sqlalchemy.orm import Session
import models, schemas

# CRUD for Worker
# ... (same as provided above)

# CRUD for Customer
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name, phone_number=customer.phone_number, trade_point_id=customer.trade_point_id)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# ... similar CRUD operations for Update and Delete

# CRUD for TradePoint
# ... similar CRUD operations for Create, Read, Update and Delete

# CRUD for Order
# ... similar CRUD operations for Create, Read, Update and Delete

# CRUD for Visit
# ... similar CRUD operations for Create, Read, Update and Delete
