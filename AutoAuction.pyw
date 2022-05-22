import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from Helpers import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
import urllib.request
global username

class loginScreen:
    def __init__(self, root):
        #setting title
        root.title("MyBiddingApp")
        #setting window size

        # Login Title
        GLabel_465=tk.Label(root)
        GLabel_465["activebackground"] = "#ffffff"
        GLabel_465["activeforeground"] = "#ffffff"
        GLabel_465["bg"] = "#ffffff"
        ft = tkFont.Font(family='Cambria',size=78)
        GLabel_465["font"] = ft
        GLabel_465["fg"] = "#333333"
        GLabel_465["justify"] = "center"
        GLabel_465["text"] = "Login"
        GLabel_465["relief"] = "flat"
        GLabel_465.place(x=515,y=100,width=250,height=120)

        # Username Entry
        GLineEdit_724=ttk.Entry(root)
        GLineEdit_724["background"] = "#ffffff"
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_724["font"] = ft
        GLineEdit_724["foreground"] = "#000000"
        GLineEdit_724["justify"] = "center"
        GLineEdit_724["textvariable"] = "Username"
        GLineEdit_724.place(x=495,y=250,width=300,height=65)


        # Password Entry
        GLineEdit_723=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_723["font"] = ft
        GLineEdit_723["background"]="#ffffff"
        GLineEdit_723["foreground"] = "#000000"
        GLineEdit_723["justify"] = "center"
        GLineEdit_723["textvariable"] = "Password"
        GLineEdit_723.place(x=495,y=350,width=300,height=65)
        GLineEdit_723["show"] = "*"


        # Signin Button
        ft = tkFont.Font(family='Cambria',size=18)
        ttk.Style().configure('Accentbutton',font = ft, foreground = 'white',justify = "center")
        GButton_207=ttk.Button(root)
        GButton_207["style"] = "Accentbutton"
        #GButton_207["background"] = "#efefef"
        #ft = tkFont.Font(family='Cambria',size=18)
        #GButton_207["font"] = ft
        #GButton_207["foreground"] = "#000000"
        #GButton_207["justify"] = "center"
        GButton_207["text"] = "Sign in"
        #GButton_207["relief"] = "raised"
        GButton_207.place(x=495,y=460,width=300,height=50)
        GButton_207["command"] = self.GButton_207_command

        ft = tkFont.Font(family='Cambria',size=12)
        ttk.Style().configure('TButton',font = ft,foreground = 'white',justify = "center")

        # Register Button
        GButton_195=ttk.Button(root)
        GButton_195["style"] = "TButton"
        #GButton_195["bg"] = "#efefef"
        #ft = tkFont.Font(family='Cambria',size=13)
        #GButton_195["font"] = ft
        #GButton_195["fg"] = "#000000"
        #GButton_195["justify"] = "center"
        GButton_195["text"] = "Register"
        GButton_195.place(x=495,y=600,width=145,height=35)
        GButton_195["command"] = self.GButton_195_command

        # Forgot Password Button
        GButton_633=ttk.Button(root)
        GButton_633["style"] = "TButton"
        #GButton_633["bg"] = "#efefef"
        #ft = tkFont.Font(family='Cambria',size=13)
        #GButton_633["font"] = ft
        #GButton_633["fg"] = "#000000"
        #GButton_633["justify"] = "center"
        GButton_633["text"] = "Forgot Password"
        GButton_633.place(x=655,y=600,width=145,height=35)
        GButton_633["command"] = self.GButton_633_command

    # Checks if login information is correct
    def GButton_207_command(self):
        global username
        widget = root.winfo_children()
        successful = LogIn(widget[1].get(), widget[2].get())
        self.username = widget[1].get()
        if not successful:
            GLabel_466=tk.Label(root)
            GLabel_466["activebackground"] = "#ffffff"
            GLabel_466["activeforeground"] = "#ffffff"
            GLabel_466["bg"] = "#ffffff"
            ft = tkFont.Font(family='Cambria',size=24)
            GLabel_466["font"] = ft
            GLabel_466["fg"] = "#ff0000"
            GLabel_466["justify"] = "center"
            GLabel_466["text"] = "You have entered an incorrect username or password!"
            GLabel_466["relief"] = "flat"
            GLabel_466.place(x=242,y=25,width=850,height=80)
            return
        else:
            username = widget[1].get()
            for widget in root.winfo_children():
                widget.destroy()
            selectionScreen(root)


    # Goes to Registration Page
    def GButton_195_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        reg1(root,[])

    # Forgor Password
    def GButton_633_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        forgorPassword1(root)

