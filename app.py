from flask import Flask, send_from_directory

app = Flask(__name__)

FILE_PATH = './files' 
FILE_NAME = 'client.exe' 

@app.route('/download')
def download_file():
    return send_from_directory(FILE_PATH, FILE_NAME, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)