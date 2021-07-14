from selenium import webdriver

import time

driver=webdriver.Chrome()

# 浏览器最大化
driver.maximize_window()
time.sleep(2)

driver.get("https://www.baidu.com/")

#
# # 操作浏览器的前进、后退
# first_url="https://www.baidu.com/"  # 访问百度首页
# driver.get(first_url)
# time.sleep(3)
#
# second_url="https://news.baidu.com/" # 访问新闻页面
# driver.get(second_url)
# time.sleep(3)
#
# driver.back() # 后退到百度首页
# time.sleep(2)
#
# driver.forward() # 前进到新闻页



# 设置浏览器宽、高
# driver.set_window_size(2000, 1000)
# time.sleep(4)



# 打印url
# url=driver.current_url
# print(url)

driver.find_element_by_id("kw").send_keys("西安")
driver.find_element_by_id("su").click()
time.sleep(4)

# #  控制浏览器滚动条
js="var q=document.documentElement.scrollTop=10000" # 滚动条拖到页面底部
driver.execute_script(js)
time.sleep(3)

js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3) # 滚动条拖到顶部


# driver.find_element_by_id("kw").clear()
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("十四届全运会")
# driver.find_element_by_id("su").submit()

# 获得文本信息
# text=driver.find_element_by_id("bottom_layer").text
# print(text)

# 固定等待和智能等待
# driver.find_element_by_id("kw").send_keys("西安")
# driver.find_element_by_id("su").submit()

# time.sleep(4) 固定等待 保证以上页面加载完后再进入下面的链接
# 智能等待 加载完毕后立即进入
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("西安(陕西省辖地级市、省会) - 百度百科").click()

# 在打印title时 如果没有这句 则在未完全加载的情况下 会打印 百度一下 你就知道
# time.sleep(6)

# 打印title
# title=driver.title
# print(title)

# 打印url
# url2=driver.current_url
# print(url2)


driver.quit()