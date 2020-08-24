import pytest
import json
import random
import re


@pytest.mark.parametrize("user", ["TestUser16082020"])
def test_create_new_branch(method, url, user):
    token = 'a033237c65d2c8be410fc170d7876ddfd465dbf3'
    branch_name = 'api_branch' + str(random.randint(1, 1000))
    ref = 'refs/heads/' + branch_name
    sha = 'f884ae51b3e7f645822307a97e31a7a9e76142d4'

    payload = {'ref': ref, 'sha': sha}
    response = method(url + '/repos/'+user+'/kek/git/refs', auth=(user, token), data=json.dumps(payload))

    rc = response.content
    mystr = rc.decode('utf-8')
    dd = json.loads(mystr)

    assert (response.status_code == 200 or response.status_code == 201) and re.findall(branch_name, dd['url'])


@pytest.mark.parametrize("user", ["TestUser16082020"])
def test_create_new_branch_same_name(method, url, user):
    token = 'a033237c65d2c8be410fc170d7876ddfd465dbf3'
    branch_name = 'api_branch' + str(random.randint(1, 1000))
    ref = 'refs/heads/' + branch_name
    sha = 'f884ae51b3e7f645822307a97e31a7a9e76142d4'

    payload = {'ref': ref, 'sha': sha}
    response = method(url + '/repos/'+user+'/kek/git/refs', auth=(user, token), data=json.dumps(payload))
    response2 = method(url + '/repos/'+user+'/kek/git/refs', auth=(user, token), data=json.dumps(payload))

    assert response.status_code == 201 and response2.status_code == 422