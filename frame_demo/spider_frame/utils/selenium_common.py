# coding: utf-8
# @Author : lryself
# @Date : 2022/7/27 23:17
# @Software: PyCharm

class SeleniumBrowser:
    class _PrivateProperty:
        class ConstError(TypeError):
            pass

        class ConstCaseError(ConstError):
            pass

        def __init__(self, isHeadless, isService):
            self.isHeadless = isHeadless
            self.isService = isService

        def __setattr__(self, key, value):
            if self.__dict__.get(key) is not None:  # 判断有没有该常量
                raise self.ConstError('%s 常量已存在' % key)
            else:
                self.__dict__[key] = value  # 初次设置该常量时会执行这里

    class InlineProperty:
        def __init__(self, retry_number):
            self.retry_number = retry_number

    def __init__(self, driver="Chrome", retry_number=10, isHeadless=False, isService=False):
        if driver is "Chrome":
            self.browser = self.init_webdriver_chrome()
        else:
            self.browser = None
        self.retry_number = 10
        self.const = self._PrivateProperty(isHeadless=isHeadless, isService=isService)
        self.property = self.InlineProperty(retry_number=retry_number)
        from selenium.webdriver.support.wait import WebDriverWait
        self.wait = WebDriverWait(self.browser, 60)

    def init_webdriver_chrome(self, chromedriver_path: str = "chromedriver"):
        from selenium import webdriver

        service_args = []
        # 不加载图片,不缓存在硬盘(内存)
        if self.const.isService:
            service_args.extend(['--load-images=false', '--disk-cache=false'])
        option = webdriver.ChromeOptions()
        # 无头模式
        if self.const.isHeadless:
            option.add_argument('headless')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        browser = webdriver.Chrome(executable_path=chromedriver_path, options=option, service_args=service_args)
        browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                {'source': 'Object.defineProperty(navigator, "webdriver", {get: () =>undefined})'})
        return browser

    def get_element(self, xpath):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait

        for i in range(self.property.retry_number):
            try:
                return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            except Exception:
                self.browser.refresh()
        return WebDriverWait(self.browser, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
