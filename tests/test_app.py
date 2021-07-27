def test_index(app, client):
    res = client.get('/') #test
    assert res.status_code == 200 