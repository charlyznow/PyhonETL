import json 

conn = {}
conn['connections'] = []

conn ['connections'] .append(
     { 
        'conn_type' : 's3',
        'AccessKey': 'AKIAXSN4OVOENWJIOAF3',
        'SecretAccessKey' : 'fF2p8tEUoeO0D5TpCaT1N9rFGHXbZo/Jddw7XJjS',
        'region': 'us-east-1'
})

"""
Example add new conexion
    data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
"""
with open ('connections.json', 'w') as file:
    json.dump(conn ,file)