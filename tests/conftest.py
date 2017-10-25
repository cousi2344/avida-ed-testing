import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.yield_fixture(scope="session")
def driver_setup(request, browser, online, setuipath, setffpath, seturl):
    wdf = WebDriverFactory(browser, online, setuipath, setffpath, seturl)
    driver = wdf.get_webdriver_instance()

    yield driver
    wdf.clean_webdriver_instance()
    driver.quit()


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


def pytest_addoption(parser):
    parser.addoption("--browser",
                     help="Name of internet browser used for testing.")
    parser.addoption("--online",
                     action="store_true",
                     default=False,
                     help="True if a local copy of Avida-ED should be run.")
    parser.addoption("--setuipath",
                     help="Path for folder containing local Avida-ED files.")
    parser.addoption("--setffpath",
                     help="Path for Firefox binary.")
    parser.addoption("--seturl",
                     help="URL for web-hosted Avida-ED.")
    parser.addoption("--runslow",
                     action="store_true",
                     default=False,
                     help="Run all tests, including time-consuming ones.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def online(request):
    return request.config.getoption("--online")


@pytest.fixture(scope="session")
def setuipath(request):
    return request.config.getoption("--setuipath")


@pytest.fixture(scope="session")
def setffpath(request):
    return request.config.getoption("--setffpath")


@pytest.fixture(scope="session")
def seturl(request):
    return request.config.getoption("--seturl")
