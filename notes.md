# Running

To run the api activate the venv and run

```uvicorn app.main:app --reload```

# Testing

To test posting a long url to shorten it

```bash test_scripts/post_long_url.sh "https://example.com"```

To test getting the long url from a short url 

```bash test_scripts/get_long_url.sh <your-short-url>```

Or to get all urls stored

```bash test_scripts/get_all_urls.sh```

Run pytest with

```python -m pytest```

# Notes

Table could later have 

created_at
expires_at (optional)
click_count (optional later)

How do we redirect? The short URL should first go to our API

URL validation

What are aliases here?