class forgorPassword1:
    def __init__(self, root):
        #setting title
        root.title("Forgot Password?")
        #setting window size

        #Page Title
        GLabel_132=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = "Forgot password?"
        GLabel_132.place(x=520,y=140,width=230,height=80)

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        #Return Home Button
        GButton_644=ttk.Button(root)
        GButton_644["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=8)
        #GButton_644["font"] = ft
        #GButton_644["fg"] = "#000000"
        #GButton_644["justify"] = "center"
        GButton_644["text"] = "Return Home"
        GButton_644.place(x=10,y=10,width=120,height=34)
        GButton_644["command"] = self.GButton_644_command

        # Phone number entry
        GLineEdit_764=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_764["font"] = ft
        GLineEdit_764["background"]="#ffffff"
        GLineEdit_764["foreground"] = "#000000"
        GLineEdit_764["justify"] = "center"
        GLineEdit_764.place(x=488,y=320,width=300,height=65)

        #instruction Label
        GLabel_638=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=13)
        GLabel_638["font"] = ft
        GLabel_638["fg"] = "#333333"
        GLabel_638["justify"] = "center"
        GLabel_638["text"] = "Enter your phone number below"
        GLabel_638.place(x=460,y=250,width=350,height=50)

        #GLabel_91=tk.Label(root)
        #ft = tkFont.Font(family='Cambria',size=13)
        #GLabel_91["font"] = ft
        #GLabel_91["fg"] = "#333333"
        #GLabel_91["justify"] = "center"
        #GLabel_91["text"] = "If the number you entered is associated with an account, you will recieve your password via text"
        #GLabel_91.place(x=430,y=480,width=400,height=100)

        ft = tkFont.Font(family='Cambria',size=8)
        ttk.Style().configure('TButton',font = ft)

        #next button
        GButton_25=ttk.Button(root)
        GButton_25["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_25["font"] = ft
        #GButton_25["fg"] = "#000000"
        #GButton_25["justify"] = "center"
        GButton_25["text"] = "Next"
        GButton_25.place(x=598,y=400,width=70,height=25)
        GButton_25["command"] = self.GButton_25_command

    # return home
    def GButton_644_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)

    # next button
    def GButton_25_command(self):
        widgets = root.winfo_children()
        phonenumber = widgets[2].get()
        phonenumber = phonenumber.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        ForgotPassword(phonenumber)
        GLabel_91=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=16)
        GLabel_91["font"] = ft
        GLabel_91["fg"] = "#00AB00"
        GLabel_91["justify"] = "center"
        GLabel_91["text"] = "If the number you entered is associated with an account, you will recieve your password via text.\n You can return home now"
        GLabel_91.place(x=185,y=450,width=900,height=150)

