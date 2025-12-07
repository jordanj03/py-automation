from playwright.sync_api import sync_playwright, Playwright
import json

def run(playwright: Playwright):
	firefox = playwright.firefox
	browser = firefox.launch(headless=False)
	context = browser.new_context()
	page = context.new_page()
	with open("cookies.json", "r") as f:
		cookies = json.loads(f.read())
		context.add_cookies(cookies)
	page.goto("https://instagram.com")
	# page.get_by_label("username").fill("student")
	# page.get_by_label("password").fill("Password123")
	# page.get_by_role('button', name="Submit").click()
	input("Press Enter to close the browser...")
	browser.close()

with sync_playwright() as playwright:
	run(playwright)