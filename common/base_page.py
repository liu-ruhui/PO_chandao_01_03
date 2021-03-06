import time

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.conf_utils import conf
from selenium.webdriver.support import expected_conditions as EC

from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

#浏览器操作封装 -->二次封装
    def open_url(self,url):
        self.driver.get( url )
        logger.info('打开url地址 %s '% url )
    def set_maxwindow(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')
    def set_minwindow(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')
    def implicitly_wait(self,seconeds=conf.time_out):
        self.driver.implicitly_wait(seconeds)
        logger.info('隐式等待%s秒'%seconeds)
    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')
    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s:'%value)
        return value
    def close(self):
        value = self.driver.close()
        logger.info('关闭当前页面')
        return value
    def quit_driver(self):
        self.driver.quit()
        logger.info('退出浏览器')

 #元素操作封装
    #element_info = {'element_name': '登录按钮','locator_type': 'xpath', 'locator_value': '//input[@name="keepLogin[]"]', 'timeout': 5}
    def find_element(self,element_info):
        self.element_name = element_info['element_name']
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_time = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver,locator_time)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        # element = WebDriverWait(self.driver,locator_time)\
        #     .until(EC.presence_of_element_located(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功' % self.element_name)
        return element

#元素点击操作
    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作' % self.element_name)
#元素输入内容
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s'% (self.element_name,content))

#获取某个元素(title)的值
    def get_element_attribute(self, element_info, content):
        element = self.find_element(element_info)
        value = element.get_attribute(content)
        # element.getattribute(content)
        logger.info('[%s]元素查找%s的值:%s' % (self.element_name, content,value))
        return value

#获取文本值
    def text(self, element_info):
        element = self.find_element(element_info)
        logger.info('[%s]元素获取文本值:%s' % (self.element_name,element.text))
        return element.text


#鼠标键盘封装（建议代码思路：判断操作系统类型）
#鼠标移动到元素
    def move_to_element_by_mouse(self,element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info('鼠标移动到元素【%s】上'%self.element_name)
#在元素上长按
    def long_press_element(self,element_info,seconds):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(seconds).release(element)
    def elemnet_keybord(self,element_info,content):
        element = self.find_element(element_info)
        if content == 'enter':
           element.send_keys(Keys.ENTER)
        elif content == 'backspace':
           element.send_keys(Keys.BACKSPACE)
        elif content == 'tab':
           element.send_keys(Keys.TAB)

#执行js脚本

    # 方法一：适用于多个方法调用self.driver.execute_script
    # def execute_script(self,js_str,element_info=None):
    #     if element_info:
    #         self.driver.execute_script(js_str)
    #     else:
    #         self.driver.execute_script(js_str,None)
    #
    # def delete_element_attribute(self,element_info,attribute_name):
    #     element = self.find_element(element_info)
    #     self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    # def update_element_attribute(self, element_info, attribute_name,attribute_value):
    #     element = self.find_element(element_info)
    #     self.execute_script('arguments[0].setAttribute("%s","%s");' %(attribute_name,attribute_value), element)
    #     logger.info('[%s]元素修改属性[%s]的值为[%s]'%(element_info['element_name'],attribute_name,attribute_value))
    # 方法二
# 移除元素属性
    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)
        logger.info('[%s]元素移除属性[%s]'%(self.element_name,attribute_name))
#修改元素属性
    def update_element_attribute(self, element_info, attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");' %(attribute_name,attribute_value), element)
        logger.info('[%s]元素修改属性[%s]的值为[%s]'%(self.element_name,attribute_name,attribute_value))
# 浏览器滚动条滑动
    def scrolltop(self,content):
        st = 'document.body.scrollTop=%d;'
        if content%2==0:
            self.driver.execute_script(st%1000)  #往下滑
            logger.info('浏览器向下滑')
        else:
            self.driver.execute_script(st% -1000) #往上滑
            logger.info('浏览器向上滑')
#判断是否获取到元素
    def get_argument(self,element_info):
        element = self.find_element(element_info)
        self.driver.execute_script("arguments[0].style.border='5px dashed #CCFFFF';", element)
        logger.info('[%s]元素已经获取'%self.element_name)

#获取当前窗口的句柄
    def get_window_handle(self):
        logger.info('获取当前窗口的句柄')
        return  self.driver.current_window_handle
#切换句柄
    def switch_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)
        logger.info('切换句柄到%s'%window_handle)
#通过标题切换浏览器窗口
    def switch_window_by_title(self,title):
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,conf.time_out).until(EC.title_contains(title)):
               self.driver.switch_to.window(window_handle)
            # if self.driver.title.__contains__(title):
               break
        logger.info('切换到标题为[%s]的界面'%title)
#通过url切换窗口浏览器
    def switch_window_by_url(self, url):
        for handle in self.driver.window_handles:
            if WebDriverWait(self.driver,conf.time_out).until(EC.title_contains(url)):
                self.driver.switch_to.window(handle)
                break
        logger.info('切换到链接为为[%s]的界面' % url)

#截图
    def screenshot_as_file(self,*screenshot_path):
        current_dir = os.path.dirname(__file__)

        if len(screenshot_path) == 0:
            screenshot_filepath = conf.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir,'..',screenshot_filepath,'UITest_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)


#切换到alter元素
    # def swich_to_alter(self):
    #     self.driver.switch_to.alert()
    #     logger.info('切换到alter元素')
#弹窗封装
    def switch_to_alter(self,action='accept',time_out = conf.time_out):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        logger.info('切换到alter元素')
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
            logger.info('点击alter确认按钮,获取弹窗文本为%s'%alter_text)
        elif action == 'dismiss':
            alter.dismiss()
            logger.info('点击alter取消按钮,获取弹窗文本为%s'%alter_text)
        return alter_text
# 向prompt中输入文字
    def alter_input(self,content):
        self.driver.switch_to.alert.send_keys(content)
        logger.info('向prompt输入文字[%s]'%content)

#进入frame框架
    def swich_to_frame(self,element_info):
        self.wait(2)
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]元素进入frame框架内'%self.element_name)
#退出Frame框架
    def default_frame(self):
        self.driver.switch_to.default_content()
        logger.info('退出框架')
#固定等待
    def wait(self,seconed=conf.time_out):
        time.sleep(seconed)
        logger.info('固定等待%s秒'%seconed)