#Intermittently checks the website of the National Exhibition Centre in Birmingham for events relating to my interests

import selenium
import requests
from apscheduler.schedulers.background import BlockingScheduler
import email
import smtplib
from env import
from win10toast import ToastNotifier
import sys
from bs4 import BeautifulSoup

toaster = ToastNotifier()

with open:
    pass

def necScrape():


def apsScheduler():
    scheduler = BlockingScheduler
    necSearch_1 = scheduler.add_job(necScrape)


def emailClient(emailaddress, bodyOfText):
    print ("New suitable event found, trying to send email")
    try:
        with smtplib.SMTP (smtpInfoS, smtpInfoP) as conn:
            conn.ehlo()

            conn.starttls()

            conn.login(smtpInfoE, smtpInfoK)

            conn.sendmail(smtpInfoE, emailaddress, bodyOfText)

            conn.quit()

            print ("Email sent")

            toaster.show_toast("Email sent", "A new suitable event at the NEC has been organised. Please see email", duration=7)

    except:
        print ("Failed to send email. Debug file created")
        #terminalOutput = sys.stdout
        #with open ("output.txt", "w") as debugFile:

