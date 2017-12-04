import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestExperimentControls(BaseTest):
    """
    Test class that runs a very simple experiment in Avida-ED.
    """

    def test_exp_run_controls(self,
                              bp: BasePage,
                              pp: PopulationPage):
        """
        Tests that a simple experiment can be run and that running, pausing, and
        doing one update work as expected.

        :return: None.
        """

        # Add @ancestor to dish.
        bp.add_ancestor_to_dish()

        # Run the experiment.
        bp.run_from_menu()
        bp.util.sleep(3, "Waiting for updates to occur.")

        # Assert that updates have occurred.
        assert pp.get_pop_current_update() > 0
        assert pp.gr_get_pop_current_update() > 0

        # Pause the experiment.
        bp.pause_from_menu()
        bp.util.sleep(1, "Making sure pause goes into effect.")

        # Get current update, wait a few seconds, assert it has not changed.
        current_update = pp.get_pop_current_update()
        bp.util.sleep(3, "Ensuring no updates occur after pause.")
        assert pp.get_pop_current_update() == current_update

        # Do one update
        bp.forward_from_menu()
        bp.util.sleep(1, "Making sure update has time to occur.")
        assert (pp.get_pop_current_update() - current_update) == 1
