import pytest

from base.base_page import BasePage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.organism.organism_page import OrganismPage
from specializations.population.population_page import PopulationPage

from tests.base_test import BaseTest


class TestPopulationStatsCalculation(BaseTest):
    """
    Test class that checks for incorrect calculation of statistics values.
    the Population page.
    """

    def test_check_calcs(self,
                         bp: BasePage,
                         pp: PopulationPage):
        """
        Tests calculation of avg fitness, offspring cost, and energy acq. rate (as well as # of viable orgs).

        :return: None.
        """
        bp.add_ancestor_to_dish()
        pp.run_from_pop()
        bp.util.sleep(10, "Waiting for experiment to run for a while.")
        pp.pause_from_pop()
        bp.util.sleep(10, "Waiting for pause.")
        calculated_values = pp.calculate_pop_averages()

        assert calculated_values[0] == pp.get_pop_current_viable()
        assert abs(calculated_values[1] - pp.get_pop_avg_fit()) < 0.2
        assert abs(calculated_values[2] - pp.get_pop_avg_offspring_cost()) < 0.2
        assert abs(calculated_values[3] - pp.get_pop_avg_energy_rate()) < 0.2
