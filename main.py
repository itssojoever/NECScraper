#Intermittently checks the website of the National Exhibition Centre in Birmingham for events relating to my interests

import requests
from apscheduler.schedulers.background import BlockingScheduler
import smtplib
from dotenv import load_dotenv
from win10toast import ToastNotifier
import sys
import os
import json
from bs4 import BeautifulSoup
from pywebcopy import save_webpage

#Config file needed for projectFolder, and destination email address

load_dotenv()

toaster = ToastNotifier()

if os.path.isfile("inputs.json"):
    print ("Configuration found")
    with open("inputs.json", "r") as f:
        try:
            data = json.load()

def necScrape():
    savepage = save_webpage 
    savepage(url="https://www.thenec.co.uk/whats-on/",
             project_folder=projectFolder,
             project_name="NEC",
             bypass_robots=False, #respectful fr fr
             debug=True,
             open_in_browser=False,
             delay=None,
             threaded=False,
             )
    #class
    #aria-label
    #href=
    #Download website daily
    #compare new download one with old download. 
    #If new download differs, access the new pages. 
    #Parse for key words.
    #Send email


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

