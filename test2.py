import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname="rypqppqx", user="rypqppqx", password="lMK--PkVbssahx106ktkFtP_dY-0blPY",
                        host="fanny.db.elephantsql.com", port="5432")


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM tasks")

# Retrieve query results
records = cur.fetchall()