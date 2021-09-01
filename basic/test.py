import qrcode

url = "google.com"
file_name = "qrcode"

img = qrcode.make(url)
img.save(f"{file_name}.jpg")