# Create a database /tmp/movies.db using SQLite3
# Create a table in it called "MOVIES"
# Insert data

def liked_the_sql():
    import sqlite3
    conn = sqlite3.connect('/tmp/movies.db')
    c = conn.cursor()
    c.execute('CREATE TABLE MOVIES (title TEXT, director TEXT, year INT)')
    c.execute('INSERT INTO MOVIES VALUES ("The Dark Knight", "Christopher Nolan", 2008)')
    c.execute('INSERT INTO MOVIES VALUES ("Pulp Fiction", "Quentin Tarantino", 1994)')
    c.execute('INSERT INTO MOVIES VALUES ("Back to the Future", "Robert Zemeckis", 1985)')
    conn.commit()
    conn.close()
    return None