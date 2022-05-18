import pandas as pd 
import boto3 
import json 

with open ("connections.json", "r") as j:
    login = json.load(j)
    print(login)
    
    #se crea la branch