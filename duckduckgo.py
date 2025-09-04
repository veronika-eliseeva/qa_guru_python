from selene import browser, be, have, by

import pytest

def test_positive_search():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('.react-results--main').should(have.text('qa'))

def test_negative_search():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('ллопрапвавывапаро').press_enter()
    browser.element(by.partial_text('По запросу')).should(be.visible)