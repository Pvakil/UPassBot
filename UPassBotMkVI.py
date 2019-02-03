from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Tkinter import *
import Tkinter as tk
import os
import datetime
import win32com.client

try:
    with open('backup') as f:
        lines = [line.rstrip('\n') for line in open('backup')]
        data = lines
        #print(data)
        f.close
except:
    pass

# Finds date for text msg
import datetime
from twilio.rest import Client
global month
month = datetime.datetime.now().strftime("%m")
if month == "01":
    month = "February"
if month == "02":
    month = "March"
if month == "03":
    month = "April"
if month == "04":
    month = "May"
if month == "05":
    month = "June"
if month == "06":
    month = "July"
if month == "07":
    month = "August"
if month == "08":
    month = "September"
if month == "09":
    month = "October"
if month == "10":
    month = "November"
if month == "11":
    month = "December"
if month == "12":
    month = "January"

OPTIONS = [
#"Choose University",
"Simon Fraser University",
"University of British Columbia",
"British Columbia Institute of Technology",
"Douglas College",
"Kwantlen Polytechnic University"

] #etc

account_sid = '<ACCOUNTSID>'
auth_token = '<AUTHTOKEN>'
client = Client(account_sid, auth_token)

def handler():
    #print("Entering Handller...")
    f = open("backup", "w")
    #print("Writing...")
    f.write(entry_username.get())
    #print("Writing...")
    f.write("\n")
    f.write(entry_password.get())
    #print("Writing...")
    f.write("\n")
    f.write(entry_number.get())
    #print("Writing...")
    f.write("\n")
    f.write(variable.get())
    print(str(variable.get()))
    f.write("\n")
    val = str(var.get())
    #print(str(val))
    print(val)
    f.write(val)
    f.close()
    #print("Quiting...")

    root.destroy()


def renew():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://upassbc.translink.ca/")
    school = str(variable.get())
    option_visible_text = school
    select = driver.find_element_by_id("PsiId")



    #now use this to select option from dropdown by visible text
    driver.execute_script("var select = arguments[0]; for(var i = 0; i < select.options.length; i++){ if(select.options[i].text == arguments[1]){ select.options[i].selected = true; } }", select, option_visible_text);
    driver.find_element_by_name("PsiId").send_keys(Keys.RETURN)
    driver.find_element_by_name("PsiId").send_keys(Keys.RETURN)
    #driver.find_element_by_name("PsiId").send_keys(Keys.RETURN)
    #driver.find_element_by_name("PsiId").send_keys(Keys.RETURN)
    driver.find_element_by_name("PsiId").send_keys(Keys.DOWN)
    driver.find_element_by_name("PsiId").send_keys(Keys.UP)
    driver.find_element_by_name("PsiId").send_keys(Keys.TAB)
    element = driver.find_element_by_id("goButton")
    element.send_keys("RETURN")
    element.submit()
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    sfu_id = entry_username.get()
    sfu_password = entry_password.get()
    username.send_keys(str(sfu_id))
    password.send_keys(str(sfu_password))
    driver.find_element_by_tag_name("INPUT").send_keys(Keys.RETURN)
    driver.find_element_by_id("chk_1").click()
    driver.find_element_by_id("requestButton").click()
    # from is twilio number
    # to is my number
    message = client.messages \
    .create(
    body="Your Compass Card for " + month + " has been renewed!",
    from_='<TWILIONUMBER>,
    to= "+1" + str(number)
    )

    print(message.sid)




def text_test():
    #print(number)
    number = entry_number.get()
    print(number)
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = '<ACCOUNTSID>'
    auth_token = '<AUTHTOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Your Compass Card for " + month + " has been renewed!",
                     from_='<TWILIONUMBER>',
                     to= "+1" + str(number)
                 )

    print(message.sid)

#master = tk.Tk()




root = tk.Tk()
root.title("Compass Card Bot")
label1 = tk.Label(root, text="Username:")
label2 = tk.Label(root, text="Password:")
label3 = tk.Label(root, text="Phone Number:")
label4 = tk.Label(root, text="University:")
entry_password = tk.Entry(root,show='*')
entry_number= tk.Entry(root)
entry_username = tk.Entry(root)
variable = StringVar(root)
try:
    entry_username.insert(0, data[0])
    entry_password.insert(0, data[1])
    entry_number.insert(0, data[2])

except:
    pass


variable.set("Choose A University") # default value
w = OptionMenu(root, variable, *OPTIONS)
w.pack()
var = IntVar()
c = Checkbutton(root, text="Auto-Renew every Month", variable=var)
c.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
try:
    var.set(int(data[4]))
except:
    print("ERROR")
    pass
try:
    variable.set(str(data[3]))
except:
    print("ERROR")
    pass
if var == 1:
    print("TRUE")
#counter_label(label)
button = tk.Button(root, text='Renew Compass Card',width=25, command= lambda: renew())
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
entry_number.grid(row=2, column=1)
w.grid(row=3,column=1)
c.grid(row=0,column=2)
button.grid(row=6,column=1)
root.protocol("WM_DELETE_WINDOW", handler)
root.mainloop()
