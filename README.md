# Twitch UI Mobile Automation Test (WAP)

Automated UI test using **Python + Selenium** for the **mobile version of Twitch**.

- Emulates a mobile device: `Pixel 2`  
- Uses the **Page Object Model (POM)** structure  
- Handles pop-ups, dynamic elements, and captures a screenshot

---

## What this test does

1. Opens Twitch in a mobile browser emulator
2. Searches for **StarCraft II**
3. Clicks on **"View All"** to load full results
4. Scrolls down **2 times**
5. Opens the **first available stream**
6. Closes pop-up (if one appears)
7. Takes a screenshot of the streamer's page 📸

---

## Installation

> Make sure you have **Python 3.10+** and **Google Chrome v135+** installed

```bash
# Clone the repository
git clone https://github.com/MaxVolobuev/python-automation-twitch
cd python-automation-twitch

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Create a .env file in the project root:
echo "ENV=prod" > .env
```

---

## ▶ Run the test

```bash
# One-line setup & test run (recommended)
make test
```

---

## For Contributors

If you add or update dependencies, please update `requirements.txt` using:

```bash
pip list --format=freeze > requirements.txt
```

> This ensures the file stays clean and only contains top-level project dependencies.

---

Screenshots will be saved in the `screenshots/` folder.  
Example filename: `streamer_page_2025-04-07_22-10-03.png`

---

## Demo GIF

<p align="center">
  <img src="https://github.com/MaxVolobuev/python-automation-twitch/raw/main/demo.gif" alt="Demo" />
</p>

---

---

## Project Structure

```
python-automation-twitch/
├── config/
│   └── config_loader.py
├── pages/
│   ├── twitch_directory_page.py
│   └── twitch_stream_page.py
├── tests/
│   ├── twitch_search.py
├── .env
├── .gitignore
├── demo.gif
├── Makefile
├── README.md
└── requirements.txt
```

---

## Author

**Maksym Volobuiev**  
Made with ❤️ for automation and streaming

---

## License

MIT — free to use, improve, share.  
Give credit if helpful
