Task 1:
Automate below test case:
Check tomorrow weather forecast from 9-day forecast screen

1. Script : test_first.py
2. Setup guide :
  1). download appium  http://appium.io/  Appium-mac-1.18.3.dmg
  2). download android studio  https://developer.android.com/studio android-studio-ide-201.6953283-mac.dmg
  3). pip3 install Appium-Python-Client (or import it by pyCharm  file |other settings | Preferences for new project | Project Interpreter)
  4). pip3 install pytest (or import it by pyCharm file |other settings | Preferences for new project | Project Interpreter)
  5). download apk https://apkpure.com/myobservatory-我的天文台/hko.MyObservatory_v1_0 MyObservatory 我的天文台_v4.17.12_apkpure.com.apk
  6). env variables setting : 
        export ANDROID_HOME=/Users/rongyao.ma/Library/Android/sdk
        export PATH=$PATH:$MONO_HOME/bin:${GOPATH}/bin:$JAVA_HOME/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools/30.0.3:.
  7). connect android device to macBook (enable USB debugging)
  8). adb devices (list devices) 
  9). start appium and start inspector session
  10). set desired_capability :
          {
              "platformName": "Android",
              "deviceName": "MQS7N19603012111",
              "app": "/Users/rongyao.ma/Downloads/MyObservatory_v4.17.12_apkpure.com.apk"
          }
  11). start session and locate elements 
  12). code and debug
  13). optimize script
  
3. A short description on your design, your test case
   1). store apk to real device
   2). open app and click buttons necessary to go to the 9-Day page
   3). check all the weather infomation :temperature, precipitation, wind, tips, day_of_week are correct.



Task 2:
The information from Task 1 (9-day forecast) is from Hong Kong Observatory API, please:
1. Capture the related API endpoint
2. Send a request using this API endpoint with your preferred language
3. Test the request response status is whether successful or not
4. Extract the relative humidity (e,g, 60 - 85%) for ​the day after tomorrow​ from the API
response (e.g. if today is Monday, then extract the relative humidity for Wednesday)

steps:  
    1). download fiddler  https://www.telerik.com/fiddler    Fiddler Everywhere 1.4.1.dmg
    2). set fiddler proxy (http/https enable remote computer connect) port 8866
    3). set proxy on phone (host:192.168.1.36 port 8866)
    4). visit ipv4.fiddler:8866 to fetch cert and install cert
    5). open MyObservatory app
    6). most captured traffic show :pda.weather.gov.hk:443 connect
    7). tcpdump -vvvvv |grep pda.weather.gov.hk to find the request is encryted
    8). brew install apktool
    9). apktool d MyObservatory_v4.17.12_apkpure.com.apk
    10). change MyObservatory_v4.17.12_apkpure.com.apk to MyObservatory_v4.17.12_apkpure.com.apk.zip
    11). uzip MyObservatory_v4.17.12_apkpure.com.apk.zip
    12). brew install dex2jar
    13).
    14). download JD-GUI  https://mac.filehorse.com/download-jd-gui-java-decompiler/  jd-gui-osx-1.6.6.tar
    
    
