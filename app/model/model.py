# import pickle
# import sklearn.externals as extjoblib
import joblib
from pathlib import Path 

__version__ = "0.1.0"

BASE_DIR =Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/phishing-{__version__}.pkl", "rb") as f:
    model = joblib.load(f)

def predict_pipeline(features):
    X_predict = []
    X_predict.append(str(features))
    y_Predict = model.predict(X_predict)
    if y_Predict == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"

    return (features, result)