import PIL
import tkinter
import customtkinter as CTK
from string import ascii_lowercase,ascii_uppercase,digits,punctuation

import pass_new

class App(CTK.CTk):
    
    def __init__(self):
        super().__init__()

        self.geometry("460x270")
        self.title("Ninja Generator")
        self.resizable(False,False)

        self.logo = CTK.CTkImage(dark_image=PIL.Image.open("img/Logo.png"),size=(358,56))
        self.logo_lable = CTK.CTkLabel(master=self,text="",image=self.logo)
        self.logo_lable.grid(row=0,column=0,pady=(10,10))

        self.pass_frame = CTK.CTkFrame(master=self,fg_color="transparent")
        self.pass_frame.grid(row=1,column=0,sticky="nsew")

        self.entry_pass = CTK.CTkEntry(master=self.pass_frame,width=300)
        self.entry_pass.grid(row=1,column=0,padx=(20,0),sticky="nsew")

        self.btn_gerator = CTK.CTkButton(master=self.pass_frame,text="Generate",width=100,command=self.set_pass)
        self.btn_gerator.grid(row=1,column=1,padx=(20,0))

        self.settings_frame = CTK.CTkFrame(master=self)
        self.settings_frame.grid(row=2,column=0,padx=(20,20),pady=(20,0),sticky="nsew")

        self.pass_len_slider = CTK.CTkSlider(master=self.settings_frame,from_=0,to=100,number_of_steps=100,command=self.slider_event)
        self.pass_len_slider.set(10)
        self.pass_len_slider.grid(row=1,column=0,columnspan=3,pady=(20,20),sticky="ew")

        self.pass_len_entry = CTK.CTkEntry(master=self.settings_frame,width=50)
        self.pass_len_entry.insert(0,10)
        self.pass_len_entry.grid(row=1,column=3,padx=(20,20),sticky="ew")

        self.cb_dig_var = tkinter.StringVar()
        self.cb_dig = CTK.CTkCheckBox(master=self.settings_frame,text="0-9",variable=self.cb_dig_var,onvalue=digits,offvalue="")
        self.cb_dig.grid(row=2,column=0,padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTK.CTkCheckBox(master=self.settings_frame,text="a-z",variable=self.cb_lower_var,onvalue=ascii_lowercase,offvalue="")
        self.cb_lower.grid(row=2,column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTK.CTkCheckBox(master=self.settings_frame,text="A-Z",variable=self.cb_upper_var,onvalue=ascii_uppercase,offvalue="")
        self.cb_upper.grid(row=2,column=2)

        self.cb_symvol_var = tkinter.StringVar()
        self.cb_symvol = CTK.CTkCheckBox(master=self.settings_frame,text="!@#$",variable=self.cb_symvol_var,onvalue=punctuation,offvalue="")
        self.cb_symvol.grid(row=2,column=3)

        self.apperance_mode_option_menu = CTK.CTkOptionMenu(master=self.settings_frame,values=["System","Light","Dark"],command=self.change_apperance_mode_event)
        self.apperance_mode_option_menu.set("System")
        self.apperance_mode_option_menu.grid(row=3,column=0,columnspan=4,pady=(10,10))

    def change_apperance_mode_event(self,new_apperance_mode):
          CTK.set_appearance_mode(new_apperance_mode)

    def set_pass(self):
            self.entry_pass.delete(0,"end")
            self.entry_pass.insert(0,pass_new.create_new(len=int(self.pass_len_slider.get()),chars=self.get_char()))
    
    def slider_event(self,value):
            self.pass_len_entry.delete(0,"end")
            self.pass_len_entry.insert(0,int(value))

    def get_char(self):
          chars = "".join(self.cb_dig_var.get()+self.cb_lower_var.get()+self.cb_upper_var.get()+self.cb_symvol_var.get())
          return chars