""" Compute accuracy of predictions """
import json
import numpy as np
import pandas as pd
from db import get_predictions


config = json.load(open("config.json"))
target = config["automl"]["target"]
predicted = config["automl"]["predicted"]
id_column = config["automl"]["id"]

test = pd.read_csv("data/test.csv", index_col=id_column)
predictions = get_predictions()
test[predicted] = predictions[predicted]

accuracy = np.round(np.sum(test[predicted] == test[target]) / test.shape[0] * 100.0, 2)
print(f"Accuracy: {accuracy}%")
