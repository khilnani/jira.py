# coding: utf-8

"""
Description:
Launch a browser with the URL to Jira with a JQL query. On iOS Pythonista supports App Share and clipboard, on linux/Mac OS supports command line arguments.

License:
The MIT License (MIT)
Copyright (c) 2016 Nik Khilnani

Github:
https://github.com/khilnani/jira.py

Configuration:
Rename 'jira.sample.conf' to 'jira.conf' and update values
To use:
1 - In any app, use App Share, Run in Pythonista and then select this script
2 - Copy text and run this script within Pythonista. 
"""

import appex
import clipboard
import console
import webbrowser
import json
import urllib
from objc_util import *

CONF_FILE = 'jira.conf'

def get_conf_info():
    try:
        with open(CONF_FILE, 'r') as conf_file:
            conf = json.load(conf_file)
            url = conf['BASE_URL']
            try:
                user = conf['USER']
            except KeyError:
                user = None
            return (url, user)
    except IOError:
        logging.error('Could not find %s' % CONF_FILE)
        sys.exit()

def main():
    text = None
    if appex.is_running_extension():
        text = appex.get_text()
    if not text:
        text = console.input_alert('Jira Query')
    if text:
        base_url, username = get_conf_info()
        url = '%s/issues/?jql=%s' % (base_url, urllib.quote_plus(text))
        console.hud_alert('Launching Jira')
        app=UIApplication.sharedApplication()
        url=nsurl(url)
        app.openURL_(url)
    else:
        console.hud_alert('No input text found.')
    if appex.is_running_extension():
        appex.finish()

if __name__ == '__main__':
    main()