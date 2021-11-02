# Create a database instance, and connect to it.
from databases import Database


async def main():
    database = Database('postgresql://rypqppqx:lMK--PkVbssahx106ktkFtP_dY-0blPY@fanny.db.elephantsql.com/tasks')
    await database.connect()

    # Create a table.
    query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query)

    # Insert some data.
    query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
    values = [
        {"name": "Daisy", "score": 92},
        {"name": "Neil", "score": 87},
        {"name": "Carol", "score": 43},
    ]
    await database.execute_many(query=query, values=values)

    #  Run a database query.
    query = "SELECT * FROM HighScores"
    rows = await database.fetch_all(query=query)
    print('High Scores:', rows)

if __name__ == '__main__':
    main()

