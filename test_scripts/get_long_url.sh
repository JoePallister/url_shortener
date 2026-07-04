#!/usr/bin/env bash

set -e

SHORT_URL=$1

BASE_URL="http://127.0.0.1:8000/$SHORT_URL"

echo "Getting long URL for $SHORT_URL at $BASE_URL"
echo

response=$(curl -s -X GET "$BASE_URL")

echo "Response:"
echo "$response" | jq