def test_create_short_url(client):
    res = client.post("/shorten", json={"url": "https://example.com/"})

    assert res.status_code == 200
    data = res.json()

    assert "short_url" in data
    short_url = data["short_url"]
    assert len(short_url) == 8
    for char in short_url:
        assert char.isalnum()


def test_expand_short_url(client):
    # First, create a short URL
    res = client.post("/shorten", json={"url": "https://example.com/"})
    assert res.status_code == 200
    short_url = res.json()["short_url"]

    # Now, expand the short URL
    res = client.get(f"/?short_url={short_url}")
    assert res.status_code == 200
    data = res.json()

    assert data == "https://example.com/"
