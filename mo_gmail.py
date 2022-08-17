#test

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from toolgmailusa.chaygologinomay import debugger_address


def loi_khong_mo_dc(d,tk=None,mk=None,tentep=None):
    if tk != None :
        f = open(tentep, mode="a+")
        f.write(tk + " " + mk + "\n")
        f.close()


def mo_acc(mk,tk):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    # driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    #driver.set_window_rect(1,1,400,600)
    # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("https://voice.google.com/u/0/signup")
    #duc= driver.find_elements(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div/text()")
    dem_so_lan_nhan_try = 0
    while dem_so_lan_nhan_try < 3 :
        driver.find_element(By.ID, "identifierId").send_keys(tk + Keys.ENTER)
        if len(driver.find_elements(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div/text()")) > 0 or len(driver.find_elements(By.XPATH,"//*[text()='Couldn’t find your Google Account']")) > 0 :
            loi_khong_mo_dc("ducwefnuwejnf@","day la mk ","loi_tra_lai.txt")
            gls.stop()
            break
        if len(driver.find_elements(By.XPATH,
                                    "//*[@id='next']/div/button/span")) > 0 or len(
                driver.find_elements(By.XPATH, "//*[text()='Try again']")) > 0:
            driver.find_element(By.XPATH,
                                 "//*[@id='next']/div/button/span").click()
            dem_so_lan_nhan_try+= 1
            continue


        if len(driver.find_elements(By.ID, "password"))>  0:
            driver.find_elements(By.ID, "password").send_keys(mk+ Keys.ENTER)
            if len(driver.find_elements(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span")) > 0 or len(driver.find_elements(By.XPATH,"//*[text()='Wrong password. Try again or click Forgot password to reset it.']")) > 0 :
                loi_khong_mo_dc("ducwefnuwejnf@", "day la mk ", "loi_tra_lai.txt")

                gls.stop()
                break

        #cho nay se kiem tra co vao duoc tk chua va hoan thanh
        if len(driver.find_elements(By.ID, "ib1")) > 0:
            loi_khong_mo_dc("ducwefnuwejnf@", "day la mk ", "mo_thanh_cong.txt")
            gls.stop()
            break