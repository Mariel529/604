iimport pandas as pd
import sqlite3


customers_df = pd.read_csv('customer.csv')
orders_df = pd.read_csv('orders.csv')
# Transformation (Transforming and processing data)
# Merge the orders and customers dataframes on 'CustomerID' using an inner join
merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='inner')


merged_df['TotalAmount'] = merged_df['Quantity'] * merged_df['Price']


merged_df['Status'] = merged_df['OrderDate'].apply(lambda d: 'New' if d.startswith('2025-03') else 'Old')


high_value_orders = merged_df[merged_df['TotalAmount'] > 5000]

# Loading (Loading transformed data into the target database)
# Connect to an SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')

# Create a table (if it doesn't exist) to store high-value orders
create_table_query = '''
CREATE TABLE IF NOT EXISTS HighValueOrders (
    OrderID INTEGER,
    CustomerID INTEGER,
    Name TEXT,
    Email TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price REAL,
    OrderDate TEXT,
    TotalAmount REAL,
    Status TEXT
)
'''
conn.execute(create_table_query)# Execute the SQL query to create the table

# Load the filtered high-value orders into the database table
# Replace the table contents if it already exists
high_value_orders.to_sql('HighValueOrders', conn, if_exists='replace', index=False)

# Query the database to retrieve and print the high-value orders
result = conn.execute('SELECT * FROM HighValueOrders')
for row in result.fetchall():# Iterate through the query results and print each row
    print(row)

# Close the database connection
conn.close()
# Print a completion message
print("ETL process completed successfully!")

