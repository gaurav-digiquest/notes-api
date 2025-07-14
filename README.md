# Notes API

A simple Django REST API to create, update, delete and view notes.

## Features
- Create a note
- View all notes
- Update a note
- Delete a note

## API Endpoints

| Method | URL                | Description     |
|--------|--------------------|-----------------|
| GET    | `/api/notes/`      | List all notes  |
| POST   | `/api/notes/`      | Create new note |
| GET    | `/api/notes/<id>/` | Get note detail |
| PUT    | `/api/notes/<id>/` | Update note     |
| DELETE | `/api/notes/<id>/` | Delete note     |

## Tech Stack
- Python
- Django
- Django REST Framework
- MySQL

## Run Locally

```bash
git clone https://github.com/gaurav-digiquest/notes-api.git
cd notes-api
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py runserver 
