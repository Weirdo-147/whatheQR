from flask import Flask, request, render_template, send_file
import qrcode
import io
import os
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    qr_type = request.form.get("type")
    text = request.form.get("data")

    if not text:
        return "No text provided!", 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Handle different QR code types based on user input
    if qr_type == "url":
        qr.add_data(text)
    elif qr_type == "wifi":
        # Expect format: SSID,Password
        if len(text.split(',')) == 2:
            ssid, password = text.split(',')
            qr.add_data(f"WIFI:T:WPA;S:{ssid};P:{password};;")
        else:
            return "Invalid Wi-Fi format! Use SSID,Password.", 400
    elif qr_type == "email":
        # Expect format: email,subject,body
        if len(text.split(',')) == 3:
            email, subject, body = text.split(',')
            qr.add_data(f"mailto:{email}?subject={subject}&body={body}")
        else:
            return "Invalid email format! Use email,subject,body.", 400
    elif qr_type == "sms":
        # Expect format: phone,message
        if len(text.split(',')) == 2:
            phone, message = text.split(',')
            qr.add_data(f"SMSTO:{phone}:{message}")
        else:
            return "Invalid SMS format! Use phone,message.", 400
    elif qr_type == "vcard":
        # Expect format: name,phone,email
        if len(text.split(',')) == 3:
            name, phone, email = text.split(',')
            qr.add_data(f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD")
        else:
            return "Invalid vCard format! Use name,phone,email.", 400
    elif qr_type == "geo":
        # Expect format: latitude,longitude
        if len(text.split(',')) == 2:
            lat, lng = text.split(',')
            qr.add_data(f"geo:{lat},{lng}")
        else:
            return "Invalid geolocation format! Use latitude,longitude.", 400
    elif qr_type == "calendar":
        # Expect format: summary,start_time,end_time,location,description
        if len(text.split(',')) == 5:
            summary, start_time, end_time, location, description = text.split(',')
            qr.add_data(f"BEGIN:VEVENT\nSUMMARY:{summary}\nDTSTART:{start_time}\nDTEND:{end_time}\nLOCATION:{location}\nDESCRIPTION:{description}\nEND:VEVENT")
        else:
            return "Invalid calendar format! Use summary,start_time,end_time,location,description.", 400
    else:
        qr.add_data(text)  # Custom text

    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save QR Code to BytesIO and send as response
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    # return send_file(img_io, mimetype='image/png')
    return render_template("wtQR.html", img_base64=img_base64)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if not set
    app.run(host="0.0.0.0", port=port, debug=True)
