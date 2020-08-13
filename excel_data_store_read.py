import pandas as pd
import os

def DataStore(name,mobile_number,email,occupation):
    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        df=df.append(pd.DataFrame([[name,mobile_number,email,occupation]],
                        columns=["name","mobile_number","email","occupation"]))
        df.to_excel("user_data.xlsx",index=False)
    else:
        df=pd.DataFrame([[name,mobile_number,email,occupation]],
                        columns=["name","mobile_number","email","occupation"])
        df.to_excel("user_data.xlsx",index=False)
    return []

def FetchData(column,occupation):

    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        data=df[column][df["occupation"]==occupation]
        return data.to_list()
    else:
        return ["There is no data. "]