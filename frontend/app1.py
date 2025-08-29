from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/api")
def api():
    # 1️⃣ Connect to PostgreSQL on VM4
    conn = psycopg2.connect(
        host="192.168.174.129",  # <-- your VM4 IP
        dbname="testdb",
        user="testuser",
        password="testpass"
    )
    cur = conn.cursor()
    cur.execute("SELECT info FROM testtable LIMIT 1;")
    db_result = cur.fetchone()[0]
    cur.close()
    conn.close()

    # 2️⃣ Read file from Samba share mounted locally
    # E.g., you mounted it at /mnt/share
    with open("/mnt/share/file.txt") as f:
        file_content = f.read()

    return jsonify({
        "db_data": db_result,
        "file_data": file_content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
