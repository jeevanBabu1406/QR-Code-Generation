import segno


vehicle_number = input("Enter the vehicle number: ")


github_url = "https://polite-cassata-78d298.netlify.app?vechile_number=" + vehicle_number


qr_code = segno.make(github_url)


qr_code.save("Vehicle_QR_Code.png", scale=7)

print("QR Code generated successfully for vehicle number:", vehicle_number)
