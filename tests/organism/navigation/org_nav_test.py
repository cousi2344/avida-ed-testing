import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestOrganismNavigation(BaseTest):
    """
    Test class that tests navigation between the panels and other sub-specializations
    within the Organism page.
    """

    def test_toggle_org_settings(self,
                                 bp: BasePage,
                                 op: OrganismPage):
        """
        Tests closing the Organism Settings pop-up.

        :return: None.
        """

        bp.go_to_organism()
        op.open_org_settings()
        assert op.org_settings_displayed()
        op.close_org_settings()
        bp.util.sleep(1)
        assert not op.org_settings_displayed()

    def test_toggle_org_details(self,
                                bp: BasePage,
                                op: OrganismPage):
        """
        Tests toggling the Details panel within the Organism page on and off.
        
        :return: None.
        """
        bp.go_to_organism()
        op.open_org_details()
        assert op.org_details_displayed()
        op.close_org_details()
        assert not op.org_details_displayed()
        op.open_org_details()
        assert op.org_details_displayed()
