import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestOrgRepStats(BaseTest):
    """
    Test class that runs simple experiments with the organism window
    reproduction, specifically regarding to statistics.
    """

    def test_org_rep_stats_startup(self,
                                   bp: BasePage,
                                   op: OrganismPage):
        """
        Tests that the stats for Organism Reproduction are set to 0 at startup.

        :return: None.
        """
        op.go_to_organism()
        assert op.get_org_num_not_performed() == 0
        assert op.get_org_num_nan_performed() == 0
        assert op.get_org_num_and_performed() == 0
        assert op.get_org_num_orn_performed() == 0
        assert op.get_org_num_oro_performed() == 0
        assert op.get_org_num_ant_performed() == 0
        assert op.get_org_num_nor_performed() == 0
        assert op.get_org_num_xor_performed() == 0
        assert op.get_org_num_equ_performed() == 0

    def test_org_rep_stats_functionality(self,
                                         bp: BasePage,
                                         op: OrganismPage):
        """
        Tests that the controls for Organism Reproduction work as intended when
        an organism that can perform all functions is added to the dish.

        :return: None.
        """
        # Put all_functions in organism view
        op.go_to_organism()
        bp.click_freezer_item("@all_functions")
        bp.add_org_to_org_view()

        # Wait for ancestor to be in org view, ensure initial values sensible.
        op.wait_until_org_controls_enabled()

        # Make sure at beginning of reproduction, all stats 0.
        assert op.get_org_num_not_performed() == 0
        assert op.get_org_num_nan_performed() == 0
        assert op.get_org_num_and_performed() == 0
        assert op.get_org_num_orn_performed() == 0
        assert op.get_org_num_oro_performed() == 0
        assert op.get_org_num_ant_performed() == 0
        assert op.get_org_num_nor_performed() == 0
        assert op.get_org_num_xor_performed() == 0
        assert op.get_org_num_equ_performed() == 0

        # Go to end of reproduction.
        op.end_org_rep()

        # Assert that all functions have been performed.
        assert op.get_org_num_not_performed() == 1
        assert op.get_org_num_nan_performed() == 1
        assert op.get_org_num_and_performed() == 1
        assert op.get_org_num_orn_performed() == 1
        assert op.get_org_num_oro_performed() == 1
        assert op.get_org_num_ant_performed() == 1
        assert op.get_org_num_nor_performed() == 1
        assert op.get_org_num_xor_performed() == 1
        assert op.get_org_num_equ_performed() == 1
