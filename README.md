# 🤖 T34Po – PocketOption Signal Auto-Trader

**T34Po** is a lightweight version of the original T34 trading bot.  
It auto-clicks the "Accept" button from the official PocketOption Telegram bot and tracks your profit & loss hourly.  
No API needed, no risky logic — just smooth signal following.

---

## ⚙️ Features

✅ Auto-clicks "Accept" on @PocketSignalBot messages  
✅ Tracks live balance automatically  
✅ Logs hourly profit/loss reports  
✅ Lightweight – no external trading APIs  
✅ Works 24/7 (can be hosted on DigitalOcean or any VPS)

---

## 📁 Project Structure

t34po/
├── core/
│ └── listener.py # Listens to signals, clicks, tracks balance
├── utils/
│ └── tracker.py # Handles balance logging and hourly report
├── run.py # Script entry point
├── .env # Telegram credentials
├── requirements.txt # Python dependencies
├── balance_log.json # Auto-created balance history
├── Dockerfile            ✅ NEW
├── docker-compose.yml    ✅ NEW
└── README.md # This file

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-user/t34po.git
cd t34po
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup .env
Create a .env file with your Telegram API credentials (from my.telegram.org):

```env
Tel_API_ID=123456
Tel_API_HASH=your_api_hash_here
```

### 4. Run the bot

python run.py

```bash
python run.py
```

✅ On first run, you’ll be asked to log into Telegram.

### 5. Docker (For deployment) (optional)
Make sure .env is in the root of t34po/

```bash
# Build the Docker image
docker-compose build

# Run it
docker-compose up -d

# Check logs
docker logs -f t34po

# Stop & Restart Anytime
docker-compose stop       # Stop without killing
docker-compose start      # Start again
docker-compose down       # Fully shut down
```

## 💬 Credits
Built by **Badzone**
Powering smarter bots, safer trading ⚡
Website: **https://badzone.co**

## ⚠️ Disclaimer
This bot uses publicly visible signals and makes no trading decisions of its own.
Use at your own risk. Badzone is not responsible for trading losses.