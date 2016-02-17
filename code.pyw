#!/usr/bin/python
# -*- coding: UTF-8 -*-

from splinter.browser import Browser
import time
import traceback

def log(str):
	fo = open("D:/python/log.txt", "a")
	fo.write("---------- " + time.strftime('%Y-%m-%d %H:%M:%S') + " ----------\n" \
		 + str +"\n\n");
	fo.close()
    
try:
    b = Browser(driver_name="chrome")
    b.visit("https://www.baidu.com/baidu?word=%E6%97%A5%E5%8E%86")
    today = b.find_by_css('.op-calendar-new-table-today').first
    if today.has_class('op-calendar-new-table-rest') \
            or (today.has_class('op-calendar-new-table-weekend') \
            and not today.has_class('op-calendar-new-table-work')):
        log('Day off')
    else :
        b.visit("https://ckip.worksap.co.jp/cws/cws/srwtimerec")
        b.fill("user_id", "C170");
        b.fill("password", "wencong38")
        b.find_by_value(u" 出 社 / Work start ").click()
        b.quit()
        log("Recorded");
        
except Exception, e:
	log(traceback.format_exc())