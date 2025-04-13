import psycopg2

conn = psycopg2.connect(
    dbname='lab_10',
    user='postgres',
    password='on2606',
    host='localhost',
    port=5433
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS snake_game_scores (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(100),
    score INTEGER,
    level INTEGER
);
""")

conn.commit()
cur.close()
conn.close()

print("Таблица успешно создана!")
