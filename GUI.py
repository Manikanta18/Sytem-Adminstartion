from tkinter import *
from tkinter import ttk,filedialog
from tkinter.colorchooser import *
import tkinter.messagebox as messageBox
from tkinter import simpledialog
import subprocess
import os
import pandas as pd
import crypt, getpass


root = Tk()
root.title("System Admin")
root.configure(bg='light grey')
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Assignment 3')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Assignment 4-SingleUser')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Assignment 4-BatchMode')

tabControl.pack(expand=1, fill="both")

#fonts
headlabelfont = ('times', 18, 'bold')
framelabelfont = ('times', 11)
commandsfont = ('times', 11)

#images
shutdown=PhotoImage(file="st2.png")
ubuntu=PhotoImage(file="ubuntu.png")
grub=PhotoImage(file="Grub_logo.png")
stop=PhotoImage(file="stop.png")
swap=PhotoImage(file="swap.png")
install=PhotoImage(file="install.png")
user_pic=PhotoImage(file="user.png")
batch_pic=PhotoImage(file="batch.png")


############## Assignment 3 ########################

#questions
Question1 = """Change the order of OS's
shown in the GRUB."""
Question2 = """Change the time-out period
(usually 10 seconds) shown in the GRUB."""
Question3 = """Change the default behavior of
shutdown & reboot buttons to do
the opposite activities and vice versa"""
Question4 = """Customize the Ubuntu’s
boot splash screen and logo."""
Question5 = """BURG configuration/installation
and document the process."""
Question6 = """Automatically shutdown/reboot/etc.
your machine."""

#documentaion of BURG
l11 = """First, add BURG boot loader PPA """
l1 = """sudo add-apt-repository ppa:n-muench/burg """
l22 = """Update the sources list: """
l2 = """sudo apt-get update """
l33 = """Then, install burg boot loader and its themes, run: """
l3 = """sudo apt-get install burg burg-themes """
l44 = """Once the BURG boot loader installation is finished,
run the following command to update boot configuration
and create burg.cfg file. """
l4 = """sudo update-burg """
l55 = """Finally, reboot your system to use
BURG boot loader. """
l5 = """sudo reboot """

#variables
entryb1 = StringVar()
name = StringVar()
entryb2 = StringVar()
name2 = StringVar()
os_name = StringVar()
time_value = IntVar()

new_name = StringVar()
new_pwd = StringVar()
new_uid = StringVar()
new_shell = StringVar()

#Login
NLabel = Label(root,bd=4, text = "User Name", relief = RIDGE)
NLabel.place(x = 190, y = 38)
Name = Entry(root, textvariable=name, bd=4)
Name.place(x = 280, y = 38)
ELabel = Label(root,bd=4, text = "Password", relief = RIDGE)
ELabel.place(x = 472, y = 38)
E = Entry(root, textvariable=entryb1,show = "*", bd=4)
E.place(x = 550, y = 38)
b1 = Button(root, text="Login",bd=3,command= lambda: hideThis(Name,E, NLabel,ELabel) if entryb1.get()!= '' and name.get() != '' else messageBox.showwarning("WARNING", "Enter Login Details") )
b1.place(x = 740, y = 38)

# NLabel2 = Label(tab2,bd=4, text = "User Name", relief = RIDGE)
# NLabel2.place(x = 190, y = 25)
# Name2 = Entry(tab2, textvariable=name2, bd=4)
# Name2.place(x = 280, y = 25)
# ELabel2 = Label(tab2,bd=4, text = "Password", relief = RIDGE)
# ELabel2.place(x = 472, y = 25)
# E2 = Entry(tab2, textvariable=entryb2,show = "*", bd=4)
# E2.place(x = 550, y = 25)
# b2 = Button(tab2, text="Login",bd=3,command= lambda: hideThis2(Name2,E2, NLabel2,ELabel2) if entryb2.get()!= '' and name2.get() != '' else messageBox.showwarning("WARNING", "Enter Login Details") )
# b2.place(x = 740, y = 25)

#headFrame
headFrame = Frame(tab1, bg="tan3", bd=8, relief = RIDGE)
headFrame.place(x = 30, y = 60, width=775, height=50)
headFrame_Label = Label(headFrame, text=" Assignment 3 ", relief = SUNKEN,bd = 4)
headFrame_Label.config(font=headlabelfont)
headFrame_Label.pack(expand=YES)


#After login
def hideThis(Name,E,NLabel,ELabel):
    global entryb1
    global name
    content = entryb1.get()
    user = name.get()
    print(user)
    print(content)
    NLabel.place_forget()
    Name.place_forget()
    ELabel.place_forget()
    E.place_forget()
    b1.place_forget()
    newLabel = Label(root, text="Hi, "+user+" !",relief = RAISED,padx =10, pady=6,bd =4, bg="cyan3")
    newLabel.place(x = 630, y = 38, width = 175)


