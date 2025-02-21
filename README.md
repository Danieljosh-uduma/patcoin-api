# Patcoin API

Welcome to the Patcoin API project!
This project is designed to manage a user referral system for the Patcoin cryptocurrency. It allows users to refer others and track their referral status and rewards.
This API allows users to interact with the Patcoin cryptocurrency system.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the Patcoin API, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Danieljosh-uduma/patcoin-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd patcoin-api
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the API server, run:
```bash
python manage.py runserver
```

The server will start on `http://localhost:8000`.

## Endpoints

Here are some of the main endpoints available in the Patcoin API:

- `GET /api/v1/wallets` - Retrieve a list of wallets
- `POST /api/v1/wallets` - Create a new wallet
- `GET /api/v1/transactions` - Retrieve a list of transactions
- `POST /api/v1/transactions` - Create a new transaction

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.