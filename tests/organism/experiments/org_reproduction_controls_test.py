import pytest
from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage
from tests.base_test import BaseTest


class TestOrgRepControls(BaseTest):
    """
    Test class that runs simple experiments with the organism window
    reproduction.
    """

    def test_org_rep_ctrl_startup(self,
                                  bp: BasePage,
                                  op: OrganismPage):
        """
        Tests that the control for Organism Reproduction are not enabled on
        startup.

        :return: None.
        """
        op.go_to_organism()
        assert not op.org_rep_controls_enabled()
        assert op.org_rep_controls_disabled()
        assert op.get_cycle() == 0

    def test_org_rep_ctrl_functionality(self,
                                        bp: BasePage,
                                        op: OrganismPage):
        """
        Tests that the controls for Organism Reproduction work as intended once
        an organism is loaded into the dish.

        :return: None.
        """
        # Put ancestor in organism view
        op.go_to_organism()
        bp.click_freezer_item("@ancestor")
        bp.add_org_to_org_view()

        # Wait for ancestor to be in org view, ensure initial values sensible.
        op.wait_until_org_controls_enabled()
        assert op.get_cycle() == 0

        # Test that forward and back options work.
        op.forward_org_rep()
        assert op.get_cycle() == 1
        op.back_org_rep()
        assert op.get_cycle() == 0

        # Test that running works.
        op.run_org_rep()
        op.util.sleep(1)
        assert op.get_cycle() > 0

        # Test that pausing works.
        op.stop_org_rep()
        cycle = op.get_cycle()
        op.util.sleep(1)
        assert op.get_cycle() == cycle

        # Test that End goes to end of reproduction.
        op.end_org_rep()
        assert op.get_cycle() == 189

        # Test that Reset goes back to 0.
        op.reset_org_rep()
        assert op.get_cycle() == 0
