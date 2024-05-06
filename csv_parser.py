from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['finkart_test']
collection = db['finkart_col']

def upload_file(file_name='sample_transactions_500_rows.csv'):
    df = pd.read_csv(file_name)
    list_of_dicts = df.to_dict(orient='records')
    collection.insert_many(list_of_dicts)

def delete_record(transaction_id):
    collection.delete_one({"TransactionID": transaction_id})

def update_record(transaction_id, updated_record):
    collection.update_one({"TransactionID": transaction_id}, updated_record)

def get_all_records():
    all_records = collection.find()
    return all_records




