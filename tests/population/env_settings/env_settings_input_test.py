import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestEnvSettingsInput(BaseTest):
    """
    Test class that checks the input validation on the variables that can be
    edited through the Environmental Settings pane in the Population window.
    """

    def test_input_dishsize_negnum(self,
                                   bp: BasePage,
                                   pp: PopulationPage,):
        """
        Tests that crashes and unexpected behaviors do not occur if a negative
        number is given to the dish size boxes.

        :return: None.
        """

        # Edit dish size with nonsensical values.
        pp.show_env_settings()
        pp.edit_dish_cols("-12")
        pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        bp.add_ancestor_to_dish()
        pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_dishsize_zero(self,
                                 bp: BasePage,
                                 pp: PopulationPage,):
        """
        Tests that crashes and unexpected behaviors do not occur if a dish size
        dimension is set to 0.

        :return: None.
        """

        # Edit dish size with nonsensical values.
        pp.show_env_settings()
        pp.edit_dish_cols("0")
        pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        bp.add_ancestor_to_dish()
        pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_dishsize_str(self,
                                bp: BasePage,
                                pp: PopulationPage):
        """
        Tests that crashes and unexpected behaviors do not occur if a
        non-numeric string is given to the dish size boxes.

        :return: None.
        """

        # Edit dish size with nonsensical values.
        pp.show_env_settings()
        pp.edit_dish_cols("sample text")
        pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        bp.add_ancestor_to_dish()
        pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_mut(self,
                       bp: BasePage,
                       pp: PopulationPage):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with nonsensical value.
        pp.show_env_settings()
        pp.edit_mut_rate("-12")
        pp.hide_env_settings()

        # Add an organism to the dish and try to run it.
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_exp()
        pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        bp.util.sleep(3)
