import pytest
import json
import random


@pytest.mark.parametrize("user", ["TestUser16082020"])
def test_create_new_repository_user_not_authorized(method, url, user):
    response = method(url + '/user/repos')
    assert response.status_code == 401


@pytest.mark.parametrize("user", ["TestUser16082020"])
def test_create_new_repository_authenticated_user(method, url, user):
    token = 'a033237c65d2c8be410fc170d7876ddfd465dbf3'
    repo = 'api_repo' + str(random.randint(1, 1000))
    description = 'Created with api'
    payload = {'name': repo, 'description': description, 'auto_init': 'true'}
    response = method(url + '/user/repos', auth=(user, token), data=json.dumps(payload))

    rc = response.content
    mystr = rc.decode('utf-8')
    dd = json.loads(mystr)

    assert (response.status_code == 200 or response.status_code == 201) and dd['name'] == repo


@pytest.mark.parametrize("user", ["TestUser16082020"])
def test_create_new_private_repository_authenticated_user(method, url, user):
    token = 'a033237c65d2c8be410fc170d7876ddfd465dbf3'
    repo = 'api_repo' + str(random.randint(1, 1000))
    description = 'Created with api'
    payload = {'name': repo, 'description': description, 'auto_init': 'true', 'private': True}
    response = method(url + '/user/repos', auth=(user, token), data=json.dumps(payload))

    rc = response.content
    mystr = rc.decode('utf-8')
    dd = json.loads(mystr)

    assert (response.status_code == 200 or response.status_code == 201) and dd['name'] == repo and dd['private'] is True
