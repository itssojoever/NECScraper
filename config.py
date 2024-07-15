#Provides a GUI for configuration of the scraper

#Standard library
import json
import os


#Third party libraries
import tkinter

from tkinter import messagebox
from tkinter import ttk


root = tkinter.Tk()
root.geometry("630x500")
root.title("NEC checker configuration")
root.iconname()

def loadData():
        if os.path.isfile("inputs.json"):
            print("JSON file found")
            with open("inputs.json", mode="r") as f:
                try:
                    data = json.load(f)
                    emailInput.insert(0, data["email_address"].capitalize())
                    confirmEmailInput.insert(0, data["email_address"].capitalize())
                except json.JSONDecodeError:
                    print("JSON file exists but is empty. It will be populated later")
        else:
            print("No JSON file found, creating file")
            with open ("inputs.json", "w") as f:
                pass

def saveData():
    givenEmail = emailInput.get().upper().strip()
    givenEmail2 = confirmEmailInput.get().upper().strip()
    if givenEmail == givenEmail2:

        information = {
            "email_address" : givenEmail,
        }

        with open("inputs.json", "w") as f:
            json.dump(information, f)
            if len("inputs.json") >1:
                messagebox.showinfo(title="Saved", message="Settings saved successfully")
            else:
                messagebox.showerror(title="Error", message="Something went wrong. Please re-try")
    else:
        messagebox.showerror(title="Error", message="Emails do not match, please try again")

#Frames>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
programFrame1 = tkinter.LabelFrame(root)
programFrame1.grid(row=0, column=0)

#frame1

l1 = ttk.Label(programFrame1, font="helvetica, 12", text="Please enter email address: ")
emailInput = ttk.Entry(programFrame1, font="helvetica", width=50)

l2 = ttk.Label(programFrame1, font="helvetica, 12", text="Please confirm email address: ")
confirmEmailInput = ttk.Entry(programFrame1, font="helvetica, 12", width=50)

l3 = ttk.Label(programFrame1, font="helvetica, 12", text="Save settings")
saveButton = ttk.Button(command=saveData)


#Layout>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#frame1
emailInput.grid(row=0, column=1, padx=10, pady=10)
l1.grid(row=0, column=0, padx=15)

confirmEmailInput.grid(row=1, column=1, padx=10, pady=10)
l2.grid(row=1,column=0, padx=15)

l3.grid(row=2, column=0, padx=15)
saveButton.grid(row=3, column=1, padx=15)

loadData()

root.mainloop()