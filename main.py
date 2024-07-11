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

smtpInfoS = os.getenv("smtpInfoS")
smtpInfoP = os.getenv("smtpInfoP")
smtpInfoE = os.getenv("smtpInfoE")
smtpInfoK = os.getenv("smtpInfoK")

toaster = ToastNotifier()

if os.path.isfile("inputs.json"):
    print ("Configuration found")
    with open("inputs.json", "r") as f:
        try:
            data = json.load(f)
            emailAddress = data.get("email_address")
            project_Folder = data.get("project_folder")
            print (f"Target email address is {emailAddress}")
            print (f"The folder within which to store web pages is {project_Folder}")

        except Exception as e:
            print(f"{e}")

def necScrape():
    savepage = save_webpage 
    savepage(url="https://www.thenec.co.uk/whats-on/",
             project_folder=project_Folder,
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

bodyOfText = "placeholder"


def emailClient(emailAddress, bodyOfText):
    print ("New suitable event found, trying to send email")
    try:
        with smtplib.SMTP (smtpInfoS, smtpInfoP) as conn:
            conn.ehlo()

            conn.starttls()

            conn.login(smtpInfoE, smtpInfoK)

            conn.sendmail(smtpInfoE, emailAddress, bodyOfText)

            conn.quit()

            print ("Email sent")

            toaster.show_toast("Email sent", "A new suitable event at the NEC has been organised. Please see email", duration=7)

    except:
        print ("Failed to send email. Debug file created")
        #terminalOutput = sys.stdout
        #with open ("output.txt", "w") as debugFile:

emailClient(emailAddress, bodyOfText)

