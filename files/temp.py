import base64

def convert_image_to_string(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        image_string = f"data:image/png;base64,{encoded_image}"
        return image_string

# Usage example
image_path = "C:\\temp\\north_arrow_s.png"
result_path = "C:\\temp\\north_arrow_s.txt"
image_string = convert_image_to_string(image_path)
with open(result_path, "w") as result_path:
    result_path.write(image_string)
    
print('Done')