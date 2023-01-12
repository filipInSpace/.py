
#Author: Filip Navrkal

import qrcode

def generate_qr(link):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")

if __name__ == '__main__':
    link = input("Enter the link you want to generate QR code for: ")
    generate_qr(link)
    print("QR code generated and saved as 'qr.png'!")
