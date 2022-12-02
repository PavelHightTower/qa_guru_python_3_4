def pretty_print(func, *args):
    function_name = func.__name__
    return function_name.replace("_", " ").title(), *args


def open_browser(browser_name):
    return print(*pretty_print(open_browser, browser_name))


def go_to_companyname_homepage(page_url):
    return print(*pretty_print(go_to_companyname_homepage, page_url))


def find_registration_button_on_login_page(page_url, button_text):
    return print(*pretty_print(find_registration_button_on_login_page, page_url, button_text))


open_browser("Chrome")
go_to_companyname_homepage("https://google.com")
find_registration_button_on_login_page("https://google.com/", "search")

