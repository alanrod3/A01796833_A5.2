# Sales Analysis Tool (Activity 5.2)

This project contains a Python script to calculate total sales from a price catalogue and a sales record JSON file. It is designed to be efficient, robust against data errors, and PEP-8 compliant.

## Structure
- `Pruebas_y_Calidad/5.2/source/`: Contains the main script `computeSales.py` and list of Products `ProductList.json` .
- `Pruebas_y_Calidad/5.2/tests/`: Contains test JSON files e.g. `TC1-Sales.json`.
- `Pruebas_y_Calidad/5.2/results/`: Stores the output execution results.

## Prerequisites
- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt

## Usage 
python3 Pruebas_y_Calidad/5.2/source/computeSales.py Pruebas_y_Calidad/5.2/source/ProductList.json Pruebas_y_Calidad/5.2/tests/TC1-Sales.json
