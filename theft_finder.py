import pandas as pd
import mysql.connector
from datetime import datetime, timedelta

# Set the percentage drop
drop_percentage = 10

# Connect to the MySQL server
db = mysql.connector.connect(user='fuel', password='CHANGE_ME', host='localhost', database='fuel')

# Create a new cursor
cursor = db.cursor()

# Execute a query to fetch all the  data
cursor.execute("SELECT date_time, fuel FROM fuel_data ORDER BY date_time ASC")

# Fetch all the rows
rows = cursor.fetchall()

# Convert the rows to a DataFrame
df = pd.DataFrame(rows, columns=['date_time', 'fuel'])

# Close the cursor and the connection
cursor.close()
db.close()

# Ensure date_time is in datetime format
df['date_time'] = pd.to_datetime(df['date_time'])

# Group by 10-minute intervals and calculate the average fuel value
df_grouped = df.resample('10T', on='date_time').mean()

# Add a new column to the DataFrame with the percentage change in 'fuel'
df_grouped['percentage_change'] = df_grouped['fuel'].pct_change() * 100

# Find the rows where the percentage change is less than the negative drop_percentage
drop_rows = df_grouped[df_grouped['percentage_change'] < -drop_percentage]

# Print the date_time and percentage change for these rows
for index, row in drop_rows.iterrows():
    print(f"At {index}, fuel dropped by {abs(row['percentage_change']):.2f}%")
