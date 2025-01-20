from flask import Flask, render_template, jsonify
import sqlite3
import os

app = Flask(__name__)

# Route for the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch weight data
@app.route('/weight', methods=['GET'])
def get_weight_data():
    try:
        db_path = os.path.join('..', 'database', 'project.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weight_logs ORDER BY timestamp DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return jsonify({
                "weight": result[1],
                "voltages": result[2:10],  # voltage1 through voltage8
                "timestamp": result[10]
            })
        return jsonify({"error": "No data found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
