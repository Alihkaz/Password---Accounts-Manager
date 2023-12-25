
#imports
from tkinter import * 
from tkinter import messagebox
import random
import pyperclip 
import json


# ---------------------------- Functions to generate passwords and save inputs ------------------------------- #

def generate_pas():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
             , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  nr_letters = random.randint(8, 15)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  
  password_combinations = []
  
  password_letters=[random.choice(letters) for char in range(nr_letters) ]
  
  password_symbols=[random.choice(symbols) for char in range(nr_symbols)]
  
  password_numbers=[random.choice(numbers) for char in range(nr_numbers)]
  
  
  password_combinations=password_letters+password_numbers+password_symbols
  
  random.shuffle(password_combinations)
  
  password="".join(password_combinations)
  
  passinput.insert(0, f"{password}")
  pyperclip.copy(password)
  
  
# ---------------------------- SAVING PASSWORD ------------------------------- #

def Save_data():
  website= websiteinput.get()
  email=usernamedata.get()
  password=passinput.get()
  new_data={
    website:{
      "email":email,
      "password":password
    }
  }

  if (websiteinput.get()=="") or (passinput.get()=="") :
    messagebox.showinfo(title="!",message=" Please don't leave any fields empty !")
    
  else:
  
    try:
      
      with open("data.json","r") as datafile:     
        data=json.load(datafile)
        
    except FileNotFoundError: 
      with open("data.json","w") as datafile :
        data=json.dump(new_data,datafile,indent=4)
      
    else:
        data.update(new_data)
        with open("data.json","w") as datafile:
          json.dump(data,datafile,indent=4)
          
    finally:
        websiteinput.delete(0,END)
        usernamedata.delete(0,END)
        usernamedata.insert(0, "@gmail.com")
        passinput.delete(0,END)


#------------------------------------------------searching for password------------------------------------------------------------------------
#

def find_pass():
  website= websiteinput.get()
  try:
    with open("data.json","r") as datafile:
          #reading old data
          data=json.load(datafile)
  except FileNotFoundError:
    messagebox.showinfo(title="Error 404",message="File not found !")

  else:
    
    if website in data:
      email=data[website]["email"]
      password=data[website]["password"]
      messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
    else:
       messagebox.showinfo(title="Error 404",message=f"No Details Found for {website} exists")


  


# ----------------------------------------------------------- UI SETUP -------------------------------------------------------------- #




window=Tk()
window.title("Password's And Account's Manager")
window.config(padx=32,pady=32)


canvas=Canvas(width=300,height=300)
passwordimage=PhotoImage(file="logo.png")

canvas.create_image(100,100,image=passwordimage)
canvas.grid(column=1,row=0)


#labels

websitelabel=Label(text="Website:",font=("Courier",10))
websitelabel.grid(column=0,row=1)


emaillabel=Label(text="Email/Username:",font=("Courier",10))
emaillabel.grid(column=0,row=2)

passlabel=Label(text="Password:",font=("Courier",10))
passlabel.grid(column=0,row=3)

#data entry fields

websiteinput=Entry(width=20)
websiteinput.grid(column=1,row=1)
websiteinput.focus()

usernamedata=Entry(width=40)
usernamedata.grid(column=1,row=2,columnspan=2)
usernamedata.insert(0, "@gmail.com")



passinput=Entry(width=21)
passinput.grid(column=1,row=3)

#buttoms

generatepass=Button(text="Generate Password",width=15,command=generate_pas)
generatepass.grid(column=2,row=3)


adddata=Button(text="Add",width=39,command=Save_data)
adddata.grid(column=1,row=4,columnspan=2)

search_buttom=Button(text="Search",width=15,command=find_pass)
search_buttom.grid(column=2,row=1)

window.mainloop()