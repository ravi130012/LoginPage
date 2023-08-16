import customtkinter
from customtkinter import *
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

#credentials

#configrations
bg_color = "#2A2A2A"
frame_bg_color = "#1F1F1F"
label_fg_color = "cyan"
btn_fg_color = "cyan"
btn_bg_color = "#1F1F1F"
entry_bg_color = "#1F1F1F"
entry_fg_color = "red"

#main configrations
root.geometry("800x600+200+50")

#frame
f = CTkFrame(root)
f.pack(pady=120)


#header
logo = customtkinter.CTkImage(Image.open("death.png"), size=(90, 90))
logo_lb = CTkLabel(f,image=logo,text="")
logo_lb.grid(row=0,column=0,pady=(15,15))

logo_txt = CTkLabel(f,text="PASSGEN",font=customtkinter.CTkFont(family="sarif", size=50))
logo_txt.grid(row=0,column=1,pady=(15,0),padx=(0,30))



#label
user_lb = CTkLabel(f,text="Username",font=customtkinter.CTkFont(family="sarif", size=30))
user_lb.grid(row=1,column=0,padx=(60,30),pady=(0,0))

pass_lb =   CTkLabel(f,text="Password",font=customtkinter.CTkFont(family="sarif", size=30))
pass_lb.grid(row=2,column=0,padx=(60,30),pady=(15,15))

#variables
user_var = StringVar(value="Darkstar")
pass_var = StringVar()

#entry
user_en = CTkEntry(f,textvariable=user_var,justify="center",font=customtkinter.CTkFont(family="sarif", size=30),width=300)
user_en.grid(row=1,column=1,padx=(0,30),pady=(0,0))


pass_en = CTkEntry(f,textvariable=pass_var,show='*',justify="center",font=customtkinter.CTkFont(family="sarif", size=30),width=300)
pass_en.grid(row=2,column=1,padx=(0,30),pady=(15,15))


#button
log_btn = CTkButton(f,text="Login",cursor="hand2",font=customtkinter.CTkFont(family="sarif", size=30))
log_btn.grid(row=3,column=1,padx=(0,30),pady=(0,30))

#btnconfig


root.mainloop()
