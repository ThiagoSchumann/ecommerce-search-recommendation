# Ecommerce Search and Recommendation

E-commerce search and recommendation system. Supports CRUD operations for products, search with filters and sorting, and personalized recommendations. Built with Flask, PostgreSQL, JWT, and RabbitMQ. Ideal for e-commerce developers seeking a comprehensive and scalable solution.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contribution](#contribution)
4. [License](#license)
5. [Contact](#contact)
6. [Additional Resources](#additional-resources)
7. [Mermaid Diagrams](#mermaid-diagrams)

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

## Contribution

1. Fork the repository.
2. Create your feature branch:
    ```bash
    git checkout -b feature/your-feature
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature
    ```
5. Open a pull request.

Please adhere to the code of conduct and follow the contribution guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For support or feedback, please contact:

**Thiago Schumann**  
[<img src="https://skillicons.dev/icons?i=linkedin" height="40">](https://www.linkedin.com/in/thiagoschumann/)
[<img src="https://skillicons.dev/icons?i=gmail" height="40">](mailto:thiagoarturschumann@gmail.com)
[<img src="https://skillicons.dev/icons?i=github" height="40">](https://github.com/ThiagoSchumann/)

**Adrian Grosch**  
[<img src="https://skillicons.dev/icons?i=linkedin" height="40">](https://www.linkedin.com/in/adriangrosch/)
[<img src="https://skillicons.dev/icons?i=gmail" height="40">](mailto:adriangrosch15@gmail.com)
[<img src="https://skillicons.dev/icons?i=github" height="40">](https://github.com/DricoGrosch)
