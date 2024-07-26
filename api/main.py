from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("../Training/models/model5.keras")


def read_file_as_image(data) -> np.ndarray:
    return np.array(Image.open(BytesIO(data)))


@app.get("/ping")
async def ping():
    return "Hello"


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(file.read())


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8550)
