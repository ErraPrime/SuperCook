from features.methods.main_methods import MainMethods
from features.methods.locators import Locators


class Ingredients(MainMethods):

    # Set the mobile driver and get the available locators
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators
    
    # Wait for intro to load
    def intro_load(self):
        self.wait_intro_load(self.locator.SKIP_INTRO_BTN)
    
    # Press skip intro
    def press_skip_intro(self):
        self.click_on_element(self.locator.SKIP_INTRO_BTN)
    
    # Ingredient addition section
    
    # Search for an ingredient in the search field, click on the field and wait for result box to load to avoid errors
    def search_for(self):
        self.click_on_element(self.locator.SEARCH_INPUT)
        self.input(self.locator.SEARCH_INPUT, "milk")
        self.find_element(self.locator.FIND_RESULTS_BOX)
    
    # Select ingredient checkbox
    def select_ingredient(self):
        self.click_on_element(self.locator.SELECT_INGREDIENT_CB)
    
    # Select all ingredients required for a recipe
    def select_all_ingredients(self):
        self.click_on_element(self.locator.INGREDIENT_BUTTER_BTN)
        self.click_on_element(self.locator.INGREDIENT_MILK_BTN)

    # Tap on the first result displayed by the result box, by coordonates
    def open_first_result(self):
        self.tap_coordonates(self.locator.FIRST_RESULT_COORDONATES)
        
    # Ingredient removal section
    
    # Press on more options on the main page 
    def press_more_options(self):
        self.click_on_element(self.locator.MORE_OPTIONS_BTN)
    
    # Press on remove all ingredients button on main page
    def press_remove_ingredients(self):
        self.tap_coordonates(self.locator.REMOVE_ALL_INGREDIENTS)
    
    # Press on confirm to remove all ingredients
    def press_confirm_remove(self):
        self.click_on_element(self.locator.CONFIRM_REMOVE_BTN)

    # Close the app
    def closeapp(self):
        self.driver.close_app()
    


