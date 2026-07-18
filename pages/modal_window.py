from pages.base_page import BasePage
from locators.modal_window_locators import ModalWindowLocators

class ModalWindow(BasePage):
    def close_modal(self):
        self.click(ModalWindowLocators.CLOSE_BUTTON)
        self.wait_for_invisibility(ModalWindowLocators.CLOSE_BUTTON)

    def get_modal_title(self) -> str:
        return self.get_text(ModalWindowLocators.MODAL_TITLE)

    def is_modal_displayed(self) -> bool:
        return self.find_element(ModalWindowLocators.MODAL_TITLE).is_displayed()
