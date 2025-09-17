from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/api")
def api():
    # Connect to PostgreSQL on backend
    conn = psycopg2.connect(
        host="192.168.20.10",  
        dbname="testdb",
        user="test_user",
        password="!Edu1234"
    )
    cur = conn.cursor()
    cur.execute("SELECT content FROM test_table LIMIT 1;")
    db_result = cur.fetchone()[0]
    cur.close()
    conn.close()

    # Read file from Samba share mounted locally
    # E.g., you mounted it at /mnt/share
    with open("/mnt/secure_share/file.txt") as f:
        file_content = f.read()

    return jsonify({
        "db_data": db_result,
        "file_data": file_content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

