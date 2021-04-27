# Feishu_Temperature
Automatic upload your temperatures on feishu just for nku students
飞书nk微应用定时填报体温脚本

### 使用方法
首先安装selenium： pip install selenium
#### Chrome
1. 下载ChromeDriver：http://chromedriver.storage.googleapis.com/index.html （注意下载的driver版本与Chrome浏览器版本的匹配）
3. 下载后解压到：python文件夹的Scripts目录下
4. 找到浏览器user_data_dir，替换掉Line11处的地址（chrome://version/， 个人资料路径）

#### FireFox
1. 下载geckodriver：https://github.com/mozilla/geckodriver/releases （注意下载的driver版本与firefox浏览器版本的匹配）
2. 下载后解压到任意目录，配置环境变量PATH
3. 找到浏览器user_data_dir，替换掉Line6处的地址（帮助-更多排障信息-配置文件夹）

首次使用需要先访问https://feishu.nankai.edu.cn/?appid=229 登录一次，之后运行程序就可以实现自动填报了！

程序运行开始，到达规定时间后会自动打开Chrome浏览器，进行填报，注意此时不能有其他Chrome浏览器窗口打开，否则会报错


**本程序仅供娱乐，仅用于解决忘记填报这一问题，请在合理且合法的范围内使用本程序。如果填报表中任意情况发生变化，请务必在手动填报。**


