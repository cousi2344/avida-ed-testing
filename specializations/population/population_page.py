import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class PopulationPage(BasePage):
    """
    Specialization of the BasePage that is specialized to the Population page
    on the Avida-ED website.
    """

    # Logger
    log = create_custom_logger(logging.DEBUG)

    # Locators for population setup pane.
    __setup_button_id = "popSetupButton"
    __setup_dish = "Dish"
    __setup_setup = "Setup"
    __setup_block_id = "setupBlock"
    __mut_rate_input = "muteInput"

    # Locators for population statistics window.
    __stats_window = "popRight"
    __stats_button = "popStatsButton"
    __dish_cols_box = "sizeCols"
    __dish_rows_box = "sizeRows"


    # Locators for updates and other UI information.
    __update_text = "TimeLabel"

    # Locators for buttons underneath dish.
    __run_pause_pop_button = "runStopButton"
    __run_text = "Run"
    __pause_text = "Pause"
    __new_dish_button = "newDishButton"
    __forward_button = "oneUpdateButton"

    # Locators for new dish dialog box.
    __new_dish_dlg = "dijit_Dialog_4"
    __new_dish_cancel_xpath = "//*/span[@widgetid='newCancel']"
    __new_dish_discard_xpath = "//*/span[@widgetid='newDiscard']"
    __new_dish_saveconf_xpath = "//*/span[@widgetid='newSaveConfig']"
    __new_dish_savepop_xpath = "//*/span[@widgetid='newSaveWorld']"

    def __init__(self, driver):
        """
        Sets up the page for use at initialization.

        :param driver: The driver that interacts with the actual page.
        """
        super().__init__(driver)
        self.driver = driver
        self.go_to_population()

    def env_settings_displayed(self):
        """
        Determines whether the "Environmental Settings" panel within the
        "Population" page is displayed.
        
        :return: True if the "Environmental Settings" panel is displayed, false
        otherwise.
        """

        setup_button_text = self.get_text(self.__setup_button_id)
        displayed = (self.__element_displayed(self.__setup_block_id) and
                     self.util.verify_text_matches(setup_button_text,
                                                   self.__setup_dish))
        self.log.info("Is Environmental Settings displayed? " + str(displayed))
        return displayed

    def grid_displayed(self):
        """
        Determines whether the main Petri dish grid on the "Population" page
        is displayed.
        
        This is essentially the opposite of the env_settings_displayed method. 
        This method could be a reversal of env_settings_displayed, but doing
        that would reduce performance because we would have to account for the
        fact that if the population window is not displayed, both functions will
        return false.
        
        :return: True if the Petri dish is displayed, false otherwise.
        """
        setup_button_text = self.get_text(self.__setup_button_id)
        displayed = (not self.__element_displayed(self.__setup_block_id) and
                     self.util.verify_text_matches(setup_button_text,
                                                   self.__setup_setup))
        self.log.info("Is grid displayed? " + str(displayed))
        return displayed

    def show_env_settings(self):
        """
        Navigates to the "Environmental Settings" panel within the "Population"
        page on the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if not self.env_settings_displayed():
            self.__click_element(self.__setup_button_id)
            self.log.info("Show environmental settings window.")

    def hide_env_settings(self):
        """
        Hides the "Environmental Settings" panel within the "Population" page on
        the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if self.env_settings_displayed():
            self.__click_element(self.__setup_button_id)
            self.log.info("Hid environmental settings window.")

    def pop_stats_displayed(self):
        """
        Checks if the stats panel within the "Population" pane of the Avida-ED
        website.

        :return: True if the stats panel is visible, false otherwise.
        """
        pop_stats_displayed = self.__element_displayed(self.__stats_window)
        self.log.info("Is population statistics displayed? "
                      + str(pop_stats_displayed))
        return pop_stats_displayed

    def show_pop_stats(self):
        """
        Shows the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if not self.__element_displayed(self.__stats_window):
            self.__click_element(self.__stats_button)
            self.log.info("Show population statistics window.")

    def hide_pop_stats(self):
        """
        Hides the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if self.__element_displayed(self.__stats_window):
            self.__click_element(self.__stats_button)
            self.log.info("Hid population statistics window.")

    def __click_runpause_pop_button(self):
        """
        Clicks on the main 'Run'/'Pause' button underneath the dish to start
        the experiment.

        :return: None.
        """
        self.__click_element(self.__run_pause_pop_button)

    def runpause_text_is_run(self):
        """
        Checks whether the text of the 'Run'/'Pause' button underneath the dish
        currently says 'Run'.

        :return: True if button text is 'Run', false if it is not (in which case
        it must be 'Pause").
        """
        btn_text = self.get_text(self.__run_pause_pop_button)
        is_run = self.util.verify_text_matches(btn_text, self.__run_text)
        self.log.info("Is Run/Pause button text 'Run'? " + str(is_run))
        return is_run

    def run_from_pop(self):
        """
        Runs the experiment via the button underneath the dish.

        :return: None.
        """
        if self.runpause_text_is_run():
            self.__click_runpause_pop_button()
            self.log.info("Started running experiment via button under dish.")

    def pause_from_pop(self):
        """
        Pauses the experiment via the button underneath the dish.
        :return:
        """
        if not self.runpause_text_is_run():
            self.__click_runpause_pop_button()
            self.log.info("Paused experiment via button under dish.")

    def new_exp_dlg_displayed(self):
        """
        Determines if the dialog that is supposed to appear after clicking on
        the 'New' button under the dish is currently displayed on-screen.

        :return: True if dialog is displayed, False otherwise.
        """
        displayed = self.__element_displayed(self.__new_dish_dlg)
        self.log.info("Is new experiment dialog displayed? " + str(displayed))
        return displayed

    def click_new_exp(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment.
        This method does not have any way of handling the dialog that may appear
        afterwards. Typically this would be a private method, but it is not
        because this method may be useful for testing purposes.

        :return: None.
        """
        self.__click_element(self.__new_dish_button)
        self.log.info("Clicked on New button without plan for dialog.")

    def new_exp_cancel(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will cancel the operation once the dialog box comes up.

        :return: None.
        """
        self.click_new_exp()
        self.log.info("Clicked on New button.")
        if self.new_exp_dlg_displayed():
            self.__click_element(self.__new_dish_cancel_xpath, "xpath")
            self.log.info("Cancelled New via dialog box.")

    def new_exp_discard(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will discard the contents of the dish.

        :return: None.
        """
        self.click_new_exp()
        self.log.info("Clicked on New button.")
        if self.new_exp_dlg_displayed():
            self.__click_element(self.__new_dish_discard_xpath, "xpath")
            self.log.info("Carried through with New, discarded old dish.")

    def new_exp_saveconf(self, name=None):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will save the dish configuration to the freezer.

        :param name: The name that the experiment configuration should be saved
        as.

        :return: None.
        """
        self.click_new_exp()
        self.log.info("Clicked on New button.")
        if self.new_exp_dlg_displayed():
            self.__click_element(self.__new_dish_saveconf_xpath, "xpath")
            name_popup = self.__switch_to_alert()
            if name is not None:
                name_popup.send_keys(name)
                self.log.info("Carried through with New, saved dish conf. as "
                              + name + ".")
            else:
                self.log.info("Carried through with New, saved dish conf. with"
                              " default name.")
            name_popup.accept()

    def new_exp_savepop(self, name=None):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will save the populated dish to the freezer.

        :param name: The name that the populated dish should be saved as.

        :return: None.
        """
        self.click_new_exp()
        self.log.info("Clicked on New button.")
        if self.new_exp_dlg_displayed():
            self.__click_element(self.__new_dish_savepop_xpath, "xpath")
            name_popup = self.__switch_to_alert()
            if name is not None:
                name_popup.send_keys(name)
                self.log.info("Carried through with New, saved populated dish"
                              "as " + name + ".")
            else:
                self.log.info("Carried through with New, saved populated dish"
                              " with default name.")
            name_popup.accept()

    def forward_from_pop(self):
        """
        Moves the experiment forward by one update by clicking on the 'Forward'
        button
        :return:
        """
        self.__click_element(self.__forward_button)
        self.log.info("Moved forward one update via 'Forward' button under dish"
                      ".")

    def get_update_ui_text(self):
        """
        Gets the text from the UI element containing information about the
        simulation update/time.

        :return: String containing update information.
        """
        update_text = self.get_text(self.__update_text)
        self.log.info("Got update number from ui: text is " + update_text)
        return update_text

    def edit_dish_cols(self, cols_num):
        """
        Edits the dish column number in the environmental settings panel.

        :param cols_num: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        cols_box = self.__get_element(self.__dish_cols_box)
        cols_box.clear()
        self.send_keys(element=cols_box, keys=cols_num)
        self.hide_env_settings()
        self.log.info("Edited dish column number to " + str(cols_num))

    def edit_dish_rows(self, rows_num):
        """
        Edits the dish row number in the environmental settings panel.

        :param rows_num: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        rows_box = self.__get_element(self.__dish_rows_box)
        rows_box.clear()
        self.send_keys(element=rows_box, keys=rows_num)
        self.hide_env_settings()
        self.log.info("Edited dish row number to " + str(rows_num))

    def edit_mut_rate(self, rate):
        """
        Edits the dish mutation rate in the environmental settings panel.

        :param rate: The input to be sent to the mutation rate box.

        :return: None.
        """
        self.show_env_settings()
        mut_rate_box = self.__get_element(self.__mut_rate_input)
        mut_rate_box.clear()
        self.send_keys(element=mut_rate_box, keys=str(rate))
        self.hide_env_settings()
        self.log.info("Edited population mutation rate to " + str(rate))