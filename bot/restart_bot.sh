#!/bin/bash
cd /home/ubuntu/Docker/broggy-discord-bot

if pgrep -f bot.py; then
    echo "Bot is running. Stopping bot..."
    pkill -f bot.py
    sleep 5
else
    echo "Bot is not running."
fi

echo "Pulling latest code..."
git pull

echo "Starting bot..."
( nohup python3 bot/bot.py > bot.log 2>&1 & )
echo "Bot started."
