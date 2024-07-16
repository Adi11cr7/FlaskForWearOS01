from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
heart_rate_data = []

@app.route('/heart_rate', methods=['POST'])
def receive_heart_rate():
    data = request.json
    heart_rate_data.append(data['heart_rate'])
    return jsonify({"status": "success"})

@app.route('/')
def index():
    return render_template('index.html', heart_rate_data=heart_rate_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
