from selenium import webdriver
import time


# Driver Section

driver = webdriver.Chrome()


# Password Section

username = 'Local vet'
password = 'Mykey2015'
twitchID = 'Localvet'
twitchPass = 'Mykey2015#'


driver.get('https://www.twitch.tv/login')
driver.find_element_by_xpath(
    "//input[@id='login-username']").send_keys(twitchID)
driver.find_element_by_xpath(
    "//input[@id='password-input']").send_keys(twitchPass)
driver.find_element_by_xpath("//button[@data-a-target]").click()
time.sleep(60)


driver.get('https://www.like4like.org/login/')


driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
driver.find_element_by_xpath("//a[@class='form-button']").click()

time.sleep(5)


driver.get('https://www.like4like.org/user/earn-twitch-followers.php')


def findx(driver, xpath):
    while True:
        try:
            dri = driver.find_element_by_xpath(xpath)
            return dri
        except:
            continue


numberOfTimes = 20

i = 0

while i < numberOfTimes + 1:
    if len(driver.window_handles) < 2:
        try:
            findx(driver, "//div[@class='height-20']").click()
        except:
            continue
    elif len(driver.window_handles) >= 2:
        while True:
            try:
                driver.switch_to.window(driver.window_handles[1])
                findx(
                    driver, "//button[@data-a-target='follow-button']").click()
                time.sleep(5)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                i += 1
                break
            except:
                continue
    else:
        continue
