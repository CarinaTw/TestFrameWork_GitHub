import pytest
import re
import allure


@allure.feature('GitHub api')
@allure.story('GitHub Repository')
@allure.title('Test list repositories')
@pytest.mark.parametrize("user", ['CarinaTw', 'TestUser16082020'])
def test_list_all_repositories_for_user(method, url, user):
    response = method(url + '/users/{}/repos'.format(user))
    json = response.json()
    assert re.findall(user, json[0]['full_name']) and response.status_code == 200


@allure.feature('GitHub api')
@allure.story('GitHub Repository')
@allure.title('Test list repositories for not existed user')
@pytest.mark.parametrize("user", ['CarinaTw1', 'TestUser16082021'])
def test_list_all_repositories_for_not_existed_user(method, url, user):
    with allure.step('Отправка запроса {}'.format(method) + 'на endpoint {}'.format(url + '/users/{}/repos'.format(user))):
        response = method(url + '/users/{}/repos'.format(user))
        assert response.status_code == 404


@allure.feature('GitHub api')
@allure.story('GitHub Repository')
@allure.title('Test list repositories and sort by desc')
@pytest.mark.parametrize("user", ['TestUser16082020'])
def test_list_all_repositories_for_user_sort_by_full_name_desc(method, url, user):
    params = {'sort': 'full_name', 'direction': 'desc'}
    response = method(url + '/users/{}/repos'.format(user), params=params)
    json = response.json()
    list_resp = []
    for i in json:
        list_resp.append(i['name'])
    list_sorted_abc = sorted(list_resp)
    assert list_resp != list_sorted_abc and (list_resp[0] == list_sorted_abc[len(list_sorted_abc)-1])


