from flask import Flask, request, send_from_directory, jsonify
import os
import json

app = Flask(__name__)

# Path to the file you want to serve
FILE_PATH = './files'
FILE_NAME = 'client.exe'

# Create the directory if it doesn't exist
os.makedirs(FILE_PATH, exist_ok=True)

@app.route('/download', methods=['GET'])
def download_file():
    try:
        return send_from_directory(FILE_PATH, FILE_NAME, as_attachment=True, mimetype='application/octet-stream')
    except FileNotFoundError:
        return jsonify({"status": "error", "message": f"{FILE_NAME} not found"}), 404

# Endpoint to receive the JSON report from client
@app.route('/report', methods=['POST'])
def receive_report():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
        
        # Save JSON report to a file
        report_path = os.path.join(FILE_PATH, 'report.json')
        with open(report_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Received report: {json.dumps(data, indent=4)}")
        
        return jsonify({"status": "success", "message": "Report received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53535)
