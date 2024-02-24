import pandas as pd
import mysql.connector

# Set the percentage drop
drop_percentage = 5

# Connect to the MySQL server
db = mysql.connector.connect(user='fuel', password='CHANGE_ME', host='localhost', database='fuel')

# Create a new cursor
cursor = db.cursor()

# Execute a query to fetch data
query = "SELECT date_time, fuel FROM fuel_data ORDER BY date_time ASC"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Convert the rows to a DataFrame
df = pd.DataFrame(rows, columns=['date_time', 'fuel'])

# Add a new column to the DataFrame with the percentage change in 'fuel'
df['percentage_change'] = df['fuel'].pct_change() * 100

# Find the rows where the percentage change is less than the negative drop_percentage
drop_rows = df[df['percentage_change'] < -drop_percentage]

# Print the date_time and percentage change for these rows
for index, row in drop_rows.iterrows():
    print(f"At {row['date_time']}, fuel dropped by {abs(row['percentage_change']):.2f}%")

# Close the cursor and the connection
cursor.close()
db.close()
