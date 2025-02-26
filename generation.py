import pandas as pd
import qrcode
import os

from PIL import Image, ImageDraw, ImageFont
with open ("Paper Size.txt", "r") as file:
    content = file.read().strip()

width, height = map(int, content.split(","))

os.makedirs("QRImages", exist_ok=True)

font = ImageFont.truetype("arial.ttf",int(width/20))
df = pd.read_excel("Sign ups.xlsx")
# Create the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=(height/100)-1,  # Size of each box in the QR grid
    border=height/400,  # Border thickness
)
# Loop through each row
for index, row in df.iterrows():
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)
    # Get the LinkedIn URL and Full Name for this row
    linkedInLink = row['LinkedIn']
    name = row['Full Name']
    studentID = str(row['Student ID'])
    program = str(row['Field Of Study'])
    year = "Year "+str(row['Year Of Study'])
    qr.add_data(linkedInLink)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_width, qr_height = qr_img.size

    # Create a blank image with the paper size

    # Paste the QR code in the bottom right corner
    qr_x = width - qr_width - 10  # 10px padding from the right
    qr_y = height - qr_height - 10  # 10px padding from the bottom
    img.paste(qr_img, (qr_x, qr_y))
    draw.text((width-qr_width+20, height/4), studentID, fill="black", font=font)
    draw.text((width/40,height/4),name,fill="black",font=font)
    draw.text((width/40,height/3),program,fill="black", font = font)
    draw.text((width/40,height/2),year,fill="black",font=font)
    # Save the final image
    img.save(f"QRImages/qrcode_{str(name)}.png")
