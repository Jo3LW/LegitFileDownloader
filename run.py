from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Change the path to the location of your chromedriver
chromedriver_path = "/path/to/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
# Change the URL to the URL of the GitHub repository which your target trusts
legitimate_github_repo_issue_url = "https://github.com/google-research/google-research/issues/new"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def generate_banner():
    banner = f"""
{Color.HEADER}               *******************************************************
               *                                                     *
               *{Color.BLUE}            Welcome to LegitFileDownloader !         {Color.HEADER}*
               *                                                     *
               *{Color.WARNING}    Warning: This tool is intended for educational   {Color.HEADER}*
               *{Color.WARNING}                    purposes only!                   {Color.HEADER}*
               *                                                     *
               *{Color.BLUE}   https://github.com/Jo3LW/LegitFileDownloader.git {Color.HEADER} *
               *                                                     *
               *******************************************************{Color.ENDC}
"""
    print(banner)



# Log in to GitHub
def login_to_github():
    username = ""
    password = ""

    try: 
        with open("login.txt", "r") as file:
            lines = file.readlines()

            if len(lines) != 2:
                username = input("Enter your GitHub username: ")
                password = input("Enter your GitHub password: ")

            username = lines[0].strip()
            password = lines[1].strip()


            if not username or not password:
                username = input("Enter your GitHub username: ")
                password = input("Enter your GitHub password: ")
                
    except FileNotFoundError:
        # If file dont exist, create one
        with open("login.txt", "w") as file:
            username = input("Enter your GitHub username: ")
            password = input("Enter your GitHub password: ")

            # Write the username and password to the file
            with open("login.txt", "w") as file:
                file.write(username + "\n")
                file.write(password + "\n")
    


    driver.get("https://github.com/login")

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.NAME, "commit")
    login_button.click()

    print("Logged in successfully!")

# Function to navigate to the desired webpage after login
def navigate_to_page(page_url):
    driver.get(page_url)

    # Find the form for uploading files
    form = driver.find_element(By.CSS_SELECTOR, 'file-attachment input[type="file"]')

    file_path = input("Enter the path of the file you want to upload: ")

    # Upload the file
    form.send_keys(file_path)

    print("File uploaded successfully!")



# Function to get the generated text
def get_generated_text():

    # Find the text box
    text_box = driver.find_element(By.CSS_SELECTOR, 'textarea#issue_body')

    time.sleep(5)

    # Retrieve the value attribute of the text box
    generated_text = text_box.get_attribute('value')

    start_index = generated_text.find("(") + 1
    end_index = generated_text.find(")")
    url = generated_text[start_index:end_index]

    return url


try:
    generate_banner()
    login_to_github()

    # Navigate to the desired webpage
    navigate_to_page(legitimate_github_repo_issue_url)

    # Get the generated text
    generated_text = get_generated_text()
    print("Generated text:", generated_text)

except Exception as e:
    print("An error occurred:", e)

driver.quit()
