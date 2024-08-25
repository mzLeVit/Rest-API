from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from typing import Optional
from datetime import datetime, timedelta
from models import Contact  # власна модель
from database import get_db  # власна функція отримання сесії бд

app = FastAPI()

@app.get("/contacts/search")
async def search_contacts(
    name: Optional[str] = Query(None),
    surname: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = select(Contact)

    if name:
        query = query.filter(Contact.name.ilike(f"%{name}%"))
    if surname:
        query = query.filter(Contact.surname.ilike(f"%{surname}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))

    result = await db.execute(query)
    contacts = result.scalars().all()
    return contacts

@app.get("/contacts/birthdays/next-7-days")
async def get_upcoming_birthdays(db: Session = Depends(get_db)):
    today = datetime.now()
    next_week = today + timedelta(days=7)

    query = select(Contact).filter(
        Contact.birthday.between(today, next_week)
    )

    result = await db.execute(query)
    contacts = result.scalars().all()
    return contacts
