from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as font
#from main_screen import main_screen
from PIL import Image, ImageTk
import tkinter as tk
from settings_screen import settings_screen
from tkinter import messagebox  

class startup_screen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.colors = self.master.colors
        self.fonts = self.master.fonts
        IMAGE_PATH = 'images\\industry_1.jpg'
        WIDTH, HEIGTH = self.master.wmax, self.master.hmax
#        WIDTH, HEIGTH = 500, 500
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH-150, bd=0, highlightthickness=0)
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure('my.TButton', bordercolor=self.colors["blue"], font=self.fonts["bold"], foreground=self.colors["blue"], background="white")


        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        self.canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.canvas.pack(fill=BOTH, expand=True)        

        self.loginFrame = Frame(self, bg='#ab9a86')
        self.user_new = Entry(self, width=20, font=self.fonts["subtitle"], fg="#555555")
        self.user_new.insert(0, self.master.dict["User"])
        self.user_new.bind('<FocusIn>', self.get_uid_input)
#        self.user_new.pack(side=TOP, ipady=5, ipadx=5)

        self.pwd_new = Entry(self, width=20, font=self.fonts["subtitle"], fg="#555555")
        self.pwd_new.insert(0, self.master.dict["nodes"])
        self.pwd_new.bind('<FocusIn>', self.get_pwd_input)        
#        self.pwd_new.pack(side=TOP, ipady=5, ipadx=5, pady=(50,0))'''
        self.btn1 = ttk.Button(self, style="my.TButton", text="Login", command=self.check_credentials)
#        btn1.grid(row=0, column=0, padx=10, sticky=E)



        # self.loginFrame.configure(bg=self.colors["blue"])

        # self.user_id_frame = Frame(self.loginFrame, bg="#394264")
        # self.user_Image = ImageTk.PhotoImage(Image.open("images\\user_id.png").resize([33, 33]))
        # Label(self.user_id_frame, image=self.user_Image, pady=5, bg=self.colors["bg"]).pack(side=LEFT,)
        # self.user_new = Entry(self.user_id_frame, width=20, font=self.fonts["text"], text="Username")
        # self.user_new.pack(side=LEFT, ipady=5, ipadx=5)
        # self.user_id_frame.pack(expand=True)#(side=TOP, pady=(20, 0))

        # self.pwd_frame = Frame(self.loginFrame)
        # self.pwd_Image = ImageTk.PhotoImage(Image.open("images\\password.png").resize([33, 33]))
        # Label(self.pwd_frame, image=self.pwd_Image, pady=5, bg=self.colors["bg"]).pack(side=LEFT, padx=0)
        # self.pwd_new = Entry(self.pwd_frame, width=20, font=self.fonts["text"], text="Password", show="*")
        # self.pwd_new.pack(side=LEFT, ipady=5, ipadx=5, padx=0)
        # self.pwd_frame.pack(side=TOP, pady=10)

        # self.loginFailed = Label(self.loginFrame, text="", width=50, fg="red", font=self.fonts["small"], bg=self.colors["bg"])
        # self.loginFailed.pack()#grid(row=3, column=0, columnspan=2)
        # #       self.loginFrame.grid(row=3, column=0, pady=10)
        # #self.loginFrame.pack(expand=True)
        # self.master.grid_rowconfigure(3, weight=1)

        # self.responseFrame = Frame(self, bg=self.colors["bg"])
        
        # btn1 = ttk.Button(self.responseFrame, style="my.TButton", text="Login", command=self.check_credentials)
        # btn1.grid(row=0, column=0, padx=10, sticky=E)

        # btn2 = ttk.Button(self.responseFrame, style="my.TButton", text="Cancel", command=self.master.destroy)
        # btn2.grid(row=0, column=1, padx=10, sticky=E)

        #self.responseFrame.pack(side=TOP, pady=20, fill=Y, expand=True)
        self.w_1 = self.canvas.create_window(WIDTH/2, 300, anchor=CENTER, window=self.user_new)
        self.w_2 = self.canvas.create_window(WIDTH/2, 350, anchor=CENTER, window=self.pwd_new)
        self.w_3 = self.canvas.create_window(WIDTH/2, 420, anchor=CENTER, window=self.btn1)


    def check_credentials(self):
        """Validate login credentials"""
        WIDTH, HEIGTH = self.master.wmax, self.master.hmax        
        u_n = self.user_new.get()
        self.master.dict["User"] = u_n
        p_wd = self.pwd_new.get()
        self.master.dict["nodes"] = int(p_wd)
        '''valid = False
        if u_n == "Administrator":
            if self.master.prog_settings.get("installer_password") == p_wd:
                valid = True
        elif u_n == "User 1":
            if self.master.prog_settings.get("user_1_password") == p_wd:
                valid = True
        elif u_n == "User 2":
            if self.master.prog_settings.get("user_2_password") == p_wd:
                valid = True
        valid = True'''
        valid = True
        if valid:
            print("Login successfull")
            self.master.switch_frame(settings_screen)
            messagebox.showinfo("Welcome!", "Welcome to the program: " + str(u_n) + "\nPlease enter the matrix!")
        else:
            self.canvas.create_text(WIDTH/2, 500, text="Incorrect Username or Password !!", font=("Helvetica", 12), fill="red")

    def get_uid_input(self, x):
        self.user_new.delete(0, 'end')
        self.user_new.config(fg="#000000")

    def get_pwd_input(self, x):
        self.pwd_new.delete(0, 'end')
        #self.pwd_new.config(show="*")
        self.pwd_new.config(fg="#000000")
