# To-Do List API using FastAPI

## Project Overview

This project is a simple REST API built using **FastAPI** that allows users to create and manage to-do lists.

The application demonstrates the basics of FastAPI, REST API development, object-oriented programming (OOP), and the **SOLID design principles** (Single Responsibility Principle and Open/Closed Principle).

The project stores data in memory using Python data structures, so no database is required.

---

## Features

* Create a new to-do list
* View all to-do lists
* Update a to-do list
* Delete a to-do list
* Search for a to-do list by keyword

---

## Technologies Used

* Python 3
* FastAPI
* Pydantic
* Uvicorn

---

## Project Structure

```
todo_project/
│
├── main.py          # FastAPI routes
├── models.py        # Pydantic models and business logic
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint                  | Description                |
| ------ | ------------------------- | -------------------------- |
| GET    | `/lists`                  | Retrieve all to-do lists   |
| POST   | `/lists`                  | Create a new to-do list    |
| PUT    | `/lists/{list_id}`        | Update a to-do list        |
| DELETE | `/lists/{list_id}`        | Delete a to-do list        |
| GET    | `/lists/search/{keyword}` | Search to-do lists by name |

---

## How to Run the Project

### 1. Clone the repository

```
git clone <repository-url>
```

### 2. Navigate to the project folder

```
cd todo_project
```

### 3. Install the dependencies

```
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```
uvicorn main:app --reload
```

If port **8000** is already in use:

```
uvicorn main:app --reload --port 8001
```

---

## Swagger API Documentation

After starting the server, open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

or

```
http://127.0.0.1:8001/docs
```

Swagger UI provides interactive API documentation where all endpoints can be tested directly.

---

## SOLID Principles Used

### Single Responsibility Principle (SRP)

* `main.py` is responsible for handling HTTP requests and responses.
* `models.py` contains the Pydantic models and the application's business logic.
* Each class has a single, well-defined responsibility.

### Open/Closed Principle (OCP)

The project uses inheritance to extend functionality.

* `BaseTodoService` provides the core CRUD operations.
* `TodoService` extends `BaseTodoService` by adding the search functionality.

This allows new features to be added without modifying the existing base class, making the code open for extension but closed for modification.

---

## Future Enhancements

* Add support for to-do items within each list.
* Integrate a SQL database such as SQLite or PostgreSQL.
* Add user authentication and authorization.
* Implement persistent data storage.
* Add automated unit tests using Pytest.
* Containerize the application using Docker.

---

## Learning Outcomes

This project demonstrates:

* FastAPI fundamentals
* REST API development
* Pydantic data validation
* Object-Oriented Programming (OOP)
* Service layer design
* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* CRUD operations
* API testing with Swagger UI
