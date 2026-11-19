import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="test",
    user="postgres",
    password="Dmail12345",
)
cur = conn.cursor()
name=input("Enter your name: ")
cur.execute(
    "select *from users where name=%s",
    (name,)
)
cur.close()
