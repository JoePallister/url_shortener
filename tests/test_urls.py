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
    res = client.post("/shorten", json={"url": "https://example.com/"})
    short_url = res.json()["short_url"]

    res = client.get(f"/{short_url}", follow_redirects=False)
    assert res.status_code in (307, 308)
    assert res.headers["location"] == "https://example.com/"


def test_caching(client, fake_redis):
    res = client.post("/shorten", json={"url": "https://example.com/"})
    short_url = res.json()["short_url"]

    assert fake_redis.successful_get_calls == 0
    assert fake_redis.set_calls == 0

    res = client.get(f"/{short_url}", follow_redirects=False)

    assert fake_redis.successful_get_calls == 0
    assert fake_redis.set_calls == 1

    res = client.get(f"/{short_url}", follow_redirects=False)
    assert fake_redis.successful_get_calls == 1
    assert fake_redis.set_calls == 1
