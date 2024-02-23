from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
name = [[],[],[],[],[]]
time = [[],[],[],[],[]]
for i in range(5):
    driver.get('https://www.fmkorea.com/index.php?mid=hotdeal&category=1254381811&page=' + str(i+1))
    name[i] = driver.find_elements(By.CLASS_NAME, "hotdeal_var8")
    time[i] = driver.find_elements(By.CLASS_NAME, "regdate")

for i in range(5):
    #for j in range(len(name[i])):
    #    print(name[i][j].text + "\n" + time[i][j].text)
    for j in name[i]:
        print(j.text)
    print("------------------------------")