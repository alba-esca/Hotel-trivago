import base64

def convert_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            return base64_image
    except Exception as e:
            print(f"Error converting image to base64: {e}")
            return None