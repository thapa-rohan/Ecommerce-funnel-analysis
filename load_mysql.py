import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='borutouzumaki7A@',
    database='funnel_db'
)
cursor = conn.cursor()

# Load funnel stages
stages = [
    ('data/home_page_table.csv', 'homepage'),
    ('data/search_page_table.csv', 'search_page'),
    ('data/payment_page_table.csv', 'payment_page'),
    ('data/payment_confirmation_table.csv', 'purchase')
]

for file, stage in stages:
    df = pd.read_csv(file)
    for uid in df['user_id']:
        cursor.execute('INSERT INTO funnel_events VALUES (%s, %s)', (int(uid), stage))

# Load users
users = pd.read_csv('data/user_table.csv')
for _, row in users.iterrows():
    cursor.execute('INSERT INTO users VALUES (%s, %s, %s, %s)', 
        (int(row['user_id']), row['date'], row['device'], row['sex']))

conn.commit()
print('Data loaded!')
cursor.close()
conn.close()