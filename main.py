#Intermittently checks the website of the National Exhibition Centre in Birmingham for events relating to my interests

import requests
#from apscheduler.schedulers.background import BlockingScheduler
import smtplib
from dotenv import load_dotenv
from win10toast import ToastNotifier
#import sys
import os
import json
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "NECEventsFinder/1.0 (+https://www.joefisher.uk/)"
}

#Config file needed for projectFolder, and destination email address

load_dotenv() #load environment variables from .env

smtpInfoS = os.getenv("smtpInfoS") #SMTP server
smtpInfoP = os.getenv("smtpInfoP") #port
smtpInfoE = os.getenv("smtpInfoE") #sender email
smtpInfoK = os.getenv("smtpInfoK") #gmail key

toaster = ToastNotifier()

if os.path.isfile("inputs.json"):
    print ("Configuration found")
    with open("inputs.json", "r") as f:
        try:
            data = json.load(f)
            emailAddress = data.get("email_address")
            #project_Folder = data.get("project_folder")
            print (f"Recipient email address is {emailAddress}")
            #print (f"The folder within which to store web pages is {project_Folder}")

        except Exception as e:
            print(f"{e}")

def emailClient(emailAddress, bodyOfText):
    print ("New suitable event(s) found, trying to send email")
    header = "Keywords found in NEC events"
    body = bodyOfText
    emailMessage = f"Subject: {header}\n\n{body}"
    try:
        with smtplib.SMTP (smtpInfoS, smtpInfoP) as conn:
            conn.ehlo()

            conn.starttls()

            conn.login(smtpInfoE, smtpInfoK)

            conn.sendmail(smtpInfoE, emailAddress, emailMessage)

            conn.quit()

            print ("Email sent")

            toaster.show_toast("Email sent", "Events with configured keywords found at the NEC. Please see email", duration=7)

    except Exception as e:
        print (f"Error: {e}")

def necScrape():
    url_list = [] #Store all event URLs

    found_URLs = {} #Store all URLs with text matching one or more of the keywords

    url = "https://www.thenec.co.uk/whats-on/"

    keywordsDesired = ["tech",
                        "politics",
                        "technology",
                        "artificial intelligence",
                        "computers",
                        "computer",
                        "political",
                        "engineering",
                        "engineers",
                        "software",
                        "future",
                        "developers",
                        "developer",
                        ]
    
    print(f"Designated keywords: {keywordsDesired}")
    
    response = requests.get(url)
    print(f"response: {response}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    targetLine = soup.find("input", {"id": "WhatsonItemsJson"})
    if targetLine:
        json_Data = targetLine.get("value")

        try:
            JSON = json.loads(json_Data)
            #print(JSON)

            for item in JSON:
                if "Url" in item:
                    url_list.append(item["Url"])
            print (f"Discovered {len(url_list)} links")
            print ("including:")
            for url in url_list:
                print(url)

            confirmSearch = input(f"Do you wish to scan all {len(url_list)} links for designated keywords?. Enter y for yes: ")
            if confirmSearch.lower() == "y":
                for url in url_list:
                    print (f"Checking URL: {url}")
                    response = requests.get(f"https://www.thenec.co.uk{url}")
                    if response.ok:
                        soup = BeautifulSoup(response.content, "html.parser")
                        time.sleep(2) #Etiquette: spread out requests
                        pageText = soup.get_text().lower()
                        locatedKeywords = [keyword for keyword in keywordsDesired if keyword.lower() in pageText]
                        if locatedKeywords:
                            print('\x1b[6;30;42m' + f"Keyword(s) found in {url}: {locatedKeywords}" + '\x1b[0m')
                            found_URLs[url] = locatedKeywords
                            #found_URLs.append(f"https://www.thenec.co.uk{url}")

                        else:
                            print(f"No keyword(s) found in {url}")
                    else:
                        print(f"Error. Status code: {response.status_code}")
            else:
                print ("Search cancelled")
        except Exception as e:
            print (f"Exception: {e}")
    
    else:
        print ("Error")
        
    if confirmSearch.lower() == "y":
        bodyOfText = json.dumps(found_URLs, indent=4, sort_keys=True)
        with open ("bodyOfText.txt", "w") as f:
            f.write(bodyOfText)

        emailClient(emailAddress, bodyOfText)

necScrape()


#def apsScheduler(): 
#    scheduler = BlockingScheduler
#    necSearch_1 = scheduler.add_job(necScrape)


#emailClient(emailAddress, bodyOfText)

