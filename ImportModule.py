# import  webbrowser
#
# webbrowser.open('http://www.youtube.com')
# webbrowser.open_new_tab('http://www.facebook.com')

# from selenium import webdriver
#
# def Open_Google():
#     driver = webdriver.Chrome()
#     driver.get('http://www.google.com')
#     driver.close()
#
# Open_Google()

from webbrowser import open

def Open_Youtube():
    open('http://www.youtube.com')

Open_Youtube()

def open_website(site):
    return open(site)

open_website('http://www.wikipedia.com')

