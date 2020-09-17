from db import get_train_data
from supervised import AutoML


# get the training data
X_train, y_train = get_train_data()
# train AutoML
automl = AutoML(results_path="Response_Classifier")
automl.fit(X_train, y_train)
