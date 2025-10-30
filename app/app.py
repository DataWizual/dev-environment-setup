from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            dbname=os.getenv("DB_NAME", "postgres")
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Database connection successful!'")
        message = cur.fetchone()[0]
        cur.close()
        conn.close()
    except Exception as e:
        message = f"Database connection failed: {e}"
    return f"<h2>{message}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
