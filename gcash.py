import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import string
# generate random alphanumeric string of length 8
def random_string(length=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# create a list of user agents with unique alphanumeric string at the end
user_agents = [
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 {random_string()}",
    f"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 {random_string()}"
]
    # filter the list of user agents to remove any that contain the string "Googlebot"
filtered_user_agents = [user_agent for user_agent in user_agents if "Googlebot" not in user_agent]


# prompt the user to enter their mobile number
mobile_number = input("Enter your mobile number: ")
# initialize a new Chrome driver instance
# initialize a new Chrome driver instance
chrome_options = Options()
chrome_options.add_argument("--headless") # run Chrome in headless mode
chrome_options.add_argument(f"user-agent={random.choice(filtered_user_agents)}")
chrome_options.add_argument("--start-maximized")
# set the proxy information
driver = webdriver.Chrome(options=chrome_options)

# navigate to the webpage with the mobile input field
driver.get("https://m.gcash.com/gcashapp/gcash-promotion-web/2.0.0/index.html#/")
sleep(5)


# find the mobile input element by its class name
mobile_input = driver.find_element(By.CLASS_NAME, "mobile-input")

# enter the mobile number into the input field
mobile_input.send_keys(mobile_number)

# find the "Next" button element by its class name
next_button = driver.find_element(By.CLASS_NAME, "ap-button-primary")

# click the "Next" button
next_button.click()

# wait for the OTP input field to appear
otp_input = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.otp-password-field input[type="tel"]')))

# get the OTP from the user
otp = input("Enter your OTP: ")

# enter the OTP digit by digit
for i in range(len(otp)):
    otp_input.send_keys(otp[i])
    sleep(0)

# find the "Send" button element by its class name
send_button = driver.find_element(By.CLASS_NAME, "ap-button-primary")

# click the "Send" button
send_button.click()
sleep(5)
# check if the current page is the "account already exists" page
if "/exist" in driver.current_url:
    print("account already exists")
    sleep(10)
    driver.quit()
    exit()



# Fill up the personal information
first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="firstname"]')
first_name = random.choice(['Adriel','Aimee','Alden','Aleah','Althea','Andrei','Angel','Angela','Angelo','Anna','Anton','April','Arnel','Audrey','Bea','Benjie','Bianca','Carlo'])
first_name_input.send_keys(first_name)

middle_name_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="middlename"]')
middle_name = random.choice(['Abad','Abalos','Abante','Abaya','Abella','Abellera','Abenojar','Abesamis','Abing','Abion','Abis','Abiva','Abolencia','Abrigo','Abuan','Acasio','Acosta'])
middle_name_input.send_keys(middle_name)

last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="lastname"]')
last_name = random.choice(['Abad','Abalos','Abante','Abaya','Abella','Abellera','Abenojar','Abesamis','Abing','Abion','Abis','Abiva','Abolencia','Abrigo','Abuan','Acasio','Acosta'])
last_name_input.send_keys(last_name)

birthdate_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="bdate"]')
Birth_date = random.choice(['2002-09-12','1997-04-05','1989-08-23','1995-12-30','1987-02-10','2001-06-07','1990-10-22','1992-11-03','1988-07-14','1999-01-19','1994-05-08'])
birthdate_input.send_keys(Birth_date)

address_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="address"]')
Address = random.choice([
'123 Malagasang 1-G Imus',
'Block 6 Lot 8 Phase 1 Tanza',
'456 Molino Road Bacoor',
'789 Anabu 2-E Imus',
'Blk 2 Lot 4 Springville Heights Molino 4',
'101 Palmridge Subdivision Dasmariñas',
'456 Gen. Trias Drive Rosario',
'789 South Homes Subdivision Bacoor',
'Blk 3 Lot 12 Avida Residences Dasmariñas',
'111 Camella Homes Subdivision Imus',
'222 Metrogate Subdivision Bacoor',
'333 Woodestate Village Dasmariñas',
'444 Palmera Homes Imus',
'555 Malagasang 1-C Imus',
'666 Springville Meadows Molino 2',
'777 Palmridge Subdivision Dasmariñas',
'888 Villa San Lorenzo Bacoor',
'999 Orchard Golf and Country Club Dasmariñas',
'Blk 4 Lot 20 San Miguel Village Bacoor',
'123 New Molino Boulevard Bacoor',
'456 Adelina Homes Imus',
'789 Victoria Homes Dasmariñas',
'Blk 5 Lot 15 Lumina Homes Tanza',
'101 Montecillo Villas Dasmariñas',
'456 Suntrust Sentosa Dasmariñas',
'789 Parksville Residences Bacoor',
'Blk 6 Lot 9 The Orchard Golf and Country Club Dasmariñas',
'111 Camella Tierra Nevada Gen Trias',
'222 Bellefort Estates Molino 4',
'333 Kensington Villages '])
address_input.send_keys(Address)

email_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="email"]')
random_number = random.randint(100, 9999)
# concatenate the first name, last name, random number, and "@gmail.com"
email = f"{first_name}{last_name}{random_number}@gmail.com"
email_input.send_keys(email)
sleep(2)
# Find the "Submit" button element by its class name
submit_button = driver.find_element(By.CLASS_NAME, "ap-button-primary")

# Click the "Submit" button
submit_button.click()

# Wait for the page to load
sleep(1)

# Find the "Submit" button element by its class name
submit_button = driver.find_element(By.CLASS_NAME, "ap-button-primary")

# Click the "Submit" button
submit_button.click()

sleep(3)
mpin_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="mpin"]')
mpin_input.send_keys("1216")
mpin_input = driver.find_element(By.CSS_SELECTOR, 'input[accessbilityid="verify-mpin"]')
mpin_input.send_keys("1216")

# Find the submit button and click it

# Wait for the page to load
# Find the "Submit" button element by its class name
submit_button = driver.find_element(By.CLASS_NAME, "ap-button-primary")
# Click the "Submit" button
submit_button.click()
sleep(5)
# Quit the driver
driver.quit()

print("Success!")

