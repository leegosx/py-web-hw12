from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from src.database.models import Contact, User
from src.schemas import ContactModel
from datetime import timedelta, datetime

async def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, user: User, db: Session) -> Contact:
    return db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()


async def create_contact(body: ContactModel, user: User, db: Session):
    contact = Contact(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        phone=body.phone,
        birthday=body.birthday,
        user_id=user.id
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(contact_id: int, body: ContactModel, user: User, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.first_name=body.first_name,
        contact.last_name=body.last_name,
        contact.email=body.email,
        contact.phone=body.phone,
        contact.birthday=body.birthday
        contact.user_id=user.id
        db.commit()
    return contact

async def remove_contact(contact_id: int, user: User, db: Session)  -> Contact | None:
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

async def search_contacts(query: str, user: User, db: Session):
    contacts = (
        db.query(Contact)
        .filter(
            or_(
                Contact.first_name.contains(query),
                Contact.last_name.contains(query),
                Contact.email.contains(query)
            ),
            Contact.user_id == user.id
        )
        .all()
    )
    return contacts

async def get_upcoming_birthdays(days: int, user: User, db: Session):
    request = []
    all_contacts = db.query(Contact).filter(Contact.user_id == user.id).all()
    for contact in all_contacts:
        if timedelta(0) <= ((contact.birthday.replace(year=int((datetime.now()).year))) - datetime.now().date()) <= timedelta(days):
            request.append(contact)

    return request