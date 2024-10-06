# Frame Technical Test for OpenInnovation 😊

This project is a technical test solution for OpenInnovation, implementing an image processing and retrieval system with a FastAPI backend 🚀.

## Project Overview

The system processes image data from a CSV file, resizes the images, stores them in a database, and provides an API to retrieve and apply custom colormaps to the images based on depth ranges 🌊.

### Key Features

- Image resizing from 200 to 150 pixels width 🔄
- Database storage of processed images 💻
- FastAPI-based API for image retrieval 🚀
- Dynamic colormap application to retrieved frames 🎨
- Depth-based frame querying 🔍

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

## Running the Application 👟

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
depth_min: 9100.3
depth_max: 9200.5
colormap: viridis
GET /frames/?depth_min=9100.3&depth_max=9200.5&colormap=viridis
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

A Dockerfile and a docker-compose.yml file are provided for containerization. To build and run the Docker image using Docker Compose:

```bash
docker-compose up
```

This command will build the Docker image and start the container based on the configuration in the docker-compose.yml file. The service is named `app` and it maps port 8000 on the host machine to port 8000 in the container. It also uses the environment variables from the `.env` file.

To access the API running in the container, open a web browser and go to `http://localhost:8000/docs`.

## Project Structure

- `main.py`: Application entry point
- `load_picture.py`: Script to process and load image data into the database
- `api/`: Contains the FastAPI application code
  - `controllers/`: Business logic
  - `models/`: Data models and schemas
  - `routes/`: API route definitions
- `Dockerfile`: Docker configuration for containerization
- `docker-compose.yml`: Docker Compose configuration for containerization

## Technologies Used

- Python 3.11 🐍
- FastAPI 🚀
- SQLModel 💻
- SQLite 🚀
- Matplotlib (for colormap application) 🎨
- Docker 🚀

## Development

### Running Tests ⚗️

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

### Type Checking ✅

For type checking, we use mypy. Run the type checker with:

```bash
mypy .
```

## API Documentation 📄

When the application is running, you can access the auto-generated API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


## Deploy

This API is deployed on a personal Ubuntu Linux server. The Docker image built from the provided Dockerfile was pushed to Docker Hub and then run on the server. You can access the API documentation directly at: http://90.0.202.78:8001/docs


## Image Loading and Manipulation

I must admit that I didn't fully understand the part of loading the image from a CSV file and handling the manipulation of the image due to its CSV format. However, I tried my best to implement this feature and learn from the experience. Despite the challenges, I focused on showcasing my Python skills and following the best practices of Python, FastAPI, linting, and testing. Given the time constraints, I prioritized demonstrating my abilities and adhering to industry standards, and I hope this effort is reflected in the code.

If you'd like to see more of my work and what I can do, please check out my GitHub account: [Souhib](https://github.com/Souhib).

Additionally, you can explore this project specifically: [IBG_API](https://github.com/Souhib/IBG_API)