# write a code which can connect to the database and should have 3 functionality
# 1. create a new record 2.show the records 3. exit from the program
import psycopg2


"""
# Connect to the PostgreSQL database local running instance
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
    port="5432"
)

# Connect to the PostgreSQL database container running instance
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="container_ip",# this u can get from the docker inspect command like 172.17.0.2
    port="5432"
)

# Connect to the PostgreSQL database container in a same network running instance(both should be on same network)
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="container_name", #like postgres(my container name)
    port="5432"
)
"""
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432"
)

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS records (id SERIAL PRIMARY KEY, data TEXT)''')

# Function to create a new record
def create_record(data):
    c.execute("INSERT INTO records (data) VALUES (%s)", (data,))
    conn.commit()

# Function to show all records
def show_records():
    c.execute("SELECT * FROM records")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Main program loop
while True:
    print("1. Create a new record")
    print("2. Show all records")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data for the new record: ")
        create_record(data)
    elif choice == "2":
        show_records()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()