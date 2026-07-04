To run the api cd into app, activate the venv and run

uvicorn main:app --reload

Need to remember: 

Use short_code as the DB index since we will be doing lookups (including uniqueness lookup) on it

Table could later have 

created_at
expires_at (optional)
click_count (optional later)

On collision have chosen to generate a new code

How do we redirect? The short URL should first go to our API

URL validation