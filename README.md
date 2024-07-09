# Ecommerce Search and Recommendation

E-commerce search and recommendation system. Supports CRUD operations for products, search with filters and sorting, and personalized recommendations. Built with Flask, PostgreSQL, JWT, and RabbitMQ. Ideal for e-commerce developers seeking a comprehensive and scalable solution.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contribution](#contribution)
4. [License](#license)
5. [Contact](#contact)
6. [Additional Resources](#additional-resources)

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- RabbitMQ
- Node.js (for frontend integration if needed)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-search-recommendation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ecommerce-search-recommendation
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the PostgreSQL database:
   ```bash
   createdb ecommerce_db
   ```
6. Run the database migrations (if using Flask-Migrate):
   ```bash
   flask db upgrade
   ```
7. Configure RabbitMQ:
   ```bash
   sudo service rabbitmq-server start
   ```

## Usage

To start the application, use the following command:

```bash
flask run
```

Example usage for searching products:

```bash
curl -X GET "http://127.0.0.1:5000/search?q=shoes"
```

Expected result:

```json
{
  "products": [
    {
      "id": 1,
      "name": "Running Shoes",
      "category": "Sports",
      "price": 59.99
    },
    ...
  ]
}
```

## Project Structure

```
ecommerce-search-recommendation-main/
├── Dockerfile
├── README.md
├── docker-compose.yml
├── main.py
├── requirements.txt
└── src
    ├── application
    │   ├── __init__.py
    │   ├── repositories
    │   │   ├── __init__.py
    │   │   └── product_repository.py
    │   └── use_cases
    │       ├── __init__.py
    │       └── product
    │           ├── __init__.py
    │           ├── create_product_use_case.py
    │           └── search_product_use_case.py
    ├── domain
    │   ├── __init__.py
    │   ├── entities
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── category.py
    │   │   └── product.py
    │   ├── routes
    │   │   ├── __init__.py
    │   │   ├── catalog_routes.py
    │   │   ├── category_routes.py
    │   │   ├── main.py
    │   │   └── product_routes.py
    ├── infra
    │   ├── __init__.py
    │   ├── http_server
    │   │   └── http_server.py
    │   ├── message_broker
    │   │   ├── __init__.py
    │   │   ├── message_broker_port.py
    │   │   └── rabbitmq
    │   │       ├── __init__.py
    │   │       └── rabbitmq_adapter.py
    │   └── orm
    │       ├── orm_port.py
    │       └── sqlalchemy_adapter.py
```

## Contribution

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please contact [your-email@example.com](mailto:your-email@example.com).

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
