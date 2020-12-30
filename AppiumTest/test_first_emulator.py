from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import pytest
class TestForcast():

  @pytest.fixture()
  def test_setup(self):
    desired_cap ={
         "deviceName": "Android Emulator",
         "platformName": "Android",
         "app": "/Users/rongyao.ma/testfolder/MyObservatory_v4.17.12_apkpure.com.apk"
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
    el2 = driver.find_elements_by_id('hko.MyObservatory_v1_0:id/linearLayout')[4]  # "hko.MyObservatory_v1_0:id/menu_icon"
    print(el2)
    driver.scroll(el1, el2)
    TouchAction(driver).press(x=700, y=1770).wait(800).move_to(x=700, y=1240).release().perform()
    driver.implicitly_wait(30)
    driver.find_elements_by_id("hko.MyObservatory_v1_0:id/linearLayout")[5].click()

    temperature = driver.find_elements_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_temp")[0].text
    precipitation = driver.find_elements_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_rh")[0].text
    wind = driver.find_elements_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_wind")[0].text
    tips = driver.find_elements_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_details")[0].text
    day_of_week = driver.find_elements_by_id("hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week")[0].text
    assert temperature == "17 - 22°C"
    assert precipitation == "65 - 90%"
    assert wind == "East force 3 to 4, force 5 offshore later."
    assert tips == "Mainly fine. Visibility relatively low in some areas at first."
    assert day_of_week == "(Mon)"

  # def test_teardown(self):
  #   driver.close_app()
  #   driver.quit()
