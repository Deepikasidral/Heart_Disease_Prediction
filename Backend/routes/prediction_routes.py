from fastapi import APIRouter
from db import predictions_collection
from models.prediction import Prediction
from bson import ObjectId
import datetime

router = APIRouter()

@router.post("/add_prediction")
def add_prediction(pred: Prediction):
    pred_dict = pred.dict()

    # Convert string to ObjectId
    pred_dict["user_id"] = ObjectId(pred.user_id)
    pred_dict["timestamp"] = datetime.datetime.now()

    predictions_collection.insert_one(pred_dict)

    return {"message": "Prediction saved successfully"}

@router.get("/get_predictions/{user_id}")
def get_predictions(user_id: str):
    data = list(predictions_collection.find(
        {"user_id": ObjectId(user_id)},
        {"_id": 0}
    ))
    return {"predictions": data}