# Todo API

A REST API built with Python and FastAPI to manage todo tasks.

## Features
- Add a new task
- View all tasks
- Mark a task as complete
- Delete a task

## Tech Stack
- Python
- FastAPI
- Uvicorn

## How to Run Locally

1. Clone this repository
git clone https://github.com/YOUR_USERNAME/todo-api.git

2. Install dependencies
pip install fastapi uvicorn

3. Run the API
uvicorn main:app --reload

4. Open in browser
http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks/add | Add a new task |
| PUT | /tasks/complete/{id} | Mark task complete |
| DELETE | /tasks/delete/{id} | Delete a task |

## Author
Your Name — VIT Chennai, B.Tech CSE