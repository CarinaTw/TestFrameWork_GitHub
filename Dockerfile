FROM python:3.6

WORKDIR /home/app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD pytest tests/test_github_list_repos_for_user.py --method=get --alluredir allure-reports ; pytest tests/test_github_create_new_repos.py --method=post --alluredir allure-reports ; pytest tests/test_github_create_new_branch.py --method=post --alluredir allure-reports
