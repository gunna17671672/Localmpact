from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to LocalImpact Dashboard!"

@app.route('/api/dashboard')
def dashboard_data():
    data = {
        "total_volunteers": 42,
        "total_hours": 200,
        "upcoming_events": 3
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
