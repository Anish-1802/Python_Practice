import mysql.connector

# Step 1: Connect to the database
db_connection = mysql.connector.connect(
    host="10.155.1.64",  # usually "localhost" or an IP address
    user="inven96412",  # your MySQL username
    password="Feb@2025",  # your MySQL password
    database="INGREAD"  # the database name
)

# Step 2: Create a cursor to interact with the database
cursor = db_connection.cursor()

# Step 3: Write the query to fetch the first 2 entries from the desired column
# Example: Let's assume you have a table called 'your_table' and a column called 'your_column'
query = "SELECT your_column FROM your_table LIMIT 2;"

# Step 4: Execute the query
cursor.execute(query)

# Step 5: Fetch the results
results = cursor.fetchall()

# Step 6: Display the results
for row in results:
    print(row[0])  # Access the first column in each row

# Step 7: Close the cursor and connection
cursor.close()
db_connection.close()
