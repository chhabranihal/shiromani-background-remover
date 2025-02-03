from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

# Ensure templates folder exists
if not os.path.exists("templates"):
    os.makedirs("templates")

@app.route('/')
def index():
    return render_template('index.html')  # Ensure "index.html" is inside the "templates" folder

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    image = Image.open(file.stream)
    output = remove(image)

    # Save the output image to a bytes buffer
    buf = io.BytesIO()
    output.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run on all interfaces
