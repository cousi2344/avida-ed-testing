import pytest
from base.base_page import BasePage

from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestMenuBarStartup(BaseTest):
    """
    Test class that tests the initial configuration of the main menu bar at the
    top of the Avida-ED website to ensure that the correct menu options are
    accessible at startup.
    """

    def test_freezer_menu_launch(self,
                                 bp: BasePage):
        """
        Tests that the correct menu options in the Freezer tab are usable on
        startup.

        :return: None.
        """
        assert not bp.can_save_current_pop()
        assert not bp.can_save_selected_org()
        assert not bp.can_save_offspring_org()

    def test_control_menu_launch(self,
                                 bp: BasePage):
        """
        Tests that the correct menu options in the Control tab are usable on
        startup.

        :return: None.
        """
        assert bp.can_run_from_menu()
        assert not bp.can_pause_from_menu()
        assert not bp.can_bring_to_org_window()
        assert not bp.can_bring_child_to_org_window()
