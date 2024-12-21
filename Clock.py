# imports libraries
from tkinter  import *
from time import strftime
from tkinter.ttk import *
from time import *
import requests

#asks for users city/town
City = input("What town do you live in? ")

#accesses Weatherapi
response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={'b57135aa24ae4639a21194427240810'}&q={City}")

# asks for users name
name1 = input("What's your name? ")

#creates window
root = Tk()
root.title("Clock")

# styles window
root.configure(bg='lightblue')

#creates weather and location
def weather():
    extra = "°C in"
    data = response.json()
    string =(data['current']['temp_c'],  extra, City, data['location']['country'])
    lbl3.config(text = string)
#creates clock
def time():
    string = strftime('%H:%M %p')
    lbl.config(text = string)
    lbl.after(1000, time)
#creates custom message based on users name and their system time
def name():
    string = strftime('%H:%M')
    if ('%03:00') < string < ('%12:00'):
        string = ( "Good morning", name1)
        lbl2.config(text = string)
    elif ('%12:00') < string < ('%17:00'):
        string = ("Good Afternoon", name1)
        lbl2.config(text = string)
    else:
        string = ("Good evening", name1)
        lbl2.config(text = string)
    

# adds style to clock and messages
lbl = Label(root, font=('calibri', 200, 'bold'))
lbl2 = Label(root, font=('calibri', 100, 'bold'))
lbl3 = Label(root, font=('calibri', 50, 'bold'))
 
#puts elements in right area
lbl.pack(anchor='n')
lbl2.pack(anchor='center')
lbl3.pack(anchor= 's')

#runs code
time()
name()
weather()

mainloop()