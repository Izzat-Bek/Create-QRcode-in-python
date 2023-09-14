import qrcode

data = input("Please enter text or url ... \n")
img = qrcode.make(data)
img.save("Qrcode.png")
