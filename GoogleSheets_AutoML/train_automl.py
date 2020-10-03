from sheets import get_train_data
from supervised import AutoML


# get the training data
df_name = "credit_card"
cred_path = "/home/shahul/Downloads/mljar-1de77676a687.json"

X_train, y_train = get_train_data(df_name,cred_path)
# train AutoML
automl = AutoML(results_path="Automl_output")
automl.fit(X_train, y_train)