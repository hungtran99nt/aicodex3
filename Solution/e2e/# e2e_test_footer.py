# e2e_test_footer.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class FooterUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://vnexpress.net/")

    def test_footer_ui(self):
        driver = self.driver
        footer = driver.find_element(By.TAG_NAME, "footer")
        
        # Check if footer is displayed
        self.assertTrue(footer.is_displayed(), "Footer is not displayed")

        # Check for specific elements in the footer
        links = footer.find_elements(By.TAG_NAME, "a")
        self.assertGreater(len(links), 0, "No links found in the footer")

        # Example: Check if a specific link text is present
        expected_link_text = "Liên hệ"
        link_texts = [link.text for link in links]
        self.assertIn(expected_link_text, link_texts, f"'{expected_link_text}' link not found in the footer")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()