from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # URL of the login page
    login_url = 'https://dathang.baoden.vn/login'
    
    # Navigate to the login page
    page.goto(login_url)
    
    # Enter login credentials
    page.fill('input[name="email"]', 'FFFFFF@gmail.com')
    page.fill('input[name="password"]', 'FFFF@#')
    
    # Submit the login form
    page.click('button[type="submit"]')
    
    # Wait for navigation after login
    page.wait_for_load_state('networkidle')
    
    # Navigate to the target page
    target_url = 'https://dathang.baoden.vn/carts'
    page.goto(target_url)
    
    # Wait for the network to be idle and ensure the specific element is loaded
    page.wait_for_load_state('networkidle')
    page.wait_for_selector('#app')
    
    # Extract the entire body content
    content = page.content()
    
    # Save the content to a .txt file
    with open('page_content2.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    
    # Print a success message
    print("HTML content saved to page_content2.txt")
    
    # Clean up
    browser.close()