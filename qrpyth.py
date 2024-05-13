import qrcode 
website_link = "https://www.instagram.com/lashattt/"
qr= qrcode.QRCode(version=7, box_size=7, border=7)
qr.add_data(website_link)
qr.make(fit=True)
img = qr.make_image(fill_color = 'purple', back_color = 'green')
img.save("q333r.png")