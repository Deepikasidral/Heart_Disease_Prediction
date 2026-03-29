from fastapi import FastAPI
from routes import user_routes, prediction_routes

app = FastAPI()

# Include Routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(prediction_routes.router, prefix="/predictions", tags=["Predictions"])

@app.get("/")
def home():
    return {"message": "Heart Disease Backend Running"}