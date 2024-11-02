from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# fullname = driver.find_element(By.ID, "fullname")
# phone = driver.find_element(By.ID, "phone")
# dropdown = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/section/form/section[1]/main/div[3]")
# fullname.send_keys("Ferhat Adi belli")
# phone.send_keys("05554443445")
#
# dropdown.click()
#
# option = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/section/form/section[1]/main/div[3]/div[2]/div[2]/ul/li[2]")
# option.click()
#
# button = driver.find_element(By.ID, "get-offer-main-page")
# button.click()
#
# driver.quit()


## PYTHON.ORG SCRAPING WEBSITE
custom_dic = {}
for item in range(1, 6):
    each_one = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{item}]')
    time = each_one.find_element(By.TAG_NAME, "time").text
    name = each_one.find_element(By.TAG_NAME, "a").text
    custom_dic[item - 1] = {"time": time, "name": name}

print(custom_dic)
# print(list)
print("This is coming from dev...s")