def test_create_short_url(client):
    res = client.post("/shorten", json={"url": "https://example.com"})

    assert res.status_code == 200
    data = res.json()

    assert "short_url" in data
