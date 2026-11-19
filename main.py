import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="test",
    user="postgres",
    password="Dmail12345",
)
cur = conn.cursor()
cur.execute(
    "SELECT id,name,email from person where id>%s",(0,),
)
rows=cur.fetchall()
for person_id, name, email in rows:
    print(person_id, name, email)
cur.execute("select count(*) from person")
total=cur.fetchone()[0]