class selectionScreen:
    def __init__(self, root):
        #setting title
        root.title("Selection Screen")
        #setting window size
        self.username = username
        # Selection screen Title
        GLabel_11=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=60)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#333333"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "Are you Looking to . . ."
        GLabel_11.place(x=250,y=30,width=796,height=110)

        # this OR that
        GLabel_930=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=45)
        GLabel_930["font"] = ft
        GLabel_930["fg"] = "#333333"
        GLabel_930["justify"] = "center"
        GLabel_930["text"] = "OR"
        GLabel_930.place(x=460,y=490,width=354,height=152)

        ft = tkFont.Font(family='Cambria',size=26)
        ttk.Style().configure('Accentbutton',font = ft)

        # Make a bid button
        GButton_586=ttk.Button(root)
        GButton_586["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=48)
        #GButton_586["font"] = ft
        #GButton_586["fg"] = "#000000"
        #GButton_586["justify"] = "center"
        GButton_586["text"] = "Make a Bid"
        GButton_586.place(x=80,y=480,width=438,height=180)
        GButton_586["command"] = self.GButton_586_command

        # Put up an item button
        GButton_895=ttk.Button(root)
        GButton_895["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=48)
        #GButton_895["font"] = ft
        #GButton_895["fg"] = "#000000"
        #GButton_895["justify"] = "center"
        GButton_895["text"] = "Put up an item"
        GButton_895.place(x=770,y=480,width=438,height=180)
        GButton_895["command"] = self.GButton_895_command

    # Forwards to Search results
    def GButton_586_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        searchScreen(root)

    # Forwards to putting up an item page
    def GButton_895_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        Sell(root)

class reg1:
    def __init__(self, root,usr):
        self.data = usr
        #setting title
        root.title("Registration")
        #setting window size

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Return Home Button
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Return Home"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        # Registration Title
        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Registration"
        GLabel_367.place(x=320,y=30,width=679,height=99)

        # Next page button
        GButton_793=ttk.Button(root)
        GButton_793["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_793["font"] = ft
        #GButton_793["fg"] = "#000000"
        #GButton_793["justify"] = "center"
        GButton_793["text"] = "Next Page"
        GButton_793.place(x=610,y=630,width=90,height=45)
        GButton_793["command"] = self.GButton_793_command

        # Name Label
        GLabel_573=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "center"
        GLabel_573["text"] = "Name:"
        GLabel_573.place(x=255,y=140,width=91,height=71)

        # Name Entry
        GLineEdit_17=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_17["font"] = ft
        GLineEdit_17["background"]="#ffffff"
        GLineEdit_17["foreground"] = "#000000"
        GLineEdit_17["justify"] = "center"
        GLineEdit_17.place(x=390,y=140,width=560,height=75)

        # Username Label
        GLabel_206=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_206["font"] = ft
        GLabel_206["fg"] = "#333333"
        GLabel_206["justify"] = "center"
        GLabel_206["text"] = "Username:"
        GLabel_206.place(x=180,y=270,width=175,height=71)

        # Username Entry
        GLineEdit_479=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_479["font"] = ft
        GLineEdit_479["background"]="#ffffff"
        GLineEdit_479["foreground"] = "#000000"
        GLineEdit_479["justify"] = "center"
        GLineEdit_479.place(x=390,y=270,width=560,height=75)

        # Email Label
        GLabel_535=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_535["font"] = ft
        GLabel_535["fg"] = "#333333"
        GLabel_535["justify"] = "center"
        GLabel_535["text"] = "Email:"
        GLabel_535.place(x=260,y=400,width=91,height=71)

        # Email Entry
        GLineEdit_433=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_433["font"] = ft
        GLineEdit_433["background"]="#ffffff"
        GLineEdit_433["foreground"] = "#000000"
        GLineEdit_433["justify"] = "center"
        GLineEdit_433.place(x=390,y=400,width=560,height=75)

        # Phone Number Label
        GLabel_175=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_175["font"] = ft
        GLabel_175["fg"] = "#333333"
        GLabel_175["justify"] = "center"
        GLabel_175["text"] = "Phone Number:"
        GLabel_175.place(x=117,y=530,width=236,height=71)

        # Phone Number Entry
        GLineEdit_238=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_238["font"] = ft
        GLineEdit_238["background"]="#ffffff"
        GLineEdit_238["foreground"] = "#000000"
        GLineEdit_238["justify"] = "center"
        GLineEdit_238.place(x=390,y=530,width=560,height=75)


    # Returns to login screen
    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)

    # Forwards to next page
    def GButton_793_command(self):
        widgets = root.winfo_children()
        self.data.append(widgets[4].get())
        self.data.append(widgets[6].get())
        self.data.append(widgets[8].get())
        self.data.append(widgets[10].get())

        for widget in root.winfo_children():
            widget.destroy()
        reg2(root,self.data)

class reg2:

    def __init__(self, root,usr:list):
        self.data = usr
        #setting title
        root.title("Registration")
        #setting window size

        # Return Home Button
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Return Home"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        # Title of page
        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Personal Info"
        GLabel_367.place(x=320,y=20,width=679,height=99)

        # Next page button
        GButton_793=ttk.Button(root)
        GButton_793["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=8)
        #GButton_793["font"] = ft
        #GButton_793["fg"] = "#000000"
        #GButton_793["justify"] = "center"
        GButton_793["text"] = "Next Page"
        GButton_793.place(x=610,y=630,width=90,height=45)
        GButton_793["command"] = self.GButton_793_command

        # Gender Entry
        GLineEdit_17=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_17["font"] = ft
        GLineEdit_17["background"]="#ffffff"
        GLineEdit_17["foreground"] = "#000000"
        GLineEdit_17["justify"] = "center"
        GLineEdit_17.place(x=390,y=120,width=560,height=75)

        # Gender Label
        GLabel_573=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "center"
        GLabel_573["text"] = "Gender:"
        GLabel_573.place(x=220,y=120,width=120,height=71)

        # Birthday Label
        GLabel_206=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_206["font"] = ft
        GLabel_206["fg"] = "#333333"
        GLabel_206["justify"] = "center"
        GLabel_206["text"] = "Birthday:"
        GLabel_206.place(x=200,y=220,width=141,height=71)

        # Birthday Entry
        GLineEdit_479=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_479["font"] = ft
        GLineEdit_479["background"]="#ffffff"
        GLineEdit_479["foreground"] = "#000000"
        GLineEdit_479["justify"] = "center"
        GLineEdit_479.place(x=390,y=220,width=560,height=75)

        # Address Label
        GLabel_535=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_535["font"] = ft
        GLabel_535["fg"] = "#333333"
        GLabel_535["justify"] = "center"
        GLabel_535["text"] = "Address:"
        GLabel_535.place(x=210,y=320,width=131,height=71)

        # Address Entry
        GLineEdit_433=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_433["font"] = ft
        GLineEdit_433["background"]="#ffffff"
        GLineEdit_433["foreground"] = "#000000"
        GLineEdit_433["justify"] = "center"
        GLineEdit_433.place(x=390,y=320,width=560,height=75)

        # Password Entry
        GLineEdit_238=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_238["font"] = ft
        GLineEdit_238["background"]="#ffffff"
        GLineEdit_238["foreground"] = "#000000"
        GLineEdit_238["justify"] = "center"
        GLineEdit_238.place(x=390,y=420,width=560,height=75)

        # Password Label
        GLabel_175=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_175["font"] = ft
        GLabel_175["fg"] = "#333333"
        GLabel_175["justify"] = "center"
        GLabel_175["text"] = "Password:"
        GLabel_175.place(x=188,y=420,width=155,height=71)

        # Confirm Password Label
        GLabel_372=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLabel_372["font"] = ft
        GLabel_372["fg"] = "#333333"
        GLabel_372["justify"] = "center"
        GLabel_372["text"] = "Confirm Password:"
        GLabel_372.place(x=50,y=520,width=300,height=71)

        # Confrim Password Entry
        GLineEdit_210=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_210["font"] = ft
        GLineEdit_210["background"]="#ffffff"
        GLineEdit_210["foreground"] = "#000000"
        GLineEdit_210["justify"] = "center"
        GLineEdit_210.place(x=390,y=520,width=560,height=75)

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Back Button
        GButton_282=ttk.Button(root)
        GButton_282["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_282["font"] = ft
        #GButton_282["fg"] = "#000000"
        #GButton_282["justify"] = "center"
        GButton_282["text"] = "Back"
        GButton_282.place(x=1150,y=10,width=120,height=35)
        GButton_282["command"] = self.GButton_282_command

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)

    def GButton_793_command(self):
        widgets = root.winfo_children()
        password = widgets[9].get()
        confirmPass = widgets[12].get()

        if(password!=confirmPass):
            GLabel_466=tk.Label(root)
            GLabel_466["activebackground"] = "#ffffff"
            GLabel_466["activeforeground"] = "#ffffff"
            GLabel_466["bg"] = "#ffffff"
            ft = tkFont.Font(family='Cambria',size=18)
            GLabel_466["font"] = ft
            GLabel_466["fg"] = "#ff0000"
            GLabel_466["justify"] = "center"
            GLabel_466["text"] = "The passwords do not match!"
            GLabel_466["relief"] = "flat"
            GLabel_466.place(x=242,y=25,width=850,height=80)
            return
        else:
            self.data.append(widgets[3].get())
            self.data.append(widgets[6].get())
            self.data.append(widgets[8].get())
            self.data.append(widgets[9].get())
            #widgets[12].get()

            for widget in root.winfo_children():
                widget.destroy()
            reg3(root,self.data)


    def GButton_282_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        reg1(root,[])

class reg3:
    def __init__(self, root,usr):
        self.data = usr
        #setting title
        root.title("Registration")
        #setting window size

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Return Home Button
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Return Home"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        # Page Title
        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Enter Banking Info"
        GLabel_367.place(x=320,y=30,width=679,height=99)

        # Next Page Button
        GButton_793=ttk.Button(root)
        GButton_793["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_793["font"] = ft
        #GButton_793["fg"] = "#000000"
        #GButton_793["justify"] = "center"
        GButton_793["text"] = "Next Page"
        GButton_793.place(x=610,y=630,width=90,height=45)
        GButton_793["command"] = self.GButton_793_command

        # Cardnumber Entry
        GLineEdit_17=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_17["font"] = ft
        GLineEdit_17["background"]="#ffffff"
        GLineEdit_17["foreground"] = "#000000"
        GLineEdit_17["justify"] = "center"
        GLineEdit_17.place(x=360,y=140,width=600,height=55)

        # Cardnumber Label
        GLabel_573=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "center"
        GLabel_573["text"] = "Card Number:"
        GLabel_573.place(x=110,y=150,width=250,height=40)

        # Back Button
        GButton_282=ttk.Button(root)
        GButton_282["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_282["font"] = ft
        #GButton_282["fg"] = "#000000"
        #GButton_282["justify"] = "center"
        GButton_282["text"] = "Back"
        GButton_282.place(x=1150,y=10,width=120,height=35)
        GButton_282["command"] = self.GButton_282_command

        # Cardholder Label
        GLabel_334=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_334["font"] = ft
        GLabel_334["fg"] = "#333333"
        GLabel_334["justify"] = "center"
        GLabel_334["text"] = "Name on Card:"
        GLabel_334.place(x=107,y=230,width=250,height=40)

        # Expiry Date Label
        GLabel_80=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_80["font"] = ft
        GLabel_80["fg"] = "#333333"
        GLabel_80["justify"] = "center"
        GLabel_80["text"] = "Expiration Date:"
        GLabel_80.place(x=100,y=320,width=250,height=40)

        # Security code label
        GLabel_806=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_806["font"] = ft
        GLabel_806["fg"] = "#333333"
        GLabel_806["justify"] = "center"
        GLabel_806["text"] = "Security Code:"
        GLabel_806.place(x=110,y=410,width=250,height=40)

        # Cardholder Entry
        GLineEdit_638=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_638["font"] = ft
        GLineEdit_638["background"]="#ffffff"
        GLineEdit_638["foreground"] = "#000000"
        GLineEdit_638["justify"] = "center"
        GLineEdit_638.place(x=360,y=230,width=600,height=55)

        # Month Entry
        GLineEdit_685=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=18)
        GLineEdit_685["font"] = ft
        GLineEdit_685["background"]="#ffffff"
        GLineEdit_685["foreground"] = "#000000"
        GLineEdit_685["justify"] = "center"
        GLineEdit_685.place(x=360,y=320,width=275,height=40)

        # Year Entry
        GLineEdit_125=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=18)
        GLineEdit_125["font"] = ft
        GLineEdit_125["background"]="#ffffff"
        GLineEdit_125["foreground"] = "#000000"
        GLineEdit_125["justify"] = "center"
        GLineEdit_125.place(x=685,y=320,width=275,height=40)

        # Month Label
        GLabel_377=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=14)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Month"
        GLabel_377.place(x=460,y=360,width=70,height=25)

        # Year Label
        GLabel_700=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=14)
        GLabel_700["font"] = ft
        GLabel_700["fg"] = "#333333"
        GLabel_700["justify"] = "center"
        GLabel_700["text"] = "Year"
        GLabel_700.place(x=790,y=360,width=70,height=25)

        # Security Code Entry
        GLineEdit_611=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_611["font"] = ft
        GLineEdit_611["background"]="#ffffff"
        GLineEdit_611["foreground"] = "#000000"
        GLineEdit_611["justify"] = "center"
        GLineEdit_611.place(x=360,y=410,width=600,height=55)

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)


    def GButton_793_command(self):
        widgets = root.winfo_children()
        self.data.append(widgets[3].get())
        self.data.append(widgets[9].get())
        self.data.append(widgets[10].get()+"/"+widgets[11].get()) # 02/22
        self.data.append(widgets[14].get())
        for widget in root.winfo_children():
            widget.destroy()
        reg4(root,self.data)


    def GButton_282_command(self):
        for widget in root.winfo_children():
            widget.destroy()

        self.data.pop()
        self.data.pop()
        self.data.pop()
        self.data.pop()

        reg2(root,self.data)

