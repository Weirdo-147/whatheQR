
# WhatheQR - QR Code Generator

**WhatheQR** is a simple and user-friendly web app that allows you to generate QR codes for various types of data, including URLs, Wi-Fi credentials, emails, SMS, vCards, geolocation, calendar events, and custom text.

## Features

- **URL QR Code**: Generate a QR code that directs to a specific URL.
- **Wi-Fi Credentials QR Code**: Generate a QR code that automatically connects users to a Wi-Fi network.
- **Email QR Code**: Generate a QR code that pre-fills an email for the user.
- **SMS QR Code**: Generate a QR code that pre-fills a text message.
- **vCard QR Code**: Generate a QR code with a contact's details.
- **Geolocation QR Code**: Generate a QR code that directs users to a location on a map.
- **Calendar Event QR Code**: Generate a QR code with event details for adding to the calendar.
- **Custom Text QR Code**: Create a QR code from any custom text.

## How to Use

1. **Select QR Code Type**: Choose the type of QR code you want to generate from the dropdown menu (e.g., URL, Wi-Fi, Email, etc.).
2. **Enter Data**: Depending on your selection, input the relevant information in the text field.
   - For URL: Simply enter the website URL.
   - For Wi-Fi: Enter Wi-Fi SSID and password in the format `SSID,Password`.
   - For Email: Enter email address, subject, and body in the format `email@example.com,Subject,Body`.
   - For SMS: Enter phone number and message in the format `+1234567890,Message`.
   - For vCard: Enter name, phone, and email in the format `Name,Phone,Email`.
   - For Geolocation: Enter latitude and longitude in the format `LAT,LNG`.
   - For Calendar Event: Enter event details in the format `EventName,StartTime,EndTime,Location,Description`.
   - For Custom Text: Enter any text you want to encode.
3. **Generate QR Code**: After entering the required information, click the "Generate QR Code" button.
4. **Download QR Code**: Once the QR code is generated, you can download or scan it with any QR scanner.

## Installation

### Requirements

- Python 3.x
- Flask
- `qrcode` library
- `gunicorn` for production (optional but recommended for Heroku deployment)

### Set Up Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/whattheqr.git
   cd whattheqr
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   python app.py
   ```

4. Open the app in your browser at `http://127.0.0.1:5000/`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [Heroku](https://www.heroku.com/)

---

Made by **Dheeraj** - 2024
```
