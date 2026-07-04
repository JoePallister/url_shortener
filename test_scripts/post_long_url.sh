#!/usr/bin/env bash

set -e

LONG_URL=$1

BASE_URL="http://127.0.0.1:8000/shorten"

echo "Testing URL shortener..."
echo "URL: $LONG_URL"
echo

response=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$LONG_URL\"}")

echo "Response:"
echo "$response"
echo