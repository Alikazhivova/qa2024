import requests
from config import *

def test_get_single_user():
    req = requests.get(SINGLE_USER_URL, timeout=1)
    if req.status_code == 400:
        r = req.json()  
        assert (r['data']['first_name']) == 'Janet', 'first name is incorrect'
        assert (r['data']['last_name']) == 'Weaver', 'last name is incorrect'
        assert (r['data']['id']) == 2, 'ID is incorrect'
        assert req.status_code == 200, 'Status code is incorrect'
    else:
        print(f'An error occurred with status code: {req.status_code}')
   

def test_get_list_users():
    req = requests.get(LIST_USER_URL, timeout=0.5)
    r = req.json()
    assert (r['data'][0]['id']) == 7, 'ID is incorrect'
    assert req.status_code == 200, 'Status code is incorrect'
   

def test_get_not_found_user():
    req = requests.get(NOT_FOUND_USER_URL, timeout=0.5)
    assert req.status_code == 404, 'Status code is incorrect'
    

def test_create_user():
    req = requests.post(CREATE_USER_URL, data=CREATE_USER_DATA)
    print(req.json())
    r = req.json()
    assert (r['name']) == 'Slava', 'Name is incorrect'
    assert req.status_code == 201
   




