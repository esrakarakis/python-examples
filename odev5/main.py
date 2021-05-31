from selenium.webdriver.common.by import By


class Homework:
    NEWSLETTER_UTM_SETTINGS = (By.ID, "enableUTMSettings_")
    INPUT_WARNING_MESSAGE = (By.CSS_SELECTOR, "in-text-input-wrapper__error-message")
    JOURNEY_DO_LIST_FILTER_INPUT = (By.ID, "search-value")
    TEST_BUTTON_RADIO = (By.CSS_SELECTOR, "in-radio-button-wrapper__label")  # 5
    JOURNEY_STATISTICS = (By.CSS_SELECTOR, "statistics")  # 0
    MESSAGE_BOX = (By.ID, "delete")
    JOURNEY_REMOVE_CHANGE = (By.CSS_SELECTOR, "py-2")
    ALERT_TOASTER = (By.CSS_SELECTOR, "messageAlertBoxHidden")
    SOCIAL_PROOF_CREATE = (By.ID, "create-mobile-campaign")
