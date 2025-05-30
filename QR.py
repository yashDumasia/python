import qrcode

data = input("Enter Text or URL : ").strip()
file = input("Enter File Name : ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(file)
print(f"QR code save in {file}")
