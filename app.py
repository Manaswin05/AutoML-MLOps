from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from analyse import make_predict
import numpy as np

app = FastAPI()

# ---- Home Route ----
@app.get("/")
def home():
    return {"message": "Welcome to ML API System 🚀"}

# ---- Weather Prediction API ----
@app.get("/api/weather")
def weather_prediction(
    temperature: float = Query(..., description="Temperature"),
    humidity: float = Query(..., description="Humidity"),
    wind_speed: float = Query(..., description="Wind_speed")
):
    result = make_predict(
        "weather",
        [temperature, humidity, wind_speed]
    )

    return {
        "message": "Weather Prediction",
        "input": {
            "temperature": f"{temperature}°C",
            "humidity": f"{humidity}%",
            "wind_speed": f"{wind_speed} m/s"
        },
        "feels_like": f"{round(float(result), 2)}°C"
    }

# GET API
@app.get("/api/nexus")
def nexus(
    day : int = Query(..., description="Day of the month"),
    month : int = Query(..., description="Month of the year"),
    year : int = Query(..., description="Year"),
):
    check_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(month==2 and year % 4 == 0 or year%4000 == 0):
        check_days[1] = 29
        return {
            "message": "Invalid date generated. Please try again."
        }
    elif (month == 2 and day > check_days[month - 1]):
        return {
            "message": "Invalid date generated. Please try again."
        }
    result = make_predict(
        "nexus",
        [day, month, year]
    )
    return {
        "message": "Nexus Prediction",
        "input": {
            "day": day,
            "month": month,
            "year": year
        },
        "estimated value" : round(float(result), 2)
    }


@app.get("/api/random-nexus")
def get_data():
    day = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = np.random.randint(2018, 2031)
    result = make_predict(
        "nexus",
        [day, month, year]
    )
    return {
        "message": "Nexus Prediction",
        "input": {
            "day": day,
            "month": month,
            "year": year
        },
        "estimated value" : round(float(result), 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=3000, reload=True)