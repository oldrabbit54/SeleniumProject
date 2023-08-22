# 🤖This is 'Automation in Python' course's final project.
Project is implemented via Python, Selenium & Pytest.\
For testing I chose a website "citilink.ru".\
Below I am going to list and describe main functions and test scenarios.

## Classes: 
### ProductSelection:
### apply_filters(filters):
Applies availability and rating filters by finding corresponding checkboxes and radio buttons.\
Args: filters - takes a dictionary with Filters' class fields.

### search_product(title, filters = None):
Finds search bar and types in passed item's name.\
Args: title - string, filters(None by default) - filters to be applied.

### ProductAcquire:
### add_to_cart():
Saves item's price and first word of its full name. Adds item to the cart.


### buy():
Starting item buying process, going to credentials page.

### assert_order():
Checking if items' prices and names are matching.


### finish_order(self, first_name, last_name, phone, city, street, building, flat, payment_method, second_phone=None, promocode=None):
After assert_order() enters passed information in corresponding input fields and presses Submit button.\
Args: first_name, last_name, phone, city, street, building, flat, payment_method, second_phone=None, promocode=None - passed information about the customer and the order.

### assert_success_order():
Checks if we are on "Success page" after successfully ordered the item(s).

### AuthorizationManager:
### login(username, password):
Using go_to_main_page() function visit main page, clicks on "Log in" button, enters passed user's data and submits it.\
Args: username, password - strings.

## Functions:
### go_to_main_page(driver, base_url):
Visits base_url address on the passed driver. \
Args: driver - WebDriver object, base_url - string.

### find_and_click_element(by: str, locator: str, driver):
Waits for the element to appear in DOM page, makes sure it is visible on a page(scrolls to it if needed) and clicks on it.\
Args: by(way of identifying object), locator(CSS, XPATH etc.) - strings

## Test functions:
### test_buy_product(test_runner):
Completes buying an item(Goes from main page to finishing the order).\
Args: test_runner fixture.

### test_login(test_runner):
Logs in account.\
Args: test_runner fixture

### test_runner():
Marks the start and the end of each test.

# Other unmentioned functions and classes are *_deprecated_*.
