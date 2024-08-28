# install libraries neede
# create function that collects text & converts it to QR code
# save the QR code as image
# run the function

import qrcode

def generate_qrcode(text):
    qr= qrcode.QRCode(
        version =1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,    
    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg01.png")

url= input("Enter your URL: ")
generate_qrcode(url)