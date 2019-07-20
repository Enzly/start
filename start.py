#!/usr/bin/python

import subprocess, webbrowser, time

if not 'start.py' in open('.gitignore').read():
    open('.gitignore','a').write("start.py")

subprocess.call('atom .', shell=True)
time.sleep(3)

subprocess.call('start php artisan serve', shell=True)
time.sleep(.600)

subprocess.call('start npm run watch', shell=True)
time.sleep(6)

site = "http://localhost:8000"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(site)
