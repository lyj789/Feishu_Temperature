from selenium import webdriver
import time
while True:
  time_now = time.strftime("%H:%M:%S", time.localtime())
  if time_now == "11:11:11":
    # profile_directory = r'C:\Users\DELL\AppData\Roaming\Mozilla\Firefox\Profiles\ufngooe2.default-release'
    # profile = webdriver.FirefoxProfile(profile_directory)
    # browser = webdriver.Firefox(firefox_profile=profile, executable_path=r'D:\GeckoDriver\geckodriver.exe')

    option = webdriver.ChromeOptions()
    # option.add_argument(r'user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data')
    chrome_dir = os.path.join(os.environ['LOCALAPPDATA'],"\\Google\\Chrome\\User Data\\")
    option.add_argument('user-data-dir=' + chrome_dir)
    browser=webdriver.Chrome(options=option)
    browser.get('https://feishu.nankai.edu.cn/?appid=229')
    time.sleep(10)
    js = """
    var q1=document.getElementById("q1");
    var arr=q1.options;
    var text=arr[3].value;
    document.getElementById("q1").value = text ;
    
    var q16=document.getElementById("q16");
    var arr2=q16.options;
    var text2=arr2[3].value;
    document.getElementById("q16").value = text2 ;
    
    var q17=document.getElementById("q17");
    var arr3=q17.options;
    var text3=arr3[3].value;
    document.getElementById("q17").value = text3 ;
    
    var q13=document.getElementById("q13");
    var arr4=q13.options;
    var text4=arr4[1].value;
    document.getElementById("q13").value = text4 ;
    
    if($(".saveBtn").attr("disabled")!="disabled"&&g_boolPromise)
      fnSave('submit');
      
    """
    browser.execute_script(js)
    time.sleep(10)
    browser.quit()

    time.sleep(60)
