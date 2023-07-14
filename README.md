# E-Commerce API

This is an API for an E-Commerce application built using FastAPI. It provides endpoints to manage products, user registration and authentication, shopping cart functionality, and order placement.

## Features

- User registration and authentication
- Product listing, creation, and management
- Shopping cart functionality
- Order placement and tracking

## Technologies Used

- Python
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python
- SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library
- SQLite: Lightweight, serverless database engine
- Pydantic: Data validation and serialization library
- JWT: JSON Web Token for user authentication and authorization

## Getting Started

### Prerequisites

### Installation

1. Clone the repository:

git clone https://github.com/your-username/PROJECT_E_COMMERCE


2. Navigate to the project directory:

cd PROJECT_E_COMMERCE





API settings

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./app.db
JWT settings

ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
CORS settings

ALLOWED_ORIGINS=http://localhost:3000


2. Adjust other configuration files as necessary (e.g., database settings, CORS origins).

## API Documentation

The API documentation is available at `http://localhost:8000/docs`.

## Usage

1. Register a new user by sending a POST request to `/register` endpoint with the required information (email, username, password).

2. Log in with the registered user by sending a POST request to `/login` endpoint with the email and password.

3. Explore the available endpoints to interact with the E-Commerce system, such as retrieving product details, adding items to the cart, and placing orders.

## Development

1. Create a new branch for your feature or bug fix:

git checkout -b feature/my-new-feature


2. Make your changes and commit them:

3. git commit -am 'Add some feature'


3. Push your changes to the remote repository:


git push origin feature/my-new-feature


4. Submit a pull request for review.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
