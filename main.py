#!/usr/bin/env python3 

from tkinter import * 
from tkinter import messagebox # need to import separately as it is not a class 
from random import choice, randint, shuffle
import pyperclip 
import json 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
    
    lets = [choice(letters) for _ in range(randint(8, 10))] 
    syms = [choice(symbols) for _ in range(randint(2, 4))] 
    nums = [choice(numbers) for _ in range(randint(2, 4))] 

    password_list = lets + syms + nums 
    shuffle(password_list)
    pass_word = ''.join(password_list)
    password.insert(0, pass_word)
    pyperclip.copy(pass_word) 

# ---------------------------- SAVE PASSWORD ------------------------------- #  
    
def save():
    web_data = website.get()
    email_data = email_user.get()
    password_data = password.get()
    new_data = {
        web_data: {
            'email': email_data,
            'password': password_data, 
        }
    }
    
    if web_data and email_data and password_data:
        is_ok = messagebox.askokcancel(message=f'Details entered:\nWebsite: {web_data}\nEmail: {email_data}\nPassword: {password_data}\nSave?')
        if is_ok:
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
            
            except FileNotFoundError as error_message:
                print(error_message)
                with open('data.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
            
            else:
                data.update(new_data)
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
            
            finally: # we do not really need the finally keyword but might as well 
                website.delete(0, END)
                password.delete(0, END) # could also write 'end'
                messagebox.showinfo(message='Success! Data saved to file!')
                pyperclip.copy(password_data)
    else:
        messagebox.showwarning(title='Oops', message='Don\'t leave any fields empty!') # titles do not show on macos without a special technique! 
        
# -----------------------SHOW EMAIL/PASSWORD -------------------------- #

def find_password():
    web_data = website.get()
    if web_data:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                site = web_data
                email = data[web_data]['email']
                password = data[web_data]['password'] 
        except FileNotFoundError as error_message:
            print(error_message)
            messagebox.showinfo(message='No data file found')
        except KeyError as error_message:
            print(error_message)
            messagebox.showinfo(message=f'No data found for {site}')
        else:
            messagebox.showinfo(message=f'Website: {web_data}\nEmail: {email}\nPassword: {password}')
            pyperclip.copy(password)
    else:
        messagebox.showinfo(message='Please enter a website') 
        
              

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('password manager')
window.config(padx=45, pady=45, bg='#9bdeac') # green hex code 

# create the canvas widget:
canvas = Canvas(width=200, height=200, bg='#9bdeac', highlightthickness=0) 
canvas.grid(row=0, column=1)

# load and add image to canvas:
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)

#LABELS:
# website label:
website_label = Label(text='website:', bg='#9bdeac', fg='#000080') # navy hex code 
website_label.grid(row=1, column=0)

# email/username label:
email_user_label = Label(text='email/username:', bg='#9bdeac', fg='#000080')
email_user_label.grid(row=2, column=0)

# password label:
password_label = Label(text='password:', bg='#9bdeac', fg='#000080')
password_label.grid(row=3, column=0)

#BUTTONS:
# generate password button:
gen_pass = Button(text='Generare Password', bg='#FFFFFF', fg='#000000', highlightthickness=0, borderwidth=0, highlightbackground='#9bdeac', highlightcolor='#9bdeac', width=10, command=generate_password) 
gen_pass.grid(row=3, column=2, pady=3, padx=1)

# add button:
add = Button(text='Add', bg='#FFFFFF', fg='#000000', highlightthickness=0, borderwidth=0, highlightbackground='#9bdeac', highlightcolor='#9bdeac', width=32, command=save)
add.grid(row=4, column=1, columnspan=2, pady=3)

# search button:
search = Button(text='Search', bg='#FFFFFF', fg='#000000', highlightthickness=0, borderwidth=0, highlightbackground='#9bdeac', highlightcolor='#9bdeac', width=10, command=find_password)
search.grid(row=1, column=2, pady=3, padx=1)

# ENTRIES:
# website entry:
website = Entry(width=21, bg='#9bdeac', fg='#000000', highlightthickness=0) # white hex code, black hex code 
website.grid(row=1, column=1, pady=3)  
website.focus() 

# email/username entry:
email_user = Entry(width=35, bg='#9bdeac', fg='#000000', highlightthickness=0)
email_user.grid(row=2, column=1, columnspan=2, pady=3)
email_user.insert(0, 'johnroddy.16@gmail.com')

# password entry:
password = Entry(width=21, bg='#9bdeac', fg='#000000', highlightthickness=0)
password.grid(row=3, column=1, pady=3)
 
    



window.mainloop()  