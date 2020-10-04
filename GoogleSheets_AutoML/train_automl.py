from sheets import get_train_data,get_client,write_out
from supervised import AutoML
import pandas as pd
from sklearn.model_selection import train_test_split


# get the training data
df_name = "sheet name"
cred_path = "path/credentials.json"
email = "shahules786@gmail.com"


client = get_client(cred_path)

X_train, y_train = get_train_data(client,df_name)
# train AutoML
X_train,X_test,y_train,y_test = train_test_split(X_train,y_train,test_size=0.1)

automl = AutoML(results_path="Automl_output",total_time_limit=10)
#automl.fit(X_train, y_train)

train_pred = automl.predict(X_train)
test_pred = automl.predict(X_test)

data = {'train_target':y_train,"train_prediction":train_pred,
        'test_target':y_test,'test_prediction':test_pred}

write_out(client,data,email)