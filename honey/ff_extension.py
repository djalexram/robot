def create_profile(path):
	from selenium import webdriver
	fp =webdriver.FirefoxProfile()
	fp.add_extension('/Users/djalex/robot/honey/browser_plugins/honey-9.5.3-mac.xpi')
	fp.set_preference("extensions.honey.currentVersion", "9.5.3")
	fp.update_preferences()
	return fp.path