import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestPauseUpdate(BaseTest):
    """
    Test class that checks the input validation on the variables that can be
    edited through the Environmental Settings pane in the Population window.
    """

    def test_startup_pause_settings(self,
                                    pp: PopulationPage):
        """
        Tests that pause settings are correct on startup.

        :return: None.
        """

        assert pp.pause_manually_enabled()
        assert not pp.pause_at_update_enabled()

    def test_pause_at_update(self,
                             bp: BasePage,
                             pp: PopulationPage):
        """
        Tests that 'Pause at Update' setting will allow user to automatically
        pause the experiment at the given update.

        :return: None.
        """

        # Setup pause settings.
        pp.enable_pause_at_update()
        pp.edit_pause_update(9)

        # Set up the rest of the experiment.
        bp.add_ancestor_to_dish()

        # Run the experiment.
        bp.run_from_menu()

        # Wait long enough for experiment to have reached update 9.
        bp.util.sleep(10, "Waiting for experiment to pause automatically.")

        # Check that pause worked properly.
        assert pp.get_pop_current_update() == 9

        # Wait to make sure it is paused.
        bp.util.sleep(1, "Ensuring that experiment is paused.")
        assert pp.get_pop_current_update() == 9
