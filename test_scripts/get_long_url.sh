#!/usr/bin/env bash

set -e

SHORT_URL=$1

BASE_URL="http://127.0.0.1:8000/expand?short_url=$SHORT_URL"

echo "Getting long URL for short URL..."
echo

response=$(curl -s -X GET "$BASE_URL")

echo "Response:"
echo "$response" | jq