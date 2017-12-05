import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestPopulationNavigation(BaseTest):
    """
    Test class that tests navigation between various panels and sub-specializations within
    the Population page.
    """

    def test_toggle_env_settings(self,
                                 bp: BasePage,
                                 pp: PopulationPage):
        """
        Tests toggling the Environmental Settings panel on and off.
        
        :return: None. 
        """

        bp.go_to_population()
        pp.show_env_settings()
        assert pp.env_settings_displayed()
        assert not pp.grid_displayed()
        pp.hide_env_settings()
        assert not pp.env_settings_displayed()
        assert pp.grid_displayed()
        pp.show_env_settings()
        assert pp.env_settings_displayed()
        assert not pp.grid_displayed()

    def test_toggle_pop_stats(self,
                              bp: BasePage,
                              pp: PopulationPage):
        """
        Tests toggling the Population Statistics window on and off.
        
        :return: None. 
        """

        bp.go_to_population()
        pp.show_pop_stats()
        assert pp.pop_stats_displayed()
        pp.hide_pop_stats()
        assert not pp.pop_stats_displayed()
        pp.show_pop_stats()
        assert pp.pop_stats_displayed()

