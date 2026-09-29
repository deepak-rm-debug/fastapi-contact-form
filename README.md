# Contact Form App

FastAPI + MySQL contact form API.

## Prerequisites

- Python 3.10+
- MySQL server running locally

The database (`contact_db`) and `contacts` table are created automatically on startup.

## Setup

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Configure

Set your MySQL password in the terminal before running.

Windows (PowerShell):
```
$env:DB_PASSWORD = "your_mysql_password"
```

Mac/Linux:
```
export DB_PASSWORD="your_mysql_password"
```

Defaults: host `localhost`, user `root`, database `contact_db`.

## Run

```
uvicorn main:app --reload
```

Docs: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path       | Description       |
|--------|------------|-------------------|
| POST   | /contacts  | Create a contact  |
| GET    | /contacts  | List all contacts |

## Sample request

```json
{
  "name": "Deepak",
  "email": "deepak@gmail.com",
  "message": "Hello, this is a test message."
}
```