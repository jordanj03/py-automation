from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
	firefox = playwright.firefox
	browser = firefox.launch(headless=False)
	context = browser.new_context()
	page = context.new_page()
	page.goto("https://practicetestautomation.com/practice-test-login/")
	page.get_by_label("username").fill("student")
	page.get_by_label("password").fill("Password123")
	page.get_by_role('button', name="Submit").click()
	page.screenshot(path="login.png")
	input("Press Enter to close the browser...")
	browser.close()

with sync_playwright() as playwright:
	run(playwright)