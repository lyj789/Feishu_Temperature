# Feishu_Temperature
Automatic upload your temperatures on feishu just for nku students
每天上午十点定时填报体温

### 使用方法
首先安装selenium： pip install selenium
#### Chrome
1. 下载ChromeDriver：http://chromedriver.storage.googleapis.com/index.html （注意下载的driver版本与Chrome浏览器版本的匹配）
3. 下载后解压到：python文件夹的Scripts目录下
4. 找到浏览器user_data_dir，替换掉Line13处的地址（chrome://version/， 个人资料路径）

#### FireFox
1. 下载geckodriver：https://github.com/mozilla/geckodriver/releases （注意下载的driver版本与firefox浏览器版本的匹配）
2. 下载后解压到任意目录，配置环境变量PATH
3. 找到浏览器user_data_dir，替换掉Line8处的地址（帮助-更多排障信息-配置文件夹）

首次使用需要先访问https://feishu.nankai.edu.cn/?appid=229 登录一次，之后运行程序就可以实现自动填报了！
