readme_content = """
# FastAPI CRUD API with MongoDB

This project is a FastAPI-based CRUD (Create, Read, Update, Delete) API for managing Items and User Clock-In Records, using MongoDB as the database. The project includes routes for creating, reading, updating, and deleting both Items and Clock-In Records.

## Features
- **Items API**: Allows for adding, updating, deleting, and fetching items.
- **Clock-In Records API**: Allows for clocking in (location-based), updating, deleting, and fetching clock-in records.
- Uses MongoDB for data storage.
- Asynchronous API operations powered by FastAPI and `motor` (MongoDB async driver).

## Prerequisites

- Python 3.8+
- MongoDB database (local or cloud-based)
- FastAPI and Uvicorn for running the API

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Allan2706/Assignment-Vodex.git
cd Assignment-Vodex

