import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):
    def test_website_loading(self):
        url = "https://atg.world"
        print("Connecting to", url)
        response = requests.get(url)
        if response.status_code == 200:
            print("Website loaded successfully!")
            self.assertTrue(True)
        else:
            print("Failed to load website. Status code:", response.status_code)
            self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
