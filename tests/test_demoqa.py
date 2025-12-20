from selene import have, be, browser


def test_demoqa():
    browser.open('/')
    browser.element("#firstName").should(be.blank)
    browser.element("#lastName").should(be.blank)
    browser.element("#userEmail").should(be.blank)