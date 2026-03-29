#!/bin/bash

TOKEN=$1
CHAT_ID=$2
MESSAGE=$3

if [ -z "$TOKEN" ] || [ -z "$CHAT_ID" ]; then
    echo "Ошибка: не указан токен или chat_id"
    echo "Использование: ./notify.sh <TOKEN> <CHAT_ID> <MESSAGE>"
    exit 1
fi

if [ -z "$MESSAGE" ]; then
    MESSAGE="Тестовое уведомление от pipeline"
fi

RESPONSE=$(curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
    -d "chat_id=${CHAT_ID}" \
    -d "text=${MESSAGE}" \
    -d "parse_mode=HTML" \
    -d "disable_web_page_preview=true")

echo "Ответ Telegram API:"
echo "$RESPONSE"
