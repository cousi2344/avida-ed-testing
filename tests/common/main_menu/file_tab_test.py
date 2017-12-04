import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestFileTab(BaseTest):
    """
    Test class that tests the File tab of the main menu bar.
    """
    def test_export_graphics(self,
                             bp: BasePage):
        """
        Tests that the "Export Graphics" option in the File tab works as
        expected.

        :return: None.
        """
        assert not bp.export_graphics_dialog_displayed()
        bp.export_graphics()
        assert bp.export_graphics_dialog_displayed()
        bp.close_export_graphics_dialog()
        assert not bp.export_graphics_dialog_displayed()

