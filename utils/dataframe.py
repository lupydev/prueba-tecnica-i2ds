from utils.login import login
import pandas as pd

def get_dataframe(file_id):
    credentials = login()
    file = credentials.CreateFile({'id': file_id})
    file.GetContentFile('prueba.xlsx')
    df = pd.read_excel('prueba.xlsx')
    return df