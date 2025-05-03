# SROSentry

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/SRO-Server-Browser/SROSentry)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange)](https://github.com/SRO-Server-Browser/SROSentry/blob/main/CONTRIBUTING.md)

**SROSentry** is a customizable AI bot designed for Silkroad Online (VSRO) servers, delivering announcements to players with style! From event notifications to maintenance alerts, it sends concise messages via a SQL and Python-based system powered by Google’s Gemini API. Define your bot’s name and tone—witty, professional, or epic—and engage your community! 🚚💬

## Features
- **Customizable Messaging:** Set your bot’s name and tone (e.g., humorous, serious, or adventurous).
- **Global & Private Messages:** Send announcements to the entire server or specific players.
- **SQL Integration:** Works with `_Announcement_AI` table and `_SendMessage_FromAI` procedure for KGuardEDGE compatibility.
- **Secure & Fast:** Messages are sanitized against SQL injection and checked every 5 seconds.
- **Gemini API:** Leverages Google’s Generative AI for dynamic, tailored responses.

## Installation
### Requirements
- Python 3.8+
- SQL Server (ODBC Driver 17 for SQL Server)
- Google Gemini API Key ([Google Cloud Console](https://cloud.google.com))
- Python libraries: `pyodbc`, `python-dotenv`, `google-generativeai`

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SRO-Server-Browser/SROSentry.git
   cd SROSentry
   ```

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain a Gemini API Key:**
   - Visit [Google Cloud Console](https://cloud.google.com).
   - Create a new project and enable the “Generative AI” API.
   - Navigate to Credentials, click “Create API Key,” and copy the key.
   - Add it to the `.env` file as `api_key=YOUR-TOKEN`.

4. **Set Up SQL Structure:**
   - Add the `_Announcement_AI` table and `_SendMessage_FromAI` procedure to the `Panel_Silvarya` database (scripts in `sql/` folder).
   - Ensure the `_DeveloperCommands` table exists in the KGuardEDGE database.

5. **Configure the `.env` File:**
   - Example `.env`:
     ```
     api_key=YOUR-TOKEN
     DRIVER={ODBC Driver 17 for SQL Server}
     SERVER=SQL_IP
     UID=sa
     PWD=Password
     Timeout=5
     ```

6. **Run the Bot:**
   ```bash
   python main.py
   ```

## Customizing the Bot
Define your bot’s identity in the `.env` file:
- **BOT_NAME:** Choose a unique name (e.g., `CaravanGuide`, `SilkroadSage`).
- **BOT_ROLE:** Set the bot’s tone. Examples:
  - Humorous: `You are {BOT_NAME}, guiding Silkroad players. Keep messages witty, short, and under 150 characters!`
  - Professional: `You are {BOT_NAME}, guiding Silkroad players. Keep messages clear, informative, and professional.`
  - Epic: `You are {BOT_NAME}, a legendary Silkroad guide. Make messages epic and thrilling!`

**Example Outputs:**
- Input: "Medusa event started!"
  - Humorous: "Medusa’s snakes are ready to party! Join or get stoned! 🐍😜"
  - Professional: "Medusa event is live. Join now to earn rewards!"
  - Epic: "Medusa’s curse awakens! Brave the arena, hero!"

## Example Usage
1. Add an announcement to the `_Announcement_AI` table:
   ```sql
   INSERT INTO Panel_Silvarya.dbo._Announcement_AI (_message, TargetCharName, TargetCharID, _private)
   VALUES ('Jangan trade festival started!', NULL, NULL, 0);
   ```

2. The bot processes the message, enhances it via Gemini, and sends it to KGuardEDGE:
   - Output (e.g., humorous): "Jangan’s caravans are rolling! Grab the gold, quick! 🚚💰"

## Troubleshooting
- **Connection Issues:** Verify SQL credentials in the `.env` file.
- **API Quota Errors:** Check your Gemini API usage in [Google Cloud Console](https://cloud.google.com).
- **Message Issues:** Review logs in `main.py` output.

## Contributing
We welcome your ideas and contributions! To contribute:
1. Fork the repository.
2. Make your changes and submit a pull request.
3. Share with the Silkroad community! 🚀

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
[MIT License](LICENSE) - See the `LICENSE` file for details.

## Contact
Have questions? Reach out on the [VSRO.org forums](https://vsro.org) or open an issue on [GitHub](https://github.com/SRO-Server-Browser/SROSentry/issues).

**Note:** Consult your server admin before deploying. Misconfigured bots might send caravans the wrong way! 😅
