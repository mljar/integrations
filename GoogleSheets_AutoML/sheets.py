import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def get_train_data(data,path):


    """
    data : the name of the  google sheet 
    path : path to the credentials json for Google API
    """    
    
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open(data)

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    records_df = pd.DataFrame.from_dict(records_data)

    return records_df.drop(['Class'],axis=1),records_df['Class']
