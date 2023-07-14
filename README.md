# ECOMMERSE_API

# E-Commerce API

This is an API for an E-Commerce application that allows users to browse products, add items to their cart, and place orders. It provides various endpoints to interact with the E-Commerce system.

## Features

- User registration and authentication
- Product listing and details
- Shopping cart functionality
- Order placement and tracking

## Technologies Used

- Python
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python
- SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library
- SQLite: Lightweight, serverless database engine
- JWT: JSON Web Token for user authentication and authorization

## Getting Started

### Prerequisites

- Python 3.7+
- Pip (Python package installer)

### Installation

1. Clone the repository:

git clone https://github.com/your-username/e-commerce-api.git

css


2. Navigate to the project directory:

cd e-commerce-api

arduino


3. Create a virtual environment:

python -m venv venv

markdown


4. Activate the virtual environment:

- Windows:

venv\Scripts\activate

diff


- Linux/Mac:

source venv/bin/activate

markdown


5. Install the dependencies:

pip install -r requirements.txt

markdown


### Configuration

1. Create a `.env` file in the root directory of the project.

2. Add the following environment variables to the `.env` file:

DATABASE_URL="sqlite:///database.db"
SECRET_KEY="your-secret-key"

markdown


3. Modify the values as per your requirements.

### Database Migration

1. Run the database migrations to create the required tables:

alembic upgrade head

markdown


### Starting the API

1. Start the API server:

uvicorn main:app --reload

csharp


2. The API will be accessible at `http://localhost:8000`.

## API Documentation

The API documentation is available at `http://localhost:8000/docs`.

## Usage

1. Register a new user by sending a POST request to `/register` endpoint with the required information (email, username, password).

2. Log in with the registered user by sending a POST request to `/login` endpoint with the email and password.

3. Explore the available endpoints to interact with the E-Commerce system, such as retrieving product details, adding items to the cart, and placing orders.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
