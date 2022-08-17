
import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin


gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmU5ZTU0MWRhN2Y3OGVjNTFhMzc0MjgiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmVhODNiNjAzNTQ2ZjFmYmViMWY3ZGYifQ.rL9AWo7jvHChxi6UIVdL5B1_capLaBYjULCEtJGzaoc",
	"profile_id": "62ea300329f5d43830802fb4",
	"local": True,
	"credentials_enable_service": False,
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()