class reg4:
    def __init__(self, root,usr):
        self.data = usr
        self.sussessful = VerifyUser(self.data[3])
        #setting title
        root.title("Verification")
        #setting window size

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Return Home Button
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Return Home"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        # Page Title
        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Confirm Verification Code"
        GLabel_367.place(x=320,y=90,width=679,height=99)

        # Verification code Entry
        GLineEdit_17=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLineEdit_17["font"] = ft
        GLineEdit_17["background"]="#ffffff"
        GLineEdit_17["foreground"] = "#000000"
        GLineEdit_17["justify"] = "center"
        GLineEdit_17.place(x=330,y=320,width=650,height=75)

        # Back Button
        GButton_282=ttk.Button(root)
        GButton_282["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_282["font"] = ft
        #GButton_282["fg"] = "#000000"
        #GButton_282["justify"] = "center"
        GButton_282["text"] = "Back"
        GButton_282.place(x=1150,y=10,width=120,height=35)
        GButton_282["command"] = self.GButton_282_command

        ft = tkFont.Font(family='Cambria',size=20)
        ttk.Style().configure('Accentbutton',font = ft)

        # Confirm Button
        GButton_245=ttk.Button(root)
        GButton_245["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=30)
        #GButton_245["font"] = ft
        #GButton_245["fg"] = "#000000"
        #GButton_245["justify"] = "center"
        GButton_245["text"] = "Confirm"
        GButton_245.place(x=560,y=410,width=190,height=85)
        GButton_245["command"] = self.GButton_245_command

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)

    def GButton_282_command(self):
        for widget in root.winfo_children():
            widget.destroy()

        self.data.pop()
        self.data.pop()
        self.data.pop()
        self.data.pop()

        reg3(root,self.data)


    def GButton_245_command(self):
        widgets = root.winfo_children()
        if(self.sussessful != widgets[2].get()): #THIS IS TO DISPLAY A WRONG CODE CHANGE WHEN BACKEND HAS REACHED HERE
            GLabel_372=tk.Label(root)
            ft = tkFont.Font(family='Cambria',size=22)
            GLabel_372["font"] = ft
            GLabel_372["fg"] = "#ff0000"
            GLabel_372["justify"] = "center"
            GLabel_372["text"] = "Wrong Code, please try again with new code"
            GLabel_372.place(x=390,y=560,width=550,height=71)
            self.sussessful = VerifyUser(self.data[3])
            return
        else:
            Register(self.data)
            self.GButton_791_command()

class searchScreen:
    global GLineEdit_178
    def __init__(self, root):
        #setting title
        root.title("Search")
        #setting window size
        self.username = username

        # Page Title
        GLabel_11=tk.Label(root)
        GLabel_11["borderwidth"] = "1px"
        ft = tkFont.Font(family='Cambria',size=70)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#333333"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "Search"
        GLabel_11.place(x=380,y=90,width=530,height=135)

        # Search Bar
        GLineEdit_178=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=26)
        GLineEdit_178["font"] = ft
        GLineEdit_178["background"]="#ffffff"
        GLineEdit_178["foreground"] = "#000000"
        GLineEdit_178["justify"] = "center"
        GLineEdit_178.place(x=30,y=260,width=1240,height=60)

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Logout
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Logout"
        GButton_791.place(x=20,y=20,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        ft = tkFont.Font(family='Cambria',size=20)
        ttk.Style().configure('Accentbutton',font = ft)

        GButton_457=ttk.Button(root)
        GButton_457["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=36)
        #GButton_457["font"] = ft
        #GButton_457["fg"] = "#000000"
        #GButton_457["justify"] = "center"
        GButton_457["text"] = "Enter"
        GButton_457.place(x=510,y=360,width=266,height=81)
        GButton_457["command"] = self.GButton_457_command

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)


    def GButton_457_command(self):
        for widget in root.winfo_children():
            if "entry" in str(widget):
                usr = widget.get()
            widget.destroy()
        resultsScreen(root,usr)

class resultsScreen:
    def __init__(self, root,usr):
        #setting title
        root.title("Results Screen")
        #setting window size

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Logout Button
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Logout"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        # Back Button
        GButton_816=ttk.Button(root)
        GButton_816["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_816["font"] = ft
        #GButton_816["fg"] = "#000000"
        #GButton_816["justify"] = "center"
        GButton_816["text"] = "Back"
        GButton_816.place(x=1150,y=10,width=120,height=34)
        GButton_816["command"] = self.GButton_816_command

        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Your Search Results"
        GLabel_367.place(x=300,y=0,width=679,height=99)


        def getCurrent(event):
            value = myList.item(myList.selection(),"text")
            for widget in root.winfo_children():
                widget.destroy()

            productScreen(root, GetInformationAboutListing(value),usr)

        listings = GetRelevantListings(str(usr).lower())


        listOfItems = ttk.Scrollbar(root)
        listOfItems.place(x=1260,y=150,width=20,height=550)

        myList = ttk.Treeview(root, selectmode="browse",yscrollcommand=listOfItems.set, height=28)
        myList.column("#0",width=1200,anchor= "center")

        listOfItems.config(command=myList.yview)

        myList.heading("#0", text="Item", anchor='center')

        myList.bind("<<TreeviewSelect>>",getCurrent)

        myList.place(x=20, y=150, width = 1235, height = 550)

        for listing in listings:
            myList.insert(parent='',index="end",text=listing)

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)


    def GButton_816_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        searchScreen(root)


    def GButton_869_command(self):
        print("command")

class productScreen:
    def __init__(self, root,listOfInfo,q):
        from urllib.request import urlopen
        from io import BytesIO
        #setting title
        root.title("Product for auction")
        #setting window size
        self.usr = q
        self.listOfInfo = listOfInfo

        name = self.listOfInfo[0]
        desc = self.listOfInfo[1]
        pic = self.listOfInfo[2]
        startingBid = self.listOfInfo[3]
        endTime = self.listOfInfo[4]
        seller = self.listOfInfo[5]
        biddingHis = self.listOfInfo[6]
        temp = biddingHis.split('|')
        self.biddingHistory=temp
        # 1000-aadi|1500-harsh|2000-mittaPatel|
        buyOut = self.listOfInfo[7]

        URL = pic
        u = urlopen(URL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        img = im.resize((600, 360), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(image=photo)
        label.image = photo
        label.place(x=50,y=85,width=600,height=360)

        # Product Title
        GLabel_132=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=30)
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = name
        GLabel_132.place(x=140,y=10,width=1000,height=75)

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        # Back Button
        GButton_578=ttk.Button(root)
        GButton_578["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=8)
        #GButton_578["font"] = ft
        #GButton_578["fg"] = "#000000"
        #GButton_578["justify"] = "center"
        GButton_578["text"] = "Back"
        GButton_578.place(x=1150,y=10,width=120,height=34)
        GButton_578["command"] = self.GButton_578_command

        # Logout Button
        GButton_644=ttk.Button(root)
        GButton_644["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=8)
        #GButton_644["font"] = ft
        #GButton_644["fg"] = "#000000"
        #GButton_644["justify"] = "center"
        GButton_644["text"] = "Logout"
        GButton_644.place(x=10,y=10,width=120,height=34)
        GButton_644["command"] = self.GButton_644_command

        # Place bid write bid amount
        GLineEdit_764=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=10)
        GLineEdit_764["font"] = ft
        GLineEdit_764["background"]="#ffffff"
        GLineEdit_764["foreground"] = "#000000"
        GLineEdit_764["justify"] = "center"
        GLineEdit_764.place(x=690,y=480,width=350,height=65)

        # Description Stuff
        descriptionFrame=ttk.LabelFrame(root, text='Description', width=535, height=300)
        descriptionFrame.place(x=710, y=120)

        GLabel_91=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=13)
        GLabel_91["font"] = ft
        GLabel_91["fg"] = "#333333"
        GLabel_91["justify"] = "center"
        GLabel_91["text"] = wrapText(desc,65)
        GLabel_91.place(x=730,y=150,width=500,height=250)

        ft = tkFont.Font(family='Cambria',size=14)
        ttk.Style().configure('Accentbutton',font = ft)

        #bid button
        GButton_25=ttk.Button(root)
        GButton_25["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_25["font"] = ft
        #GButton_25["fg"] = "#000000"
        #GButton_25["justify"] = "center"
        GButton_25["text"] = "Place Bid!"
        GButton_25.place(x=1080,y=480,width=150,height=65)
        GButton_25["command"] = self.GButton_25_command

        # end date
        dateFrame=ttk.LabelFrame(root, text='End Date', width=265, height=80)
        dateFrame.place(x=980, y=588)

        GLabel_226=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=12)
        GLabel_226["font"] = ft
        GLabel_226["fg"] = "#333333"
        GLabel_226["justify"] = "center"
        GLabel_226["text"] = str(endTime)
        GLabel_226.place(x=990,y=605,width=230,height=60)

        # Buy-Out
        dateFrame=ttk.LabelFrame(root, text='Buy-Out', width=265, height=80)
        dateFrame.place(x=370, y=468)

        GLabel_878=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=12)
        GLabel_878["font"] = ft
        GLabel_878["fg"] = "#333333"
        GLabel_878["justify"] = "center"
        GLabel_878["text"] = "$" + str(buyOut)
        GLabel_878.place(x=380,y=483,width=230,height=60)

        # Starting bid
        dateFrame=ttk.LabelFrame(root, text='Starting Bid', width=265, height=80)
        dateFrame.place(x=685, y=588)

        #Starting Bid Label
        GLabel_1=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=12)
        GLabel_1["font"] = ft
        GLabel_1["fg"] = "#333333"
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = str(startingBid)
        GLabel_1.place(x=695,y=605,width=230,height=60)

        # Seller
        sellerFrame=ttk.LabelFrame(root, text='Sold by', width=265, height=80)
        sellerFrame.place(x=370, y=588)

        GLabel_191=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=12)
        GLabel_191["font"] = ft
        GLabel_191["fg"] = "#333333"
        GLabel_191["justify"] = "center"
        GLabel_191["text"] = seller
        GLabel_191.place(x=380,y=605,width=230,height=60)

        # List of bids
        listOfItems = ttk.Scrollbar(root)
        listOfItems.place(x=330,y=470,width=20,height=200)
        myList = ttk.Treeview(root, selectmode="browse",yscrollcommand=listOfItems.set)

        myList.heading("#0", text="Bid History", anchor='center')
        myList.column("#0",anchor= "center")

        myList.place(x=60,y=470,width=270,height=200)

        for bid in reversed(self.biddingHistory):
            myList.insert(parent="", index='end', text=bid)

        '''
        listOfItems = tk.Scrollbar(root)
        listOfItems.place(x=330,y=470,width=20,height=200)

        myList = tk.Listbox(root, yscrollcommand = listOfItems.set,selectmode=tk.SINGLE)

        myList.place(x=60,y=470,width=270,height=200)
        for listing in biddingHistory:
            myList.insert(tk.ANCHOR,listing)
        '''


    def GButton_578_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        resultsScreen(root, self.usr)


    def GButton_644_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)


    def GButton_25_command(self):
        global username
        for widget in root.winfo_children():
            if "entry" in str(widget):
                msg = placeBid(widget.get(),self.listOfInfo[0],username, int(self.listOfInfo[-1]))
                break

        GLabel_19=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=12)
        GLabel_19['bg'] = "#FFFFFF"
        GLabel_19["font"] = ft
        GLabel_19["justify"] = "center"
        GLabel_19["text"] = msg[0]
        GLabel_19["fg"] = msg[1]
        GLabel_19.place(x=652,y=425,width=625,height=35)

        if(msg[1]=="#00AB00"): # If green then reload
            for widget in root.winfo_children():
                if "treeview" in str(widget) or "scrollbar" in str(widget):
                    widget.destroy()

            self.biddingHistory = GetInformationAboutListing(self.listOfInfo[0])[-2].split("|")

            listOfItems = ttk.Scrollbar(root)
            listOfItems.place(x=330,y=470,width=20,height=200)
            myList = ttk.Treeview(root, selectmode="browse",yscrollcommand=listOfItems.set)

            myList.heading("#0", text="Bid History", anchor='center')
            myList.column("#0",anchor= "center")
            myList.place(x=60,y=470,width=270,height=200)
            for bid in reversed(self.biddingHistory):
                myList.insert(parent="", index='end', text=bid)


