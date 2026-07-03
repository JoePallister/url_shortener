#!/usr/bin/env bash

set -e

BASE_URL="http://127.0.0.1:8000/urls"

echo "Getting all URLs..."
echo

response=$(curl -s -X GET "$BASE_URL")

echo "Response:"
echo "$response" | jq