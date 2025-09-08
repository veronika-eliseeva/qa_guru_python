from selene import browser, be, have

from selene.support.shared import config
import os

reports_path = os.path.join('D:', 'selene_reports', 'screenshots')
os.makedirs(reports_path, exist_ok=True)

config.reports_folder = reports_path

browser.open('https://duckduckgo.com/')
browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
browser.element('html').should(have.text('QA.GURU'))
#browser.element('[id="search"]').should(have.text('qa.guru - Курсы тестировщиков'))
