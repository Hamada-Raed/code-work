from flask import Flask, render_template, request, redirect, flash
import os
from PIL import Image 
app = Flask(__name__)
app.secret_key = "" 
 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  
 
MIN_RESOLUTION = (800, 600)
MAX_RESOLUTION = (4000, 3000)
ALLOWED_ASPECT_RATIOS = [(4, 3), (16, 9)]
 
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
def validate_image(image):
    
    if not allowed_file(image.filename):
        return "Invalid file format. Allowed formats are PNG, JPG, JPEG, GIF."
 
    image.seek(0, os.SEEK_END)
    file_size = image.tell()
    if file_size > MAX_FILE_SIZE:
        return f"File size too large. Max size is 5MB."
 
    image.seek(0)
 
    img = Image.open(image)
    width, height = img.size
 
    if width < MIN_RESOLUTION[0] or height < MIN_RESOLUTION[1]:
        return f"Resolution too small. Minimum resolution is {MIN_RESOLUTION[0]}x{MIN_RESOLUTION[1]}."
    if width > MAX_RESOLUTION[0] or height > MAX_RESOLUTION[1]:
        return f"Resolution too large. Maximum resolution is {MAX_RESOLUTION[0]}x{MAX_RESOLUTION[1]}."
 
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    aspect_ratio = (width // gcd(width, height), height // gcd(width, height))
    if aspect_ratio not in ALLOWED_ASPECT_RATIOS:
        return f"Invalid aspect ratio. Allowed ratios are 4:3 or 16:9."
 
    return None  
 
@app.route('/')
def upload_form():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Image Upload - Tourism Office</title>
<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 20px;
            }
            form {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
            input[type="file"] {
                padding: 10px;
                margin-top: 10px;
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .message {
                color: red;
                margin-top: 10px;
            }
</style>
</head>
<body>
<h1>Tourism Office - Image Upload</h1>
<form action="/upload" method="POST" enctype="multipart/form-data">
<input type="file" name="image" required>
<button type="submit">Upload Image</button>
</form>
</body>
</html>
    '''
 
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return redirect('/')
 
    image = request.files['image']
 
    if image.filename == '':
        flash('No selected file')
        return redirect('/')
 
    validation_error = validate_image(image)
    if validation_error:
        return f'<h3 class="message">{validation_error}</h3><br><a href="/">Go Back</a>'
 
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    return f'<h3>Image uploaded successfully!</h3><br><a href="/">Upload another image</a>'
 
if __name__ == "__main__":
    app.run(debug=True)