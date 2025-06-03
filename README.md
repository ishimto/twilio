# Twilio GitLab Automation Bot

This project automates user and project creation in GitLab using data from a Google Sheet, and provides a Twilio WhatsApp bot interface for retrieving contact information.

---

## Features

- **GitLab Automation:** Automatically creates users, assigns them to a group, and creates projects for each user based on data from a Google Sheet.
- **Twilio WhatsApp Bot:** Responds to WhatsApp messages with contact information from the same Google Sheet.
- **Google Sheets Integration:** Uses Google Sheets as the source of truth for user and contact data.

---

## Project Structure

```
main.py
modules/
    bot.py
    create_user.py
    envs.py
    parse.py
    sheet_auth.py
    __init__.py
credentials.json
requirements.txt
.gitignore
__init__.py
```

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the project root or export these variables in your shell:

- `SHEET_ID`: Your Google Sheet ID
- `GITLAB_URL`: Your GitLab instance URL
- `GITLAB_TOKEN`: Your GitLab personal access token

Example `.env` file:
```
SHEET_ID=your_google_sheet_id
GITLAB_URL=https://gitlab.example.com
GITLAB_TOKEN=your_gitlab_token
```

### 5. Google Service Account

- Place your `credentials.json` (Google service account credentials) in the project root.

### 6. Run the application

```bash
python main.py
```

---

## Exposing the Python App with ngrok

To receive WhatsApp messages from Twilio, your Flask app must be accessible from the internet. You can use [ngrok](https://ngrok.com/) to expose your local server:

```bash
ngrok http 5000
```

Copy the generated `https://xxxx.ngrok.io` URL.

---

## Configure Twilio WhatsApp Sandbox

1. Go to the [Twilio Console WhatsApp Sandbox](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp/sandbox).
2. In the **"WHEN A MESSAGE COMES IN"** field, enter:
   ```
   https://xxxx.ngrok.io/...
   ```
   (Replace `xxxx.ngrok.io` with your ngrok URL.)
3. Save the changes.

Now, when you send a WhatsApp message to your Twilio Sandbox number, Twilio will forward it to your local Flask app.

---

## Usage

- **GitLab Automation:** On startup, the app reads user data from the Google Sheet and creates users, assigns them to the `main-group`, and creates projects for them.
- **Twilio WhatsApp Bot:** Send a WhatsApp message (e.g., `contacts`) to your Twilio Sandbox number. The bot will reply with a list of contacts from the Google Sheet.

---

## File Descriptions

- `main.py`: Entry point; runs GitLab user creation and starts the Flask app.
- `modules/bot.py`: Implements the Twilio WhatsApp bot using Flask.
- `modules/create_user.py`: Handles GitLab user and project creation.
- `modules/parse.py`: Parses data from the Google Sheet.
- `modules/sheet_auth.py`: Authenticates and connects to Google Sheets.
- `modules/envs.py`: Loads environment variables.
