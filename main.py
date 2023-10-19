# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI
import joblib

app = FastAPI()

#pkl
phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

# ML Aspect
@app.get('/predict/{feature}')
async def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return (features, result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)