import cv2
import pytesseract
from PIL import Image

def ocr_image(image_path, preprocess=False):
    """
    Perform OCR on an image file.

    :param image_path: Path to the image file.
    :param preprocess: Boolean flag to apply preprocessing (e.g., convert to grayscale).
    :return: Extracted text from the image.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Optionally preprocess the image
    if preprocess:
        # Convert the image to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to perform OCR on the image
    # Convert the image to a PIL Image object
    pil_image = Image.fromarray(image)

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(pil_image)

    return extracted_text

# Example usage
if __name__ == "__main__":
    image_path = 'download.png'
    text = ocr_image(image_path, preprocess=True)
    print("Extracted Text:")
    print(text)