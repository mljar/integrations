from db import get_live_data
from db import insert_predictions

from supervised import AutoML


X_live, ids = get_live_data()
if X_live is None or not X_live.shape[0]:
    print("No new data")
else:
    print("Compute predictions")
    automl = AutoML(results_path="Response_Classifier")
    predictions = automl.predict(X_live)
    print("Insert prediction into DB")
    insert_predictions(predictions, ids)
