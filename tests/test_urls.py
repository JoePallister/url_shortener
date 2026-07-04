def test_create_short_url(client):
    res = client.post("/shorten", json={"url": "https://example.com"})

    assert res.status_code == 200
    data = res.json()

    assert "short_url" in data
    short_url = data["short_url"]
    assert len(short_url) == 8
    for char in short_url:
        assert char.isalnum()
