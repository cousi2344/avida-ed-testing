import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestBasicNavigation(BaseTest):
    """
    Test class that tests navigation between the major specializations
    within the Avida-ED website.
    
    Note that "specializations" are logical rather than real, URL-level separations
    within the site. They are divided into the major parts of the website --
    Population, Organism, and Analysis -- because a user will always be within
    one of those three parts of the site.
    """

    def test_go_to_population(self,
                              bp: BasePage):
        """
        Tests navigating to the Population page.
        
        Should not be run first, because the site loads this page as the
        default.
        
        :return: None. 
        """
        bp.go_to_population()
        assert bp.population_displayed()
        bp.util.sleep(3)

    def test_go_to_organism(self,
                            bp: BasePage):
        """
        Tests navigating to the Organism page.
        
        :return: None.
        """
        bp.go_to_organism()
        assert bp.organism_displayed()
        bp.util.sleep(3)

    def test_go_to_analysis(self,
                            bp: BasePage):
        """
        Tests navigating to the Analysis page.
        
        :return: None. 
        """
        bp.go_to_analysis()
        assert bp.analysis_displayed()
        bp.util.sleep(3)
