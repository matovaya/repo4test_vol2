from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_should_be_add_to_basket_button(browser):
	browser.get(link)
	assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), \
		"Add to basket button is not available"
