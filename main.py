from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, EmailStr
from database import get_connection, init_db
import mysql.connector


app = FastAPI(title="Contact Form App")


@app.on_event("startup")
def startup():
    init_db()


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.post("/contacts")
def create_contact(contact: ContactForm):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (contact.name, contact.email, contact.message),
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return {"id": new_id, **contact.model_dump()}


@app.get("/contacts")
def list_contacts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contacts ORDER BY created_at DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows