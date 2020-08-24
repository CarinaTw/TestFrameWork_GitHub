import pytest
import requests
import logging
logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.INFO, filename='logs.log')


class ApiClient:
    """
    Для работы с http-запросами
    """

    def __init__(self, base_addr):
        self.base_addr = base_addr

    def get(self, path="/", params=None):
        url = self.base_addr + path
        logger = logging.getLogger('')
        logger.info("\nGET request to {}".format(url))
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        help="This is request url",
        default='https://api.github.com'
    )

    parser.addoption(
        "--method",
        default="get",
        help="method to execute"
    )

    parser.addoption(
        "--status_code",
        default='200',
        help="status code"
    )


@pytest.fixture
def url(request):
    logger = logging.getLogger('')
    logger.info("URL {}".format(request.config.getoption("--url")))
    return request.config.getoption("--url")


@pytest.fixture
def method(request):
    m = request.config.getoption("--method")
    logger = logging.getLogger('')
    if m == "get":
        logger.info("METHOD {}".format(m))
        return requests.get
    elif m == "post":
        logger.info("METHOD {}".format(m))
        return requests.post
    else:
        return 'Please use following methods: get, post'


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return ApiClient(base_addr=base_url)

