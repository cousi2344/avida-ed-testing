import unittest
import pytest


@pytest.mark.usefixtures("bp_setup")
class AvidaEdTabTest(unittest.TestCase):
    """
    Test class that tests the Avida-ED tab of the main menu bar.
    """

    @pytest.mark.run()
    def test_about_page(self):
        """
        Tests that the about page works properly.

        :return: None.
        """
        self.bp.open_avida_ed_about()
        assert self.bp.avida_ed_about_displayed()
        self.bp.close_avida_ed_about()
        assert not self.bp.avida_ed_about_displayed()

