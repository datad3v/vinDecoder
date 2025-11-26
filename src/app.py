from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(
    title="Car Info Decoder API",
    description="Simple API that decodes car information from a VIN prefix.",
    version="1.0.0"
)

# Load the dataset once when the app starts
cars_path = Path(__file__).parent / "cars.json"
cars = json.loads(cars_path.read_text())

@app.get("/")
def root():
    return {"message": "Welcome to the Car Info Decoder API"}

@app.get("/decode")
def decode_car(vin: str):
    if len(vin) < 6:
        raise HTTPException(status_code=400, detail="VIN must be at least 6 characters.")
    
    vin_prefix = vin[:6].upper()

    for car in cars:
        if car["vin_prefix"] == vin_prefix:
            return {
                "vin_prefix": vin_prefix,
                "make": car["make"],
                "model": car["model"],
                "year": car["year"],
                "trim": car["trim"]
            }

    raise HTTPException(status_code=404, detail="Car not found for provided VIN prefix.")
