from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from gologin import GoLogin
from random_ten import r1andom_ten
import time
import asyncio
import pyppeteer
from gologin import get_random_port


def loi_khong_mo_dc(tk=None , mk=None ,khoiphuc=None , cookie = None , tentep=None ):
    if tk != None :
        f = open(tentep, mode="a+")
        f.write(tk + " " + mk + " " + khoiphuc + " " + cookie + "\n")
        f.close()


def tao_profile(du_lieu_tk):

    dia_chi = du_lieu_tk[3]
    tokens = du_lieu_tk[4]
    dia_chi_chua_profile = du_lieu_tk[5]
    gl = GoLogin({
        "token": tokens,
        "local": False,
        "credentials_enable_service": False,


    })
    ten = r1andom_ten()

    profile_id=gl.create({
        "name": ten,
        "os": 'win',
        "tmpdir": dia_chi_chua_profile,
        "navigator": {
            "language": 'en-US',
            #"userAgent": 'Mozilla/5.0 (Linux; Android 11; LM-G820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',  # Your userAgent (if you don't want to change, leave it at 'random')
            #"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
            #"userAgent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36",
            "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            "resolution": '412x892',  # Your resolution (if you want a random resolution - set it to 'random')
            "platform": 'Win32',
        },
        # 'profile': r'C:\Users\duc13\OneDrive\Desktop\gologin ',
        'proxyEnabled': True,  # Specify 'false' if not using proxy
        'proxy': {
            'mode': 'tor',
            'autoProxyRegion': dia_chi
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
    return profile_id



async def chaygoc(du_lieu_tk ):
    random_port = get_random_port()
    tk = du_lieu_tk[0]
    mk = du_lieu_tk[1]
    kp=du_lieu_tk[2]
    tokens = du_lieu_tk[4]
    dia_chi_chua_profile =du_lieu_tk[5]
    id = tao_profile(du_lieu_tk)
    gl = GoLogin({
      "token": tokens,
      "profile_id": id,
      "tmpdir": dia_chi_chua_profile,
      "port": random_port
    })

    debugger_address = gl.start()
    browser = await pyppeteer.connect(browserURL="http://" + debugger_address)
    page = await browser.newPage()
    await gl.normalizePageView(page)
    await page.goto('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1')
    await page.click("[name='identifier']")
    await page.type("[name='identifier']",tk , options={"delay":2})
    #await page.$x("//button[contains(., 'Button text')]")
    #xac_nhan_xuat_hien123 = await page.waitForSelector("[id='selectionc0']", {"timeout": 30000})
    #print("day la xuat hien 123 :" , xac_nhan_xuat_hien123)
    click_nut_next = await page.xpath('//button[@type="button" and contains(., "Next")]')
    time.sleep(3)
    await click_nut_next[0].click()
    try :
        xac_nhan_xuat_hien = await page.waitForSelector("[id='selectionc0']", { "timeout":15000})
        time.sleep(5)
        await page.click("[name='password']")
        await page.type("[name='password']", mk)
        click_nut_next = await page.xpath('//button[@type="button" and contains(., "Next")]')
        await click_nut_next[0].click()
        await page.waitForSelector("[id='searchAccountPhoneSearchBar']", {"timeout": 15000})
        time.sleep(5)
        await browser.close()
        gl.stop()
        gl.delete(id)
    except:
        loi_khong_mo_dc(tk,mk,"khong_co_tai_khoan_hoac_sai_mk.txt")
        await browser.close()
        gl.stop()
        gl.delete(id)

def chay_tien_trinh( du_lieu_tk ) :
    asyncio.get_event_loop().run_until_complete(chaygoc(du_lieu_tk))


du_lieu_tk=["duc131219972@gmail.com" ,"01262688165", "khoiphuc","us","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmZkYjdlZmQzNTdkZDllOWI4NDMwOTEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzAzMzUwYWIxNDQzN2Y4NDk1YjcyNWEifQ.BhwdRYroZRyd02PBN71hlZuGzgStegL5cuVAgqd3EJY", "E:\\mu\\toolgmailusa\\profile"]
chay_tien_trinh(du_lieu_tk)






"""

id="searchAccountPhoneSearchBar"
gls = GoLogin({
        "token": tokens,
        "profile_id": profile_id,
        #"profile_id": "gologin_62fdf136c1e4886f5de1a3da",
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
    driver.implicitly_wait(10)
    #driver.set_window_rect(1,1,400,600)
    # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1")
    #duc= driver.find_elements(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div/text()")
    dem_so_lan_nhan_try = 0
    while dem_so_lan_nhan_try < 3 :

        driver.find_element(By.ID, "identifierId").click()
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
            driver.find_elements(By.ID, "password").click()
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
    driver.close()
"""









