from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium_stealth import stealth
_driver = None

def getDriver(headless=True):
    global _driver
    if _driver is None:
        chrome_options = Options()
        # chrome_options.add_argument(f"--user-data-dir=C:/Users/rosha/AppData/Local/Google/Chrome/User Data")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")
        # chrome_options.add_argument("profile-directory=Default")
        
        if headless:
            chrome_options.add_argument("start-maximized")
            chrome_options.add_argument("--headless")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
        try:
            # Using webdriver_manager to automatically handle driver downloads and updates
            _driver = webdriver.Chrome(options=chrome_options)
            # Stealth mode to avoid detection
            stealth(_driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

            print("WebDriver initialized.")
        except Exception as e:
            print(f"Error initializing WebDriver: {e}")
            _driver = None # Ensure driver is None if initialization fails
            raise # Re-raise the exception to signal failure to the caller
    return _driver

def closeDriver():
    global _driver
    if _driver is not None:
        try:
            _driver.quit()
            print("WebDriver closed.")
        except Exception as e:
            print(f"Error closing WebDriver: {e}")
        finally:
            _driver = None

if __name__ == "__main__":
    try:
        # Get the driver (it will be initialized here)
        driver1 = getDriver(headless=True)
        if driver1:
            driver1.get("http://selenium.dev")
            print(f"Page title (driver1): {driver1.title}")

        # Get the driver again (it should return the same instance)
        driver2 = getDriver()
        if driver2:
            # To prove it's the same instance, navigate to a different page
            # If it were a new instance, it would open a new browser or error
            driver2.get("https://www.google.com")
            print(f"Page title (driver2): {driver2.title}")

        print(f"Are driver1 and driver2 the same object? {driver1 is driver2}")

        driver1.get("https://hindupost.in/defence/9-terror-factories-in-pak-pojk-destroyed/")
        driver1.save_screenshot("hindupost.png")
    except Exception as e:
        print(f"An error occurred during example usage: {e}")
    finally:
        # Close the driver when done
        closeDriver()