import os.path

from selene import have, be, browser


def test_demoqa():
    browser.open('/')
    browser.element("#firstName").type("Artem")
    browser.element("#lastName").type("Plotnikov")
    browser.element("#userEmail").type("artem.plotnikov@mail.ru")
    browser.element("#genterWrapper").element(".custom-control-label").click()
    browser.element("#userNumber").type("1234567890")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element("option[value='0']").click()
    browser.element(".react-datepicker__year-select").element("option[value='2000']").click()
    browser.element(".react-datepicker__day--020").click()

    browser.element("#subjectsInput").type("Maths").press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('./images/img.jpg'))
    browser.element("#currentAddress").type("Pushkin 12 515")
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-content').should(have.text('Artem Plotnikov'))
    browser.element('.modal-content').should(have.text('artem.plotnikov@mail.ru'))
    browser.element('.modal-content').should(have.text('Male'))
    browser.element('.modal-content').should(have.text('1234567890'))
    browser.element('.modal-content').should(have.text('20 January,2000'))
    browser.element('.modal-content').should(have.text('Maths'))
    browser.element('.modal-content').should(have.text('Sports, Music'))
    browser.element('.modal-content').should(have.text('img.jpg'))
    browser.element('.modal-content').should(have.text('Pushkin 12 515'))
    browser.element('.modal-content').should(have.text('Haryana Karnal'))

    #Close
    browser.element('#closeLargeModal').click()