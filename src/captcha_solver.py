import time
import os
import base64
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import re

# Constants
CAPTCHA_DIR = "runtime_captchas"
GECKODRIVER_PATH = '/usr/local/bin/geckodriver'

def setup_driver():
    """Set up the Firefox WebDriver."""
    service = Service(executable_path=GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service)
    return driver

def create_captcha_directory():
    """Create a directory for storing CAPTCHA images if it doesn't exist."""
    if not os.path.exists(CAPTCHA_DIR):
        os.makedirs(CAPTCHA_DIR)

def get_last_image_number():
    """Retrieve the last saved image number to continue from there."""
    existing_images = [f for f in os.listdir(CAPTCHA_DIR) if f.endswith('.png') and bool(re.search(r'\d',f))]
    if existing_images:
        last_image = max(existing_images, key=lambda x: int(x.split('_')[-1].split('.')[0]))
        return int(last_image.split('_')[-1].split('.')[0])
    return 0

def save_captcha_image(captcha_image_data, image_number):
    """Save the decoded CAPTCHA image to a file."""
    with open(f"{CAPTCHA_DIR}/captcha_image_{image_number}.png", "wb") as file:
        file.write(captcha_image_data)
    print(f"Captcha image {image_number} saved locally as 'captcha_image_{image_number}.png'.")

def click_redirect_button(driver):
    """Click the button to redirect to the CAPTCHA page."""
    redirect_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.fw-bold")
    redirect_button.click()

def refresh_until_captcha_found(driver, images_retrieved):
    """Refresh the page until the CAPTCHA image is found or timeout."""
    start_time = time.time()
    while True:
        if time.time() - start_time > 100:
            print("Timeout: CAPTCHA image not found within 100 seconds.")
            return False
        try:
            # Wait for a while to ensure the CAPTCHA image is loaded
            time.sleep(2)
            # Try to find the CAPTCHA image
            captcha_element = driver.find_element(By.CSS_SELECTOR, "img.form-control.img-fluid.bg-light.border-0")
            return captcha_element
        except NoSuchElementException:
            print("Captcha image not found, refreshing...")
            driver.refresh()
            time.sleep(3)  # Wait for the page to load again

def extract_and_save_captcha(driver, images_retrieved):
    """Extract the CAPTCHA image and save it locally."""
    captcha_element = driver.find_element(By.CSS_SELECTOR, "img.form-control.img-fluid.bg-light.border-0")
    captcha_base64 = captcha_element.get_attribute("src").split(',')[1]  # Get Base64 part
    captcha_image_data = base64.b64decode(captcha_base64)
    save_captcha_image(captcha_image_data, images_retrieved + 1)

def get_captcha_value():
    # Solves the captcha and returns the value from the model
    return "temp_captcha"

def solve_captcha():
        #enter captcha enter username and password. 
        # Check IF page crossed -> multiple approaches to check
            #If page bypassed return 1 else return 0

        # Username
        driver.find_element(By.ID, "username").send_keys("23BCY10065")
        #Pass
        driver.find_element(By.ID, "password").send_keys("PASS")
        # Captcha
        captcha_value = get_captcha_value()
        driver.find_element(By.ID, "captchaStr").send_keys(get_captcha_value(), Keys.ENTER)
        time.sleep(2)
        try:
            driver.find_element(By.ID, "sidePanel")
            return 1
        except:
            driver.find_element(By.CSS_SELECTOR, "span.text-danger.text-center")
        

        # captcha failed -> .text-danger text-center
        # 
        # #sidePanel




if __name__ == "__main__":
    """Main function to run the CAPTCHA extraction process."""
    
    driver = setup_driver()
    driver.get("https://vtop.vitbhopal.ac.in/vtop/login")
    time.sleep(2)  # Wait for the page to load

    create_captcha_directory()
    images_retrieved = get_last_image_number()  # Start from the last saved image number
    # print(f"images retrieved : {images_retrieved}")
    # Click the redirect button to VTOP Login page
    click_redirect_button(driver)
    time.sleep(3)

    
    start=time.time()
    while True:
        if refresh_until_captcha_found(driver, images_retrieved):
            extract_and_save_captcha(driver, images_retrieved)
            images_retrieved += 1  # Increment the count of images retrieved
        #Solve the captcha and login
        if solve_captcha():
            print("Captcha Bypassed")
            break
        if (time.time() - start)>50:
            print("captcha tries timed out")
            break
        

    # Close the browser
    driver.quit()