# #After login
# def hideThis2(Name2,E2,NLabel2,ELabel2):
#     global entryb2
#     global name2
#     content2 = entryb2.get()
#     user2 = name2.get()
#     print(user2)
#     print(content2)
#     NLabel2.place_forget()
#     Name2.place_forget()
#     ELabel2.place_forget()
#     E2.place_forget()
#     b2.place_forget()
#     newLabel2 = Label(tab2, text="Hi, "+user2+" !",relief = RAISED,padx =10, pady=6,bd =4, bg="cyan3")
#     newLabel2.place(x = 630, y = 22, width = 175)

#-----------------QUESTION1--------------------------------


def linux():
    global entryb1
    pwd = entryb1.get()
    if pwd != '':
        print("this is linux")
        cmd = "echo \""+pwd+"\" | sudo -S sed -i \"s/GRUB_DEFAULT=[0-9]*/GRUB_DEFAULT=0/g\" \"/etc/default/grub\""
        subprocess.call(cmd, shell=True)
        subprocess.call(['sudo', 'update-grub'])
        messageBox.showinfo("GRUB_DEFAULT", "Successfully changed")
    else:
        messageBox.showwarning("WARNING", "Login Required")


def windows():
    global entryb1
    pwd = entryb1.get()
    if pwd != '':
        print("this is windows")
        cmd = "echo \""+pwd+"\" | sudo -S sed -i \"s/GRUB_DEFAULT=[0-9]*/GRUB_DEFAULT=2/g\" \"/etc/default/grub\""
        subprocess.call(cmd, shell=True)
        subprocess.call(['sudo', 'update-grub'])
        messageBox.showinfo("GRUB_DEFAULT", "Successfully changed")
    else:
        messageBox.showwarning("WARNING", "Login Required")


def change_os():
    global os_name
    os_value = os_name.get()
    print("change_os" + os_value)
    if os_value != '':
        if os_value =='Ubuntu':
            linux()
        elif os_value == 'Windows':
            windows()
        else:
            print("error in selection")
    else:
        messageBox.showwarning("OS Order", "Choose OS to change")


# on change dropdown value
def change_dropdown(*args):
    print( os_name.get() )

# link function to change dropdown
os_name.trace('w', change_dropdown)

firstFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
firstFrame.place(x = 30, y = 150, width=370, height=150)
firstFrame_Label = Label(firstFrame, text=Question1, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
firstFrame_Label.config(font=framelabelfont)
firstFrame_Label.place(width=260, height=70)
firstFrame_Label2 = Label(firstFrame, image=grub).pack(side="right")
os_name.set('-Select-')
choices = {'Ubuntu','Windows'}
DropDown1 = OptionMenu(tab1, os_name, *choices)
DropDown1.place(x=55,y=255)

Button1 = Button(tab1, text="Change", fg="black", bg="snow", command=change_os, bd=3)
Button1.place(x=170,y=255)

#-----------------QUESTION2--------------------------------


def grub_time():
    global entryb1
    global time_value
    pwd = entryb1.get()
    t = str(time_value.get())
    if t != '0':
        if pwd != '':
            print("this is GRUB_TIMEOUT")
            cmd = "echo \""+pwd+"\" | sudo -S sed -i \"s/GRUB_TIMEOUT=[0-9]*/GRUB_TIMEOUT="+t+"/g\" \"/etc/default/grub\""
            subprocess.call(cmd, shell=True)
            subprocess.call(['sudo', 'update-grub'])
            messageBox.showinfo("GRUB_TIMEOUT", "Successfully changed")
        else:
            messageBox.showwarning("WARNING", "Login Required")
    else:
        messageBox.showwarning("WARNING", "Enter Time")

secondFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
secondFrame.place(x = 435, y = 150, width=370, height=150)
secondFrame_Label2 = Label(secondFrame, image=stop).pack(side="right")
secondFrame_Label = Label(secondFrame, text=Question2, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
secondFrame_Label.config(font=framelabelfont)
secondFrame_Label.place(width=260, height=70)

TimeEntry = Entry(tab1, textvariable=time_value, bd=4, bg="light grey")
TimeEntry.place(x = 470, y = 255, width=60, height=30)

Button2 = Button(tab1, text="Change", fg="black", bg="white", bd=3, command=grub_time)
Button2.place(x=550,y=255)

#-----------------QUESTION3--------------------------------

#mkdir temp
#mv -v ~/Desktop/first/* ~/Desktop/temp
#rm -r temp

thirdFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
thirdFrame.place(x = 30, y = 330 , width=370, height=150)
thirdFrame_Label = Label(thirdFrame, text=Question3, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
thirdFrame_Label.config(font=framelabelfont)
thirdFrame_Label.place(width=270, height=70)
thirdFrame_Label2 = Label(thirdFrame, image=swap).pack(side="right")

Button3 = Button(thirdFrame, text="Change", fg="black", bg="white", bd=3)
Button3.pack(side=BOTTOM)

#-----------------QUESTION4 --------------------------------

#sudo cp /home/manikanta/Pictures/.jpg /boot/grub/
#cd /boot/grub/
#sudo rm *.jpg

# def select_image():
#     global entryb1
#     pwd = entryb1.get()
#     filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Picture",filetypes = (("jpg files","*.jpg"),("jpeg files","*.jpeg"),("PNG files","*.png"),("all files","*.*")))
#     print(filename)
#     if filename != '':
#         if pwd != '':
#             cmd2 = "echo \""+pwd+"\" | sudo -S rm /boot/grub/*.jpg /boot/grub/*.png /boot/grub/*.jpeg"
#             subprocess.call(cmd2, shell=True)
#
#             cmd3 = "sudo cp "+filename+" /boot/grub/"
#             subprocess.call(cmd3, shell=True)
#             subprocess.call(['sudo', 'update-grub'])
#             messageBox.showinfo("Ubuntu’s boot splash screen and logo", "Successfully changed")
#         else:
#             messageBox.showwarning("WARNING", "Login Required")
#     else:
#         messageBox.showwarning("WARNING", "Image not selected")

#/usr/share/plymouth/themes/ubuntu-logo
#sudo update-initramfs -u


def splash_screen():
    global entryb1
    pwd = entryb1.get()
    if pwd != '':
        color = askcolor(color="#dd4814")
        newlist = list(color[0])
        colorList = []
        for a in newlist:
            a = float(a) / 255
            colorList.append(round(a,2))

        color_tuple = tuple(colorList)
        new_color= str(color_tuple)
        print(new_color)
        cmd = "echo \""+pwd+"\" | sudo -S sed -i \"s/^Window.SetBackgroundTopColor .*$/Window.SetBackgroundTopColor "+new_color+";     # Nice colour on top of the screen fading to/g\" \"/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script\""
        cmd2 = "echo \""+pwd+"\" | sudo -S sed -i \"s/^Window.SetBackgroundBottomColor .*$/Window.SetBackgroundBottomColor "+new_color+";     # an equally nice colour on the bottom/g\" \"/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script\""
        print(cmd)
        subprocess.call(cmd, shell=True)
        subprocess.call(cmd2, shell=True)
        subprocess.call(['sudo', 'update-initramfs', '-u'])
        messageBox.showinfo("splash_screen", "Successfully changed")
    else:
        messageBox.showwarning("WARNING", "Login Required")

#sudo cp /home/manikanta/Pictures/logos/mkLogo2.png  /usr/share/plymouth/themes/ubuntu-logo
# echo "mani8996" | sudo -S sed -i 's/logo_filename = .*$"/logo_filename = "mkLogo.png"/' /usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script


def splash_logo():
    global entryb1
    pwd = entryb1.get()
    filename =  filedialog.askopenfilename(initialdir = "/home",title = "Select Picture",filetypes = (("PNG files","*.png"),("all files","*.*")))
    image_name = os.path.basename(filename)
    print(filename)
    print(image_name)
    print(filename)
    if filename != '':
        if pwd != '':
            cmd = "echo \""+pwd+"\" | sudo -S cp "+filename+" /usr/share/plymouth/themes/ubuntu-logo"
            cmd2 = "echo \""+pwd+"\" | sudo -S sed -i \'s/logo_filename = .*\"/logo_filename = \""+image_name+"\"/\' /usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script"
            print(cmd2)
            subprocess.call(cmd, shell=True)
            subprocess.call(cmd2, shell=True)
            subprocess.call(['sudo', 'update-initramfs', '-u'])
            messageBox.showinfo("Ubuntu’s boot splash screen and logo", "Successfully changed")
        else:
            messageBox.showwarning("WARNING", "Login Required")
    else:
        messageBox.showwarning("WARNING", "Image not selected")

fourthFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
fourthFrame.place(x = 435, y = 330 , width=370, height=150)
fourthFrame_Label2 = Label(fourthFrame, image=ubuntu).pack(side="right")
fourthFrame_Label = Label(fourthFrame, text=Question4, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
fourthFrame_Label.config(font=framelabelfont)
fourthFrame_Label.place(width=260, height=70)

Button4 = Button(tab1, text="Splash screen", fg="black", bg="white", bd=3, command=splash_screen)
Button4.place(x=470,y=435)
Button41 = Button(tab1, text="Splash logo", fg="black", bg="white", bd=3, command=splash_logo)
Button41.place(x=605,y=435)

#-----------------QUESTION5--------------------------------


def read():
    popup = Tk()
    popup.wm_title("documentaion of BURG")
    popupFrame = Frame(popup, bg="ivory2", bd = 10)
    popupFrame.place( width=820, height=500)
    line00 = Label(popupFrame, text=" INSTRUCTIONS", relief = RIDGE, pady=10, padx=10, bg="OrangeRed2",bd = 6)
    line00.place(x=20, y=10, width=400, height=40)
    line00.config(font=commandsfont)
    line0 = Label(popupFrame, text=" COMMANDS", relief = RIDGE, pady=10, padx=10, bg="OrangeRed2",bd = 6)
    line0.place(x=430, y=10, width=350, height=40)
    line0.config(font=commandsfont)
    line11 = Label(popupFrame, text=l11, relief = RIDGE, pady=10, padx=10, bg="wheat3")
    line11.place(x=20, y=60, width=400, height=40)
    line1 = Label(popupFrame, text=l1, relief = SUNKEN, pady=10, padx=10, bd = 3)
    line1.place(x=430, y=60, width=350, height=40)
    line1.config(font=commandsfont)
    line22 = Label(popupFrame, text=l22, relief = RIDGE, justify=LEFT, pady=10, padx=10, bg="wheat3")
    line22.place(x=20, y=110, width=400, height=40)
    line2 = Label(popupFrame, text=l2, relief = SUNKEN, pady=10, padx=10, bd = 3)
    line2.place(x=430, y=110, width=350, height=40)
    line2.config(font=commandsfont)
    line33 = Label(popupFrame, text=l33, justify=LEFT, relief = RIDGE, pady=10, padx=10, bg="wheat3")
    line33.place(x=20, y=160, width=400, height=40)
    line3 = Label(popupFrame, text=l3, relief = SUNKEN, pady=10, padx=10, bd = 3)
    line3.place(x=430, y=160, width=350, height=40)
    line3.config(font=commandsfont)
    line44 = Label(popupFrame, text=l44, justify=LEFT, relief = RIDGE, pady=10, padx=10, bg="wheat3")
    line44.place(x=20, y=210, width=400, height=70)
    line4 = Label(popupFrame, text=l4, relief = SUNKEN, pady=10, padx=10, bd = 3)
    line4.place(x=430, y=210, width=350, height=70)
    line4.config(font=commandsfont)
    line55 = Label(popupFrame, text=l55,relief = RIDGE, pady=10, padx=10, bg="wheat3")
    line55.place(x=20, y=290, width=400, height=50)
    line5 = Label(popupFrame, text=l5, relief = SUNKEN, pady=10, padx=10, bd = 3)
    line5.place(x=430, y=290, width=350, height=50)
    line5.config(font=commandsfont)
    popup.minsize(820, 390)
    popup.resizable(0, 0)
    popup.mainloop()

fifthFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
fifthFrame.place(x = 30, y = 510, width=370, height=150)
fifthFrame_Label2 = Label(fifthFrame, image=install).pack(side="right")
fifthFrame_Label = Label(fifthFrame, text=Question5, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
fifthFrame_Label.config(font=framelabelfont)
fifthFrame_Label.place(width=260, height=70)

Button5 = Button(fifthFrame, text="Read", fg="black", bg="white", command=read, bd=3)
Button5.pack(side=BOTTOM)

#----------------------Question6-------------------------


#shutdown Counter
counter = 60
def counterStdwn_label(label):
    def count():
        global counter
        counter = counter-1
        label.config(text="Your system Shutdowns in "+str(counter))
        label.after(1000, count)
    count()


#retsrt counter
counter2 = 60
def counterRstrt_label(label):
    def count():
        global counter2
        counter2 = counter2-1
        if counter2 > 0:
            label.config(text="Your system Restarts in "+str(counter2))
            label.after(1000, count)
    count()


#shutdown
def stDwn():
    popup = Tk()
    popup.wm_title("Shutdown")
    popup.config(bg = "brown2")
    label = ttk.Label(popup)
    label.pack(anchor="center",side="left",expand=YES)
    counterStdwn_label(label)
    # subprocess.call(["shutdown", "-h", "+1"])
    # B1 = ttk.Button(popup, text="stop", command=subprocess.call(["shutdown", "-c"]))
    # B1.pack(side="bottom")
    popup.minsize(300, 100)
    popup.resizable(0, 0)
    popup.mainloop()


#Restart
def rstrt():
    popup = Tk()
    popup.wm_title("Restart")
    popup.config(bg = "light goldenrod")
    label = ttk.Label(popup)
    label.pack(anchor="center",side="left", expand=YES)
    counterRstrt_label(label)
    subprocess.call(["shutdown", "-r", "+1"])
    popup.minsize(300, 100)
    popup.resizable(0, 0)
    popup.mainloop()


sixthFrame = Frame(tab1, bg="steel blue", bd = 8, relief = RIDGE)
sixthFrame.place(x = 435, y = 510, width=370, height=150)
sixthFrame_Lable2 = Label(sixthFrame, image=shutdown).pack(side="right")
sixthFrame_Label = Label(sixthFrame, text=Question6, justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
sixthFrame_Label.config(font=framelabelfont)
sixthFrame_Label.place(width=260, height=70)

Button7 = Button(sixthFrame, text="reboot", fg="black", bg="chartreuse3", command=rstrt, bd=3)
Button7.pack(side=LEFT, anchor = SW)
Button6 = Button(sixthFrame, text="Shutdown", fg="white", bg="red2", command=stDwn, bd=3)
Button6.pack(side=LEFT, anchor = SW)


############## Assignment 4 part1 ########################


#headFrame
headFrame2 = Frame(tab2, bg="tan3", bd=8, relief = RIDGE)
headFrame2.place(x = 30, y = 60, width=775, height=50)
headFrame_Label2 = Label(headFrame2, text=" Assignment 4 ", relief = SUNKEN,bd = 4)
headFrame_Label2.config(font=headlabelfont)
headFrame_Label2.pack(expand=YES)


# on change dropdown value
def change_dropdown2(*args):
    print( new_shell.get() )


# link function to change dropdown
new_shell.trace('w', change_dropdown2)


def addSingleUser():
    global entryb1
    pwd = entryb1.get()

    if pwd != '':
        user_name = new_name.get()
        user_pwd = crypt.crypt(str(new_pwd.get()), crypt.mksalt(crypt.METHOD_SHA512))
        # user_pwd = new_pwd.get()
        user_id = new_uid.get()
        user_shell = new_shell.get()
        print(user_name,user_pwd,user_id,user_shell)

        if user_name != '' and  user_pwd != '' and user_id != '' and user_shell != '':
            cmd1 = "echo \""+pwd+"\" | sudo -S groupadd -g \""+user_id+"\" \""+user_name+"\""
            cmd2 = "sudo useradd -m \""+user_name+"\" -p \""+user_pwd+"\" -u \""+user_id+"\" -g \""+user_id+"\" -s \""+user_shell+"\""
            print(cmd1)
            print(cmd2)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
            messageBox.showinfo("Add User", "Successfully Added")
        else:
            messageBox.showwarning("WARNING", "Fill User Details")

    else:
        messageBox.showwarning("WARNING", "Login Required")


#delete User
def del_user():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Delete USER","Enter Username ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S userdel -r \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Delete User", "Successfully Deleted")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Username")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#lock User
def lock_user():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Lock USER","Enter Username ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S usermod -L \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Lock User", "Successfully Locked")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Username")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#unlock User
def unlock_user():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Unlock USER","Enter Username ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S usermod --unlock \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Unlock User", "Successfully Unlocked")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Username")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update username
def update_username():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Update Username","Enter Username ",parent=tab2)
        new_username = simpledialog.askstring("Update Username","Enter New Username ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S usermod -l \""+new_username+"\" \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Update Username", "Successfully Updated Username")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Username")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's Shell
def update_usershell():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Update user's shell","Enter Username ",parent=tab2)
        user_sh = simpledialog.askstring("Update user's shell","Enter new Usershell ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S usermod -s \""+user_sh+"\" \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Update User's Shell", "Successfully Updated User's Shell")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter User's shell")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's uid
def update_userUID():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Update user's UID","Enter Username ",parent=tab2)
        user_uid = simpledialog.askstring("Update user's UID","Enter new UID ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S usermod -u \""+user_uid+"\" \""+username+"\""
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            messageBox.showinfo("Update User's UID", "Successfully Updated User's UID")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter User's UID")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's gid
def update_userGID():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Update user's GID","Enter Username ",parent=tab2)
        user_gid = simpledialog.askstring("Update user's GID","Enter new GID ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S groupmod -g \""+user_gid+"\" \""+username+"\""
            cmd2 = "echo \""+pwd+"\" | sudo -S usermod -g \""+user_gid+"\" \""+username+"\""
            print(cmd2)
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
            messageBox.showinfo("Update User's GID", "Successfully Updated User's GID")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter User's GID")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's homedir
def update_homedir():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Update user's Home Dir","Enter Username ",parent=tab2)
        user_dir = simpledialog.askstring("Update user's Home Dir","Enter new User's Home Dir ",parent=tab2)

        if username != "":
            cmd1 = "echo \""+pwd+"\" | sudo -S mkdir -p \""+user_dir+"\""
            cmd2 = "echo \""+pwd+"\" | sudo -S usermod -d \""+user_dir+"\" \""+username+"\""
            print(cmd2)
            print(cmd1)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
            messageBox.showinfo("Update User's Home Dir", "Successfully Updated User's Home Dir")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter User's Home Dir")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#set Expiry Date
def setExd():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Set Expiry Date","Enter Username ",parent=tab2)
        user_exd = simpledialog.askstring("Set Expiry Date","Enter Expiry Date ",parent=tab2)

        if username != "":
            cmd = "echo \""+pwd+"\" | sudo -S usermod -e \""+user_exd+"\" \""+username+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
            messageBox.showinfo("Set Expiry Date", "Successfully Updated Expiry Date")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Expiry Date")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#Change Password
def setPwd():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)
    if pwd != "":
        username = simpledialog.askstring("Change Password","Enter Username ",parent=tab2)
        user_pxd = simpledialog.askstring("Change Password","Enter Password ",parent=tab2)
        e_pwd = crypt.crypt(str(user_pxd), crypt.mksalt(crypt.METHOD_SHA512))

        if username != "":
            cmd = "echo \""+pwd+"\" | sudo -S usermod -p \""+e_pwd+"\" \""+username+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
            messageBox.showinfo("Change Password", "Successfully Updated Expiry Date")
            print("done")
        else:
            messageBox.showwarning("WARNING", "Enter Password")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#single User
seventhFrame = Frame(tab2, bg="steel blue", bd = 8, relief = RIDGE)
seventhFrame.place(x = 30, y = 150, width=775, height=300)
seventhFrameLable2 = Label(seventhFrame, image=user_pic).pack(side="left")
seventhFrameLabel = Label(seventhFrame, text="Single User Mode:   CREATE USER", justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
seventhFrameLabel.config(font=framelabelfont)
seventhFrameLabel.place(x=200,y=2,width=545, height=50)

userLabel = Label(seventhFrame,bd=4, text = "User Name", relief = RIDGE, pady=3)
userLabel.place(x = 270, y = 70, width=230)
userEntry = Entry(seventhFrame, textvariable=new_name, bd=4)
userEntry.place(x = 500, y = 70, width=230)
pwdLabel = Label(seventhFrame,bd=4, text = "Password", relief = RIDGE, pady=3)
pwdLabel.place(x = 270, y = 115, width=230)
pwdEntry = Entry(seventhFrame, textvariable=new_pwd,show = "*", bd=4)
pwdEntry.place(x = 500, y = 115, width=230)
uidLabel = Label(seventhFrame,bd=4, text = "User ID", relief = RIDGE, pady=3)
uidLabel.place(x = 270, y = 160, width=230)
uidEntry = Entry(seventhFrame, textvariable=new_uid, bd=4)
uidEntry.place(x = 500, y = 160, width=230)
shellLabel = Label(seventhFrame,bd=4, text = "User's login shell", relief = RIDGE, pady=3)
shellLabel.place(x = 270, y = 205, width=230)
# shellEntry = Entry(seventhframe, textvariable=new_shell, bd=4)
# shellEntry.place(x = 500, y = 205, width=230)
new_shell.set('-Select-')
choices2 = {'/bin/bash','/bin/sh'}
DropDown2 = OptionMenu(seventhFrame, new_shell, *choices2)
DropDown2.place(x = 505, y = 205, width=220)
Button8 = Button(seventhFrame, text="Create", fg="black", bg="white", bd=3, command=addSingleUser)
Button8.place(x = 450, y = 250, width=100)

ninthFrame = Frame(tab2, bg="steel blue", bd = 8, relief = RIDGE)
ninthFrame.place(x = 30, y = 480, width=775, height=220)
ninthFrameLabel = Label(tab2, text="Single User Management Operations", justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
ninthFrameLabel.place(x=40,y=490,width=754, height=45)

Btn81 = Button(tab2, text="Delete User", fg="white", bg="red2", bd=3,command=del_user).place(x = 60, y = 560, width=100)
Btn82 = Button(tab2, text="Lock User", fg="white", bg="tomato", bd=3, command=lock_user).place(x = 60, y = 630, width=100)
Btn83 = Button(tab2, text="Update Username", fg="black", bg="white", bd=3, command=update_username).place(x = 180, y = 560, width=140)
Btn84 = Button(tab2, text="Update Password", fg="black", bg="white", bd=3, command=setPwd).place(x = 180, y = 630, width=140)
Btn85 = Button(tab2, text="Update User's Shell", fg="black", bg="white", bd=3, command=update_usershell).place(x = 340, y = 560, width=160)
Btn86 = Button(tab2, text="Set Expiry Date", fg="black", bg="white", bd=3,command=setExd).place(x = 340, y = 630, width=160)
Btn87 = Button(tab2, text="Update UID", fg="black", bg="white", bd=3,command=update_userUID).place(x = 520, y = 560, width=100)
Btn88 = Button(tab2, text="Update GID", fg="black", bg="white", bd=3,command=update_userGID).place(x = 520, y = 630, width=100)
Btn89 = Button(tab2, text="Change Home Dir", fg="black", bg="white", bd=3,command=update_homedir).place(x = 640, y = 560, width=140)
Btn810 = Button(tab2, text="Unlock User", fg="black", bg="pale green", bd=3, command=unlock_user).place(x = 640, y = 630, width=140)


############## Assignment 4 part2 ########################


#headFrame
headFrame3 = Frame(tab3, bg="tan3", bd=8, relief = RIDGE)
headFrame3.place(x = 30, y = 60, width=775, height=50)
headFrame_Label3 = Label(headFrame3, text=" Assignment 4 ", relief = SUNKEN,bd = 4)
headFrame_Label3.config(font=headlabelfont)
headFrame_Label3.pack(expand=YES)


csv_filename =""

def uploadCSV():
    global csv_filename
    csv_filename =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    print(csv_filename)
    if str(csv_filename) != "":
        messageBox.showinfo("Add csv", "Successfully Added")
    else:
        messageBox.showwarning("WARNING", "upload csv file required")


def batchMode():
    global csv_filename
    data = pd.read_csv(csv_filename)
    df = pd.DataFrame(data)

    matrix =[]
    username = []
    uid = []
    pswd = []
    shll = []

    for row in df.iterrows():
        matrix.append(row)

    range_lenth = len(matrix)

    for i in range(0,range_lenth):
        username.append(matrix[i][1][0])
        uid.append(str(matrix[i][1][1]))
        #encrypting password
        pswd.append(crypt.crypt(str(matrix[i][1][2]), crypt.mksalt(crypt.METHOD_SHA512)))
        shll.append(matrix[i][1][3])

    global entryb1
    pwd = entryb1.get()

    if pwd != '':
        for i in range(0,range_lenth):
            cmd1 = "echo \""+pwd+"\" | sudo -S groupadd -g \""+uid[i]+"\" \""+username[i]+"\""
            print(cmd1)
            cmd2 = "sudo useradd -m \""+username[i]+"\" -p \""+pswd[i]+"\" -u \""+uid[i]+"\" -g \""+uid[i]+"\" -s \""+shll[i]+"\""
            print(cmd2)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
        messageBox.showinfo("Add Users", "Successfully Added")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#delete User
def del_users_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userdel_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userdel_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S userdel -r \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Delete Users", "Successfully deleted Users")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#lock User
def lock_users_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userlock_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userlock_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -L \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Lock Users", "Successfully Locked Users")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#unlock User
def unlock_user_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userunlock_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userunlock_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod --unlock \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Unock Users", "Successfully unlocked Users")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update username
def update_username_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userdel_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userdel_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        update_name = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            update_name.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -l \""+update_name[i]+"\" \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Update Usernames", "Successfully Updated Usernames")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's Shell
def update_usershell_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != "":
        usershl_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(usershl_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        update_shell = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            update_shell.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -s \""+update_shell[i]+"\" \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Update User's Shells", "Successfully Updated User's Shells")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's uid
def update_userUID_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != "":
        useruid_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(useruid_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        update_uid = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            update_uid.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -u \""+update_uid[i]+"\" \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Update User's UIDs", "Successfully Updated User's UIDs")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's gid
def update_userGID_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != "":
        usergid_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(usergid_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        update_gid = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            update_gid.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd1 = "echo \""+pwd+"\" | sudo -S groupmod -g \""+update_gid[i]+"\" \""+username[i]+"\""
            cmd2 = "echo \""+pwd+"\" | sudo -S usermod -g \""+update_gid[i]+"\" \""+username[i]+"\""
            print(cmd1)
            print(cmd2)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
        print("done")
        messageBox.showinfo("Update User's GIDs", "Successfully Updated User's GIDs")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#update user's homedir
def update_homedir_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != "":
        userdir_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userdir_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        update_dir = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            update_dir.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd1 = "echo \""+pwd+"\" | sudo -S mkdir -p \""+update_dir[i]+"\""
            cmd2 = "echo \""+pwd+"\" | sudo -S usermod -d \""+update_dir[i]+"\" \""+username[i]+"\""
            print(cmd1)
            print(cmd2)
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
        print("done")
        messageBox.showinfo("Update User's Home Dirs", "Successfully Updated User's Home Dirs")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#set Expiry Date
def setExd_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userex_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userex_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        set_ex = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            set_ex.append(str(matrix[i][1][1]))

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -e \""+set_ex[i]+"\" \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Set Expiry Date", "Successfully Updated Expiry Dates")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#Change Password
def setPwd_batch():
    global entryb1
    pwd = entryb1.get()
    print("pwd :"+pwd)

    if pwd != '':
        userpwd_file =  filedialog.askopenfilename(initialdir = "/home",title = "Select CSV",filetypes = (("CSV files","*.csv"),("all files","*.*")))

        data = pd.read_csv(userpwd_file)
        df = pd.DataFrame(data)

        matrix =[]
        username = []
        set_pwd = []

        for row in df.iterrows():
            matrix.append(row)

        range_lenth = len(matrix)

        for i in range(0,range_lenth):
            username.append(matrix[i][1][0])
            print(matrix[i][1][0])
            set_pwd.append(crypt.crypt(str(matrix[i][1][1]), crypt.mksalt(crypt.METHOD_SHA512)))

        for i in range(0,range_lenth):
            cmd = "echo \""+pwd+"\" | sudo -S usermod -p \""+set_pwd[i]+"\" \""+username[i]+"\""
            print(cmd)
            subprocess.call(cmd, shell=True)
        print("done")
        messageBox.showinfo("Update Password", "Successfully Updated Passwords")
    else:
        messageBox.showwarning("WARNING", "Login Required")


#batchMode
eightFrame = Frame(tab3, bg="steel blue", bd = 8, relief = RIDGE)
eightFrame.place(x = 30, y = 150, width=775, height=220)
eightFrameLable2 = Label(eightFrame, image=batch_pic).pack(side="left")
eightFrameLabel = Label(tab3, text="Batch Mode:  CREATE USER", justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
eightFrameLabel.config(font=framelabelfont)
eightFrameLabel.place(x=220,y=160,width=545, height=50)
Button9 = Button(tab3, text="upload CSV", fg="black", bg="white", bd=3, command=uploadCSV)
Button9.place(x=350,y=270)
Button91 = Button(tab3, text="Create", fg="black", bg="white", bd=3, command=batchMode)
Button91.place(x=500,y=270, width=100)

tenthFrame = Frame(tab3, bg="steel blue", bd = 8, relief = RIDGE)
tenthFrame.place(x = 30, y = 400, width=775, height=300)
tenthFrameLable = Label(tenthFrame, text="Batch Mode Management Operations", justify=LEFT, relief = SUNKEN, pady=6, bg="old lace", bd = 4)
tenthFrameLable.config(font=framelabelfont)
tenthFrameLable.place(x=2,y=2,width=754, height=45)

Btn101 = Button(tab3, text="Delete User", fg="white", bg="red2", bd=3, command=del_users_batch).place(x = 60, y = 560, width=100)
Btn102 = Button(tab3, text="Lock User", fg="white", bg="tomato", bd=3, command=lock_users_batch).place(x = 60, y = 630, width=100)
Btn103 = Button(tab3, text="Update Username", fg="black", bg="white", bd=3,command=update_username_batch).place(x = 180, y = 560, width=140)
Btn104 = Button(tab3, text="Update Password", fg="black", bg="white", bd=3, command=setPwd_batch).place(x = 180, y = 630, width=140)
Btn105 = Button(tab3, text="Update User's Shell", fg="black", bg="white", bd=3,command=update_usershell_batch).place(x = 340, y = 560, width=160)
Btn106 = Button(tab3, text="Set Expiry Date", fg="black", bg="white", bd=3, command=setExd_batch).place(x = 340, y = 630, width=160)
Btn107 = Button(tab3, text="Update UID", fg="black", bg="white", bd=3, command=update_userUID_batch).place(x = 520, y = 560, width=100)
Btn108 = Button(tab3, text="Update GID", fg="black", bg="white", bd=3, command=update_userGID_batch).place(x = 520, y = 630, width=100)
Btn109 = Button(tab3, text="Change Home Dir", fg="black", bg="white", bd=3, command=update_homedir_batch).place(x = 640, y = 560, width=140)
Btn110 = Button(tab3, text="Unlock User", fg="black", bg="pale green", bd=3, command=unlock_user_batch).place(x = 640, y = 630, width=140)

#####################################################
root.minsize(845, 750)
root.resizable(0, 0)
root.mainloop()
