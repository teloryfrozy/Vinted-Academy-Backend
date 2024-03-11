# Vinted-Academy-Backend
🐍 Python Shipment discount calculation module for Vinted Academy

## Features

- Calculate shipment prices and apply discounts based on the guidelines provided in the assignment.
- Unit tests of functions are written in `tests/tests.py`.
- Code is clearly written, organized, and divided into three main modules:
  - **Data Accessor (`utils/data_accessor.py`):** Access and return the data from predefined constants in `utils/constants.py`.
  - **Data Validator (`utils/data_validator.py`):** Validate the conformity of data to ensure accurate processing.
  - **Engine (`utils/engine.py`):** Handle the execution of algorithms for shipment discount calculations.
- An executor `main.py` file that coordinates the overall process of adding discounts to the transactions.


## Metadata
- Author: Augustin ROLET ([GitHub](https://github.com/teloryfrozy/))
- Version: 1.0.0


## Requirements
- Python 3 - Version used in development: 3.11.2


## Get started
```bash
git clone -b main https://github.com/teloryfrozy/Vinted-Academy-Backend.git
cd Vinted-Academy-Backend
python main.py input.txt
```