
import requests

def test_get_products():
    res = requests.get("https://dummyjson.com/products/1")
    assert res.status_code == 200

def test_post_add_product():
    payload = {"title": "Test Phone"}
    res = requests.post("https://dummyjson.com/products/add", json=payload)
    assert res.status_code in [200, 201,429]

def test_status_code_404():
    res = requests.get("https://dummyjson.com/products/999999")
    assert res.status_code in [404,429]