# VIN Decoder API

A lightweight, portfolio-ready REST API that decodes vehicle information based on a VIN prefix.  
Built using **FastAPI** and designed for demonstration purposes.

---

## Features

- FastAPI-based REST API  
- VIN decoding using prefix matching  
- Returns:
  - Make  
  - Model  
  - Year  
  - Trim  
- Built-in validation & error handling  
- Includes automated tests  
- JSON dataset for easy expansion  

---

## Project Structure
car-info-api/
│
├── src/
│ ├── app.py # Main API
│ ├── cars.json # Dataset
│ └── init.py
│
├── tests/
│ └── test_api.py # Unit tests
│
├── requirements.txt
├── README.md
└── .gitignore


---

## Running Locally

### 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Start the server
uvicorn src.app:app --reload

API will run at:
http://127.0.0.1:8000

### 4. Ready to Run:
Once you paste these files in:

```bash
cd car-info-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.app:app --reload


---

## Example

### Request:
GET /decode?vin=3TMKB5FN0SM050383


### Response:
```json
{
  "vin_prefix": "3TMKB5",
  "make": "Toyota",
  "model": "Tacoma",
  "year": 2024,
  "trim": "TRD Sport"
}

Run tests with:
pytest


