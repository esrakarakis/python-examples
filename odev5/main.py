from selenium.webdriver.common.by import By


class Homework:
    NEWSLETTER_UTM_SETTINGS = (By.ID, "enableUTMSettings_")
    INPUT_WARNING_MESSAGE = (By.CLASS_NAME, "in-text-input-wrapper__error-message")
    JOURNEY_DO_LIST_FILTER_INPUT = (By.ID, "search-value")
    TEST_BUTTON_RADIO = (By.ID, "Test")
    JOURNEY_STATISTICS = (By.CSS_SELECTOR, 'tr[item-index="0"] td.vuetable-slot.statistics')
    MESSAGE_BOX = (By.ID, "delete")
    JOURNEY = (By.LINK_TEXT, "SMS")
    ALERT_TOASTER = (By.CLASS_NAME, "messageAlertBoxHidden")
    SOCIAL_PROOF_CREATE = (By.ID, "create-mobile-campaign")
