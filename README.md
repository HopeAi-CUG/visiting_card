# 🪪 Visiting Card to Text (AI Powered)

An AI-powered web application that extracts text details from visiting/business cards using **OpenAI Vision**, allows users to **edit extracted data**, and **automatically stores it in Google Sheets**.

This project is useful for automating contact data entry, CRM lead capture, and business card digitization.

---

## 🚀 Features

- 📸 Upload or capture visiting card image (mobile & desktop supported)
- 🤖 AI-based text extraction from images
- ✏️ Editable extracted details before saving
- 📊 Automatically saves data to Google Sheets
- 🔐 Secure Google Sheets access using Service Account
- ⚡ Clean and responsive UI
- 🧾 Timestamped entries in Google Sheets

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- OpenAI (Vision Model via LangChain)
- Google Sheets API

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### Other Tools
- Google Service Account
- dotenv
- LangChain OpenAI

---

## 📂 Project Structure

<img width="384" height="463" alt="image" src="https://github.com/user-attachments/assets/1f8f5aa0-8482-4742-94b6-e85d8aa646c1" />



---

## 🔄 Application Flow

1. User uploads or captures a visiting card image
2. Image is sent to OpenAI Vision for text extraction
3. Extracted data is shown in an editable form
4. On confirmation, data is saved to Google Sheets
5. Each entry includes an automatic timestamp

---

## 📋 Extracted Fields

- Organization Name
- Person Name
- Contact Number
- Email ID
- Website
- Address
- Date & Time (auto-generated)

---

## 🔐 Environment Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/visiting-card-to-text.git
cd visiting-card-to-text

## 2️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

📊 Google Sheets Setup

Create a project in Google Cloud Console

Enable Google Sheets API

Create a Service Account

Download the credentials.json file

Place credentials.json in the project root directory

Share your Google Sheet with the service account email

Update the Spreadsheet details in google_sheets.py

SPREADSHEET_ID = "your_google_sheet_id"
SHEET_NAME = "Sheet1"

▶️ Run the Application

Start the Flask server:

python app.py


Open the application in your browser:

http://localhost:5000

🧪 API Endpoints
Method	Endpoint	Description
GET	/	Upload UI
POST	/extract-card	Extract card details
POST	/save-card	Save data to Google Sheets
GET	/health	Health check







