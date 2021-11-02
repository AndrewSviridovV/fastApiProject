from databases import Database

DATABASE_URL = "postgresql://postgres:Yjdfz_7963@localhost:5432/tasks"
database = Database(DATABASE_URL)

# Establish the connection pool
await database.connect()
# Fetch multiple rows
query = "SELECT * FROM tasks"
rows = await database.fetch_all(query=query, values={"completed": True})

# Close all connection in the connection pool
await database.disconnect()


