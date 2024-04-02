# Locators from most to least preferred
1. **Role and Text:** `page.get_by_role("button", name="Submit")`
2. **Test ID:** `page.get_by_test_id("add-to-cart-button)`
3. **CSS Selector:** `page.locator("button.myId")`
4. **XPATH as a Last Resort:** `page.locator('//button[@text()='Click me']')`