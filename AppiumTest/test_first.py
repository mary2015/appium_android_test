from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import pytest
class TestForcast():

  @pytest.fixture()
  def test_setup(self):
    desired_cap ={
      "platformName": "Android",
      "deviceName": "MQS7N19603012111",
      "app": "/Users/rongyao.ma/newfolder/MyObservatory_v4.17.12_apkpure.com1.apk",
    }
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    driver.find_element_by_id("hko.MyObservatory_v1_0:id/btn_agree").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("hko.MyObservatory_v1_0:id/btn_agree").click()
    driver.find_element_by_id("com.android.permissioncontroller:id/permission_deny_button").click()
    driver.find_element_by_id("hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip").click()
    yield
    driver.close_app()
    driver.quit()

  def test_checkData(self,test_setup):
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]').click()
    driver.implicitly_wait(30)
    el1 = driver.find_element_by_id('hko.MyObservatory_v1_0:id/lower_layout')
    el2 = driver.find_element_by_id('hko.MyObservatory_v1_0:id/menu_icon')
    driver.scroll(el1,el2)
    # TouchAction(driver).press(x=700, y=1770).wait(800).move_to(x=700, y=1240).release().perform()
    driver.implicitly_wait(30)
    driver.find_element_by_id("hko.MyObservatory_v1_0:id/linearLayout").click()
    temperature = driver.find_element_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_temp").text
    precipitation = driver.find_element_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_rh").text
    wind = driver.find_element_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_wind").text
    tips = driver.find_element_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_details").text
    day_of_week = driver.find_element_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week").text
    assert temperature == "13 - 18°C"
    assert precipitation == "50 - 80%"
    assert wind == "North force 4 to 5, occasionally force 6 offshore."
    assert tips == "Sunny periods. Rather cool in the morning and at night. Dry during the day."
    assert day_of_week == "(Sat)"

  # def test_teardown(self):
  #   driver.close_app()
  #   driver.quit()