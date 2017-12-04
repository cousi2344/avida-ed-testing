import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestAvidaEdTab(BaseTest):
    """
    Test class that tests the Avida-ED tab of the main menu bar.
    """

    def test_about_page(self,
                        bp: BasePage):
        """
        Tests that the about page works properly.

        :return: None.
        """
        bp.open_avida_ed_about()
        assert bp.avida_ed_about_displayed()
        bp.close_avida_ed_about()
        assert not bp.avida_ed_about_displayed()

