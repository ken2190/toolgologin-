
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





def loi_khong_mo_dc(d,tk=None,mk=None,tentep=None):
    if tk != None :
        f = open(tentep, mode="a+")
        f.write(tk + " " + mk + "\n")
        f.close()




tk="duc13121997@gmail.com"
mk="01qretgregqqwqf8165"
def tao_profile(tk,mk):
    tokens = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmVjZDg4OWJkOGMyN2NjOTdiMDYyMTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmVjZGRmMDVhNTM5ODgyOGJjODNlMDUifQ.I7WsbC6jlyOPwxlmUTgEY2oFRgX6EhvllddyNxjjHgg"
    gl = GoLogin({
        "token": tokens,
        # "profile_id": "62eb86813528007c2cdc2f5f",
        "local": False,
        "credentials_enable_service": False,

    })

    profile_id = gl.create({
        "name": 'testchuate',
        "os": 'win',
        "navigator": {
            "language": 'en-US',
            #"userAgent": 'Mozilla/5.0 (Linux; Android 11; LM-G820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',  # Your userAgent (if you don't want to change, leave it at 'random')
            "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
            "resolution": '412x892',  # Your resolution (if you want a random resolution - set it to 'random')
            "platform": 'Win32',
        },
        # 'profile': r'C:\Users\duc13\OneDrive\Desktop\gologin ',
        'proxyEnabled': True,  # Specify 'false' if not using proxy
        'proxy': {
            'mode': 'gologin',
            'autoProxyRegion': 'us'
            # "host": '',
            # "port": '',
            # "username": '',
            # "password": '',
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },

    })

    print('profile id=', profile_id)

    # gl.setProfileId(profile_id)
    # gl.createStartup()


    gls = GoLogin({
        "token": tokens,
        "profile_id": profile_id,
        #"profile_id": "62ebbd94a8d2004d6fb57e6f",
        # "port": random_port
        "tmpdir": "E:\\mu\\toolgmailusa\\profile"
    })

    if platform == "linux" or platform == "linux2":
        chrome_driver_path = "./chromedriver"
    elif platform == "darwin":
        chrome_driver_path = "./mac/chromedriver"
    elif platform == "win32":
        chrome_driver_path = "chromedriver.exe"


    debugger_address = gls.start()
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

tao_profile(tk,mk)