class Sell:
    def __init__(self, root):
        #setting title
        root.title("Auction Sell Setup")

        #setting window size

        ft = tkFont.Font(family='Cambria',size=10)
        ttk.Style().configure('TButton',font = ft)

        #Logout
        GButton_791=ttk.Button(root)
        GButton_791["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_791["font"] = ft
        #GButton_791["fg"] = "#000000"
        #GButton_791["justify"] = "center"
        GButton_791["text"] = "Logout"
        GButton_791.place(x=10,y=10,width=120,height=34)
        GButton_791["command"] = self.GButton_791_command

        #Set up Auction Text
        GLabel_367=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=43)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "Setup Your Auction"
        GLabel_367.place(x=320,y=30,width=679,height=99)

        #Entry for Name of Object
        GLineEdit_17=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLineEdit_17["font"] = ft
        GLineEdit_17["background"]="#ffffff"
        GLineEdit_17["foreground"] = "#000000"
        GLineEdit_17["justify"] = "center"
        GLineEdit_17.place(x=360,y=140,width=600,height=55)


        #Text Name of Object
        GLabel_573=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "center"
        GLabel_573["text"] = "Name of Object:"
        GLabel_573.place(x=110,y=140,width=250,height=40)

        #Back Button
        GButton_282=ttk.Button(root)
        GButton_282["style"] = "TButton"
        #ft = tkFont.Font(family='Cambria',size=10)
        #GButton_282["font"] = ft
        #GButton_282["fg"] = "#000000"
        #GButton_282["justify"] = "center"
        GButton_282["text"] = "Back"
        GButton_282.place(x=1150,y=10,width=120,height=35)
        GButton_282["command"] = self.GButton_282_command

        ft = tkFont.Font(family='Cambria',size=18)
        ttk.Style().configure('Accentbutton',font = ft)

        #Confirm Button
        GButton_245=ttk.Button(root)
        GButton_245["style"] = "Accentbutton"
        #ft = tkFont.Font(family='Cambria',size=30)
        #GButton_245["font"] = ft
        #GButton_245["fg"] = "#000000"
        #GButton_245["justify"] = "center"
        GButton_245["text"] = "Confirm"
        GButton_245.place(x=540,y=590,width=190,height=65)
        GButton_245["command"] = self.GButton_245_command

        #Description Text
        GLabel_334=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_334["font"] = ft
        GLabel_334["fg"] = "#333333"
        GLabel_334["justify"] = "center"
        GLabel_334["text"] = "Description:"
        GLabel_334.place(x=110,y=220,width=250,height=40)

        #Prices Text
        GLabel_80=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_80["font"] = ft
        GLabel_80["fg"] = "#333333"
        GLabel_80["justify"] = "center"
        GLabel_80["text"] = "Prices:"
        GLabel_80.place(x=110,y=350,width=250,height=40)

        #End Date Text
        GLabel_806=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_806["font"] = ft
        GLabel_806["fg"] = "#333333"
        GLabel_806["justify"] = "center"
        GLabel_806["text"] = "End Date:"
        GLabel_806.place(x=110,y=430,width=250,height=40)

        #Entry For Description
        GLineEdit_638=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLineEdit_638["font"] = ft
        GLineEdit_638["background"]="#ffffff"
        GLineEdit_638["foreground"] = "#000000"
        GLineEdit_638["justify"] = "center"
        GLineEdit_638.place(x=360,y=220,width=600,height=100)

        #Entry For Staring Price
        GLineEdit_685=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_685["font"] = ft
        GLineEdit_685["background"]="#ffffff"
        GLineEdit_685["foreground"] = "#000000"
        GLineEdit_685["justify"] = "center"
        GLineEdit_685.place(x=360,y=350,width=275,height=40)

        #Entry For Buy Out Price
        GLineEdit_125=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=20)
        GLineEdit_125["font"] = ft
        GLineEdit_125["background"]="#ffffff"
        GLineEdit_125["foreground"] = "#000000"
        GLineEdit_125["justify"] = "center"
        GLineEdit_125.place(x=680,y=350,width=275,height=40)


        #Starting Text
        GLabel_377=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=14)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Starting"
        GLabel_377.place(x=460,y=390,width=70,height=25)

        #Buy Out Text
        GLabel_700=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=14)
        GLabel_700["font"] = ft
        GLabel_700["fg"] = "#333333"
        GLabel_700["justify"] = "center"
        GLabel_700["text"] = "Buy-Out "
        GLabel_700.place(x=780,y=390,width=70,height=25)

        #Entry for End Date

        GLineEdit_611=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLineEdit_611["font"] = ft
        GLineEdit_611["background"]="#ffffff"
        GLineEdit_611["foreground"] = "#000000"
        GLineEdit_611["justify"] = "center"
        GLineEdit_611.place(x=360,y=430,width=600,height=55)

        #Image Upload Text
        GLabel_590=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_590["font"] = ft
        GLabel_590["fg"] = "#333333"
        GLabel_590["justify"] = "center"
        GLabel_590["text"] = "Image Upload"
        GLabel_590.place(x=100,y=520,width=250,height=40)

        GLineEdit_621=ttk.Entry(root)
        ft = tkFont.Font(family='Cambria',size=24)
        GLineEdit_621["font"] = ft
        GLineEdit_621["background"]="#ffffff"
        GLineEdit_621["foreground"] = "#000000"
        GLineEdit_621["justify"] = "center"
        GLineEdit_621.place(x=360,y=525,width=600,height=55)

    def GButton_791_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        loginScreen(root)


    def GButton_282_command(self):
        for widget in root.winfo_children():
            widget.destroy()
        selectionScreen(root)


    def GButton_245_command(self):
        from time import sleep
        global username
        from Helpers import CreateAuction
        widgets = root.winfo_children() # this command returns a list of each widget
        saleInfo = ['', '', '', '', '', '', '', '']

        saleInfo[0] = widgets[2].get()
        saleInfo[1] = widgets[9].get()
        saleInfo[3] = widgets[10].get()
        saleInfo[7] = widgets[11].get()
        saleInfo[4] = widgets[14].get()
        saleInfo[5] = username
        saleInfo[2] = widgets[16].get()
        CreateAuction(saleInfo)
        GLabel_313=tk.Label(root)
        ft = tkFont.Font(family='Cambria',size=22)
        GLabel_313["font"] = ft
        GLabel_313["fg"] = "#00FF00"
        GLabel_313["justify"] = "center"
        GLabel_313["text"] = "Done!"
        GLabel_313.place(x=515,y=650,width=250,height=40)
        GButton_245=tk.Label(root)
        GButton_245.destroy() 
        sleep(1)
        for widget in root.winfo_children():
            widget.destroy()
        selectionScreen(root)


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    root.tk.call('source', 'azure/azure.tcl')
    style.theme_use('azure')
    app = loginScreen(root)
    width=1280
    height=720
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.configure(bg="White")
    root.resizable(width=False, height=False)
    root.mainloop()