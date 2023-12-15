def get_qrcode(filepath, base64_string):
    image_data = base64.b64decode(base64_string)
    with open(f"app/{filepath}", 'wb') as f:
         f.write(image_data)

get_qrcode()