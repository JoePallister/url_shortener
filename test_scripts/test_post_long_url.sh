#!/usr/bin/env bash

set -e

BASE_URL="http://127.0.0.1:8000/shorten"

URL_TO_SHORTEN="https://example.com"

echo "Testing URL shortener..."
echo "URL: $URL_TO_SHORTEN"
echo

response=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$URL_TO_SHORTEN\"}")

echo "Response:"
echo "$response"
echo