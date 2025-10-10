🚀 QR Code Generator

A simple and powerful QR Code Generator Web App built with Django 🐍.
Easily generate, download, and share beautiful QR codes in seconds — no coding skills required! ✨

📸 Preview
<img width="1919" height="1028" alt="Screenshot 2025-10-10 175600" src="https://github.com/user-attachments/assets/c2b20c74-ab82-48f1-b79f-14e717be3b77" />
<img width="1919" height="969" alt="Screenshot 2025-10-10 175622" src="https://github.com/user-attachments/assets/048c8b96-b7b3-4337-a698-b56de0062bc8" />



🧠 Features

✅ Generate custom QR codes instantly
🎨 Stylish, modern, and fully responsive UI
🧭 Gradient design theme
📥 Download QR codes with one click
🔐 100% secure — no data is stored
📱 Works smoothly on desktop and mobile
💡 Built using Django + Bootstrap + Font Awesome

📂 Project Structure
qr-generator/
├── qr_app/
│   ├── templates/
│   │   ├── home.html
│   │   ├── features.html
│   │   ├── help.html
│   │   ├── about.html
│   │   └── generate.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── image/
│   └── views.py
├── qr_generator/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md

🧰 Tech Stack

🐍 Django — Backend framework

🧭 HTML5 / CSS3 / Bootstrap — Frontend UI

🖼️ Font Awesome — Icons

🧠 qrcode Python package — QR generation

⚡ How to Clone & Run Locally
1. 📥 Clone the repository
git clone https://github.com/kunalkt5656/qr-generator.git
cd qr-generator

2. 🐍 Create and activate a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate

3. 📦 Install dependencies
pip install -r requirements.txt

4. ⚙️ Run migrations
python manage.py migrate

5. 🚀 Start the development server
python manage.py runserver

6. 🌐 Open in browser
http://127.0.0.1:8000/

🧪 How It Works

✍️ Enter your text or URL

🪄 Click Generate QR

🖼️ Your custom QR Code will appear

📥 Click Download to save it as an image

🌟 Pages Included

🏠 Home Page – Landing page with CTA

🧭 Features Page – Highlights of the app

🆘 Help Page – Guide for new users

🧑‍💻 About Page – Info about the project

📸 QR Generator Page – Actual QR creation tool

🛡️ Future Improvements

✨ Add dynamic QR customization (color, logo, etc.)
🖼️ Allow users to upload logos inside QR
📊 Add scan analytics
📲 Share QR directly to social media

🧑‍💻 Author

Kunal Thakur
📍 Built with ❤️ using Django
🌐 Your Portfolio Link
 | 🐙 GitHub
 | 💼 LinkedIn

📜 License

This project is licensed under the MIT License.
Feel free to use and modify it for personal or commercial projects.
