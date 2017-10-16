import pytest

from tests.base_test import BaseTest


class PopulationStatsCalculationCheck(BaseTest):
    """
    Test class that checks for incorrect calculation of statistics values.
    the Population page.
    """

    @pytest.mark.run()
    def test_check_calcs(self):
        """
        Tests calculation of avg fitness, offspring cost, and energy acq. rate (as well as # of viable orgs).

        :return: None.
        """
        self.bp.add_ancestor_to_dish()
        self.pp.run_from_pop()
        self.bp.util.sleep(10, "Waiting for experiment to run for a while.")
        self.pp.pause_from_pop()
        self.bp.util.sleep(10, "Waiting for pause.")
        calculated_values = self.pp.calculate_pop_averages()

        assert calculated_values[0] == self.pp.get_pop_current_viable()
        assert abs(calculated_values[1] - self.pp.get_pop_avg_fit()) < 0.2
        assert abs(calculated_values[2] - self.pp.get_pop_avg_offspring_cost()) < 0.2
        assert abs(calculated_values[3] - self.pp.get_pop_avg_energy_rate()) < 0.2
