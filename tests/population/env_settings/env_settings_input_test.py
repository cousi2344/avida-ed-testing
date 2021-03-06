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

        # Edit dish size with negative values.
        pp.show_env_settings()
        pp.edit_dish_cols("-12")
        pp.hide_env_settings()
        assert pp.check_size_cells_error()

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

        # Edit dish size with value zero.
        pp.show_env_settings()
        pp.edit_dish_cols("0")
        pp.hide_env_settings()
        assert pp.check_size_cells_error()

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

        # Edit dish size with string values.
        pp.show_env_settings()
        pp.edit_dish_cols("sample text")
        pp.hide_env_settings()
        assert pp.check_size_cells_error()

        # Add an organism to the experiment and try to run it.
        bp.add_ancestor_to_dish()
        pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_dish_size_floating_point(self,
                                  bp: BasePage,
                                  pp: PopulationPage):
        """
        Tests that crashes and unexpected behaviors do not occur if a
        floating point number is given in the dish size boxes.

        :return: None.
        """

        # Edit dish size with a floating point number.
        pp.show_env_settings()
        pp.edit_dish_cols("10.5")
        pp.hide_env_settings()
        assert pp.check_size_cells_error()

        # Add an organism to the experiment and try to run it.
        bp.add_ancestor_to_dish()
        pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_mut_negative(self,
                       bp: BasePage,
                       pp: PopulationPage):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with negative value.
        pp.show_env_settings()
        pp.edit_mut_rate("-12")
        pp.hide_env_settings()
        assert pp.check_mutation_rate_error()

        # Add an organism to the dish and try to run it.
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_exp()
        pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_mut_string(self,
                                bp: BasePage,
                                pp: PopulationPage):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with string value.
        pp.show_env_settings()
        pp.edit_mut_rate("m&ms")
        pp.hide_env_settings()
        assert pp.check_mutation_rate_error()

        # Add an organism to the dish and try to run it.
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_exp()
        pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_mut_btwn_hundred_and_thousand(self,
                                bp: BasePage,
                                pp: PopulationPage):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with value between 100 and 1000.
        pp.show_env_settings()
        pp.edit_mut_rate("500")
        pp.hide_env_settings()
        assert pp.check_mutation_rate_error()

        # Add an organism to the dish and try to run it.
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_exp()
        pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        bp.util.sleep(3)

    def test_input_mut_over_thousand(self,
                                bp: BasePage,
                                pp: PopulationPage):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with value over 1000.
        pp.show_env_settings()
        pp.edit_mut_rate("5000")
        pp.hide_env_settings()
        assert pp.check_mutation_rate_error()

        # Add an organism to the dish and try to run it.
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_exp()
        pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        bp.util.sleep(3)


