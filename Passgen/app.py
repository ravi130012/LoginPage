from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


#configrations
bg_color = "#2A2A2A"
frame_bg_color = "#1F1F1F"
label_fg_color = "cyan"
btn_fg_color = "cyan"
btn_bg_color = "#1F1F1F"
entry_bg_color = "#1F1F1F"
entry_fg_color = "red"

#defining root object
root = Tk()


#function
def on_enter(e):
    log_btn['foreground'] = '#fb1466'

def on_leave(e):
    log_btn['foreground'] = 'cyan'

def handle_click(e):
    check_user_input()


#main configrations
root.config(bg=bg_color)
root.title("Login")
root.geometry("800x600+200+50")

#frame
f = Frame(root,bg=frame_bg_color)
f.pack(pady=120)


#header
img = Image.open("death.png")
img = img.resize((100,100))
logo = ImageTk.PhotoImage(img)
logo_lb = Label(f,image=logo,bg=frame_bg_color)
logo_lb.grid(row=0,column=0,pady=(15,15))

logo_txt = Label(f,text="PASSGEN",fg="#fb1466",bg=frame_bg_color,font=("sarif 40 bold"))
logo_txt.grid(row=0,column=1,pady=(15,0),padx=(0,0))



#label
user_lb = Label(f,text="Username",font=("sarif 20 bold"),bg=frame_bg_color,fg=label_fg_color)
user_lb.grid(row=1,column=0,padx=(60,30),pady=(0,0))

pass_lb = Label(f,text="Password",font=("sarif 20 bold"),bg=frame_bg_color,fg=label_fg_color)
pass_lb.grid(row=2,column=0,padx=(60,30),pady=(15,15))

#variables
user_var = StringVar(value="Darkstar")
pass_var = StringVar()

#entry
user_en = Entry(f,textvariable=user_var,font=("san-sarif 20"),bg=entry_bg_color,fg=entry_fg_color,justify="center")
user_en.grid(row=1,column=1,padx=(0,30),pady=(0,0))
user_en.bind("<Return>", handle_click)

pass_en = Entry(f,textvariable=pass_var,font=("san-sarif 20"),bg=entry_bg_color,fg=entry_fg_color,show='*',justify="center")
pass_en.grid(row=2,column=1,padx=(0,30),pady=(15,15))
pass_en.bind("<Return>", handle_click)

#button
log_btn = Button(f,text="Login",font=("sarif 20 bold"), bg=btn_bg_color,fg=btn_fg_color,cursor="hand2")
log_btn.grid(row=3,column=1,pady=(0,70))

#btnconfig
log_btn.bind('<Enter>',on_enter)
log_btn.bind('<Leave>',on_leave)

root.mainloop()
