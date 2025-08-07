# 🐍 Base Python image
FROM python:3.11-slim

# 👨‍💻 Set working directory
WORKDIR /app

# 🧾 Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📦 Copy the full project
COPY . .

# 🔑 Set environment file
ENV PYTHONUNBUFFERED=1

# 🚀 Start the bot
CMD ["python", "run.py"]
