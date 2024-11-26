import os
import cv2
import numpy as np
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PROCESSED_FOLDER'] = 'static/processed/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Function to perform background removal using GrabCut
def remove_background(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Check if the image is valid
    if img is None:
        raise ValueError("The image is invalid or not found.")
    
    # Create a mask for background removal
    mask = np.zeros(img.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    
    # Define the region to process (using GrabCut)
    rect = (10, 10, img.shape[1] - 10, img.shape[0] - 10)
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    
    # Create a mask for the foreground (object) and background
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    
    # Apply the mask to the image
    img_result = img * mask2[:, :, np.newaxis]
    
    # Convert the image to include an alpha channel for transparency
    result_with_alpha = cv2.cvtColor(img_result, cv2.COLOR_BGR2BGRA)
    
    # Set the alpha channel for the background to be transparent
    result_with_alpha[:, :, 3] = mask2 * 255
    
    # Ensure the output file has a .png extension
    output_path = os.path.splitext(output_path)[0] + ".png"
    
    # Save the image in PNG format with transparency
    cv2.imwrite(output_path, result_with_alpha)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        # Ensure the filename is secure
        original_filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        
        # Ensure processed file is saved with .png extension
        processed_filename = os.path.splitext(original_filename)[0] + ".png"
        processed_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)

        # Save the uploaded file
        file.save(upload_path)
        
        # Process the image to remove the background
        remove_background(upload_path, processed_path)

        # Render the result page with the paths of the images
        return render_template('result.html', original=upload_path, processed=processed_path)

    return 'Invalid file type.', 400

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True)

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)
    app.run(debug=True)
