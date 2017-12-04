import pytest

from base.base_page import BasePage

from specializations.population.population_page import PopulationPage
from specializations.organism.organism_page import OrganismPage
from specializations.analysis.analysis_page import AnalysisPage


@pytest.mark.usefixtures("driver_setup")
class BaseTest:
    """
    Test class that tests the initial configuration of the main menu bar at the
    top of the Avida-ED website to ensure that the correct menu options are
    accessible at startup.
    """

    bp = None
    pp = None
    op = None
    ap = None

    @pytest.yield_fixture(autouse=True, scope="class")
    def class_setup(self, request, bp: BasePage):
        """
        Sets up class prior to run. Adds necessary variables to the class and
        waits for the splash screen to go away.

        Also performs any necessary cleanup of the objects it instantiates after
        testing is completed.

        :return: None.
        """
        # Wait for splash screen to go away
        bp.wait_until_splash_gone()

        yield

        # Cleanup of logger object.
        bp.close_logger()

    @pytest.fixture(scope="class")
    def bp(self, driver_setup):
        return BasePage(driver_setup)

    @pytest.fixture(scope="class")
    def pp(self, driver_setup):
        return PopulationPage(driver_setup)

    @pytest.fixture(scope="class")
    def op(self, driver_setup):
        return OrganismPage(driver_setup)

    @pytest.fixture(scope="class")
    def ap(self, driver_setup):
        return AnalysisPage(driver_setup)

    @pytest.yield_fixture(autouse=True, scope="function")
    def closing_assertions(self, class_setup, bp: BasePage):
        """
        Performs basic assertions that should evaluate to True after every test
        (e.g. crash report not displayed, etc.).

        :return: None.
        """
        yield
        assert not bp.crash_report_displayed()

    @pytest.yield_fixture()
    def soft_reset(self, closing_assertions, pp: PopulationPage):
        """
        Performs a 'soft reset" at the beginning of an experiment by resetting
        the dish. In the future (when tests with Organism and Analysis window
        are in place) it will also do as much as possible to reset those
        windows.

        * Not Fully Implemented Yet *

        :return:
        """
        yield
        pp.new_exp_discard()

    @pytest.yield_fixture(autouse=True, scope="function")
    def hard_reset(self, closing_assertions, bp: BasePage):
        """
        Performs a 'hard reset' at the beginning of an experiment by refreshing
        the Avida-ED webpage and waits for it to load completely.

        Used by default, since tests no longer run in specific orders.

        :return: None.
        """
        yield
        bp.refresh_avida_ed()

