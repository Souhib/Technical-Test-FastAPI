# Frame Technical Test for OpenInnovation

This project is a technical test solution for OpenInnovation, implementing an image processing and retrieval system with a FastAPI backend.

## Project Overview

The system processes image data from a CSV file, resizes the images, stores them in a database, and provides an API to retrieve and apply custom colormaps to the images based on depth ranges.

### Key Features

- Image resizing from 200 to 150 pixels width
- Database storage of processed images
- FastAPI-based API for image retrieval
- Dynamic colormap application to retrieved frames
- Depth-based frame querying

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment:
   - Create a `.env` file in the project root
   - Add the following line to the `.env` file:
     ```bash
     DATABASE_URL=sqlite:///database.db
     ```

4. Load the image data:
   ```bash
   python load_picture.py
   ```

## Running the Application

Start the FastAPI server:

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

You can also use uvicorn directly:

```bash
uvicorn main:app --reload
```

## API Usage

### Get Frames

Endpoint: `GET /frames/`

Query Parameters:
- `depth_min`: Minimum depth (float)
- `depth_max`: Maximum depth (float)
- `colormap`: Colormap to apply (string, options: viridis, plasma, inferno, magma, cividis)

Example:
```
GET /frames/?depth_min=9000&depth_max=9500&colormap=viridis
```

Response:
```json
[
  {
    "depth": 9000.5,
    "frame": [[r, g, b], [r, g, b], ...]
  },
  {
    "depth": 9001.2,
    "frame": [[r, g, b], [r, g, b], ...]
  },
  ...
]
```

## Docker Support

A Dockerfile is provided for containerization. To build and run the Docker image:

```bash
docker build -t frame-technical-test .
docker run -p 8000:8000 frame-technical-test
```

## Project Structure

- `main.py`: Application entry point
- `load_picture.py`: Script to process and load image data into the database
- `api/`: Contains the FastAPI application code
  - `controllers/`: Business logic
  - `models/`: Data models and schemas
  - `routes/`: API route definitions
- `Dockerfile`: Docker configuration for containerization

## Technologies Used

- Python 3.11
- FastAPI
- SQLModel
- SQLite
- Matplotlib (for colormap application)
- Docker

## Development

### Running Tests

To run the tests for this project, use the following command:

```bash
pytest
```

### Code Linting

We use ruff and black for code linting. Run the linter with:

```bash
ruff check .
black .
isort .
```

### Type Checking

For type checking, we use mypy. Run the type checker with:

```bash
mypy .
```

## API Documentation

When the application is running, you can access the auto-generated API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
