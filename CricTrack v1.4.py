import customtkinter
from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime
from tkinter import messagebox
import sqlite3

home = customtkinter.CTk()
home.geometry("720x480")

frame = ttk.Frame(home)
frame.grid(row=0, column=0)
home.grid_rowconfigure(0, weight=1)
home.grid_rowconfigure(1, weight=1)
home.grid_rowconfigure(2, weight=1)
home.grid_rowconfigure(3, weight=1)
home.grid_rowconfigure(4, weight=1)

home.grid_columnconfigure(0, weight=1)
home.grid_columnconfigure(1, weight=1)
home.grid_columnconfigure(2, weight=1)
home.grid_columnconfigure(3, weight=1)



now = datetime.now()
day_label = customtkinter.CTkLabel(home,text=now.strftime("%A"))
day_label.grid(row=0,column=3)
date_label = customtkinter.CTkLabel(home,text=now.strftime("%d %B %Y"))
date_label.grid(row=1,column=3)

upi_label = customtkinter.CTkLabel(home,text="Support Me:\nabhilashrai9896@oksbi")   #add QR code as a permanent image 
upi_label.grid(row=0,column=0)

continue_button = customtkinter.CTkButton(home,text="Continue Match")   # add command later
continue_button.grid(row=3,column=3)
def create_function():
       global teamname_entry
       global teamname_entry2
       global playernames_entry
       global playernames_entry2
       create_page = customtkinter.CTkToplevel(home) 
       create_page.geometry("500x300")

       frame2 = ttk.Frame(create_page)
       frame2.grid(row=0, column=0)
       create_page.grid_rowconfigure(0, weight=1)
       create_page.grid_rowconfigure(1, weight=1)
       create_page.grid_rowconfigure(2, weight=2)
       create_page.grid_rowconfigure(3, weight=2)
       create_page.grid_rowconfigure(4, weight=1)

       create_page.grid_columnconfigure(0, weight=2)
       create_page.grid_columnconfigure(1, weight=2)
       create_page.grid_columnconfigure(2, weight=1)
       create_page.grid_columnconfigure(3, weight=1)
#--------------------BATTING----------------------
       batteam_label = customtkinter.CTkLabel(create_page,text="Batting Team")
       batteam_label.grid(row=0,column=0)
       teamname_label = customtkinter.CTkLabel(create_page,text="Team Name*")
       teamname_label.grid(row=1,column=0)
       teamname_entry = customtkinter.CTkEntry(create_page,placeholder_text="must fill...",width=120)
       teamname_entry.grid(row=1,column=1)

       playernames_entry = customtkinter.CTkEntry(create_page,placeholder_text="use comma to separate player names...",width=250,height=200)
       playernames_entry.grid(row=2,column=0,columnspan=2)

       save_list = customtkinter.CTkButton(create_page,text="Save List",command=save_batteam_list)  
       save_list.grid(row=3,column=0,ipady=5)
#--------------------BALLING----------------
       ballteam_label = customtkinter.CTkLabel(create_page,text="Balling Team")
       ballteam_label.grid(row=0,column=2)
       teamname_label2 = customtkinter.CTkLabel(create_page,text="Team Name*")
       teamname_label2.grid(row=1,column=2)
       teamname_entry2 = customtkinter.CTkEntry(create_page,placeholder_text="must fill...",width=120)
       teamname_entry2.grid(row=1,column=3)

       playernames_entry2 = customtkinter.CTkEntry(create_page,placeholder_text="use comma to separate player names...",width=250,height=200)
       playernames_entry2.grid(row=2,column=2,columnspan=2)
   
       save_list2 = customtkinter.CTkButton(create_page,text="Save List",command=save_ballteam_list)  
       save_list2.grid(row=3,column=2,ipady=5)
def save_batteam_list():   #db to save data of batting team
#----------------------fetching teamnames to check for redundancy-----------------------
                     conn = sqlite3.connect('batteam.db')
                     c = conn.cursor()
                     c.execute('SELECT TEAM_BATTING FROM BATTEAM')
                     teamnames = c.fetchall()
                     conn.commit()
                     conn.close()
                     batteam_name_list = [row[0] for row in teamnames]  # fixed: flatten tuples to plain strings
                     #print(batteam_name_list)
                     if teamname_entry.get() in batteam_name_list:
                            messagebox.showerror("Error","Team name already exists!\nUse a different team name") 
                     #for names in teamnames:
                     #       print(names[0])            # row[0] extracts the strings from the tuple
                     #       if teamname_entry.get() == names[0]:
                                    
#----------------------inserting into db now--------------------------------------------
                     else:        
                            conn = sqlite3.connect('batteam.db')
                            c = conn.cursor()
                            c.execute('''CREATE TABLE IF NOT EXISTS BATTEAM(
                                      ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                      DATE INTEGER NOT NULL,
                                      VENUE TEXT NOT NULL,
                                      TEAM_BATTING TEXT NOT NULL,
                                      PLAYERS_BAT TEXT NOT NULL
                            )''')
                            #conn.commit()
                            #conn.close()
                            #conn = sqlite3.connect('batteam.db')
                            #c = conn.cursor()
                            c.execute('''INSERT INTO BATTEAM(
                                      DATE,VENUE,TEAM_BATTING,PLAYERS_BAT)
                                      VALUES (?,?,?,?)''',(now.year * 10000 + now.month * 100 + now.day,"Piro",teamname_entry.get(),playernames_entry.get())) 
                            #conn.commit()
                            #conn.close()
                            #conn = sqlite3.connect('batteam.db')
                            #c = conn.cursor()
                            c.execute('SELECT * FROM BATTEAM')
                            result = c.fetchall()
                            conn.commit()
                            conn.close()
                            print("batteam",result)
                            messagebox.showinfo("Edit List","List Saved Successfully!")   #list is actaully saved or not should be tested 
                                                                                           #but okay for now
def save_ballteam_list():   #db to save data of balling team
                     conn = sqlite3.connect('ballteam.db')
                     c = conn.cursor()
                     c.execute('SELECT TEAM_BALLING FROM BALLTEAM')
                     teamnames2 = c.fetchall()
                     conn.commit()
                     conn.close()
                     ballteam_neame_list = [row[0] for row in teamnames2]  # fixed: flatten tuples to plain strings
                     #print(batteam_name_list)
                     if teamname_entry2.get() in ballteam_neame_list:
                             messagebox.showerror("Error","Team name already exists!\nUse a different team name")
                     else:
                             conn = sqlite3.connect('ballteam.db')
                             c = conn.cursor()
                             c.execute('''CREATE TABLE IF NOT EXISTS BALLTEAM(
                                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                       DATE INTEGER NOT NULL,
                                       VENUE TEXT NOT NULL,
                                       TEAM_BALLING TEXT NOT NULL,
                                       PLAYERS_BALL TEXT NOT NULL
        
                             )''')
                             #conn.commit()
                             #conn.close()
                             #conn = sqlite3.connect('ballteam.db')
                             #c = conn.cursor()
                             c.execute('''INSERT INTO BALLTEAM(
                                       DATE,VENUE,TEAM_BALLING,PLAYERS_BALL)
                                       VALUES (?,?,?,?)''',(now.year * 10000 + now.month * 100 + now.day,"Piro",teamname_entry2.get(),playernames_entry2.get())) 
                             #conn.commit()
                             #conn.close()
                             #conn = sqlite3.connect('ballteam.db')
                             #c = conn.cursor()
                             c.execute('SELECT * FROM BALLTEAM')
                             result2 = c.fetchall()
                             conn.commit()
                             conn.close()
                             print("ballteam",result2)
                             messagebox.showinfo("Edit List","List Saved Successfully!")   #list is actaully saved or not should be tested 
                                                                                             #but okay for now
edit_button = customtkinter.CTkButton(home,text="Create Team",command=create_function)    
edit_button.grid(row=4,column=2)
def edit_list():
              edit_page = customtkinter.CTkToplevel(home) 
              edit_page.geometry("500x300")

              frame3 = ttk.Frame(edit_page)
              frame3.grid(row=0, column=0)
              edit_page.grid_rowconfigure(0, weight=1)
              edit_page.grid_rowconfigure(1, weight=1)
              edit_page.grid_rowconfigure(2, weight=1)
              edit_page.grid_rowconfigure(3, weight=1)
              edit_page.grid_rowconfigure(4, weight=1)

              edit_page.grid_columnconfigure(0, weight=1)
              edit_page.grid_columnconfigure(1, weight=1)
              edit_page.grid_columnconfigure(2, weight=1)
              edit_page.grid_columnconfigure(3, weight=1)

              #label2 = customtkinter.CTkLabel(edit_page,text="edit")
              #label2.grid(row=0,column=1)
              select_team = customtkinter.CTkLabel(edit_page,text="Select team*")
              select_team.grid(row=0,column=0)
              teamname_label = customtkinter.CTkLabel(edit_page,text="Team name*")
              teamname_label.grid(row=2,column=0)
              radio_var = customtkinter.StringVar(value="BATTEAM")
              batteam_radiobtn = customtkinter.CTkRadioButton(edit_page,text="Batting team",variable=radio_var,value="BATTEAM")
              batteam_radiobtn.grid(row=0,column=1)
              ballteam_radiobtn = customtkinter.CTkRadioButton(edit_page,text="Balling team",variable=radio_var,value="BALLTEAM")
              ballteam_radiobtn.grid(row=1,column=1)
              teamname_entry3 = customtkinter.CTkEntry(edit_page,placeholder_text="must fill...")
              teamname_entry3.grid(row=2,column=1)
#-------------data from db will be feteched and inserted into this entry widget later-------------------------------
              def fetch_insert():
                      global player_edited_entry
                      global player_edited_entry2
                      if radio_var.get() == "BATTEAM":
                              conn = sqlite3.connect('batteam.db')
                              c = conn.cursor()
                              c.execute('SELECT PLAYERS_BAT FROM BATTEAM WHERE TEAM_BATTING = ?', (teamname_entry3.get(),))
                              playername_fetch = c.fetchone()
                              conn.commit()
                              conn.close()
                              #playername_list = [row[0] for row in playername_fetch]
                              player_edited_entry = customtkinter.CTkEntry(edit_page)
                              player_edited_entry.insert(0, playername_fetch[0])
                              player_edited_entry.grid(row=3,column=0,ipadx=100,ipady=70,columnspan=2)

                      elif radio_var.get() == "BALLTEAM":
                              conn = sqlite3.connect('ballteam.db')
                              c = conn.cursor()
                              c.execute('SELECT PLAYERS_BALL FROM BALLTEAM WHERE TEAM_BALLING = ?', (teamname_entry3.get(),))
                              playername_fetch2 = c.fetchone()
                              conn.commit()
                              conn.close()
                              #playername_list2 = [row[0] for row in playername_fetch2]
                              player_edited_entry2 = customtkinter.CTkEntry(edit_page)
                              player_edited_entry2.insert(0, playername_fetch2[0])
                              player_edited_entry2.grid(row=3,column=0,ipadx=100,ipady=70,columnspan=2)
                              print("ok")
                      #print("write code to fetch and insert from db")
              load_button = customtkinter.CTkButton(edit_page,text="Load",command=fetch_insert) # to be defined later
              load_button.grid(row=4,column=0)
              def update_team():
                      if radio_var.get() == "BATTEAM":
                              conn = sqlite3.connect('batteam.db')
                              c = conn.cursor()
                              c.execute('UPDATE BATTEAM SET PLAYERS_BAT = ? WHERE TEAM_BATTING = ?',(player_edited_entry.get(),teamname_entry3.get()))
                              conn.commit()
                              conn.close()
                              messagebox.showinfo("Save","List edited successfully!")
                      elif radio_var.get() == "BALLTEAM":
                              conn = sqlite3.connect('ballteam.db')
                              c = conn.cursor()
                              c.execute('UPDATE BALLTEAM SET PLAYERS_BALL = ? WHERE TEAM_BALLING = ?',(player_edited_entry2.get(), teamname_entry3.get()))
                              conn.commit()
                              conn.close()
                              messagebox.showinfo("Save","List edited successfully!")
              save_button = customtkinter.CTkButton(edit_page,text="Save",command=update_team) # to be defined later
              save_button.grid(row=4,column=1)
edit_another_list2 = customtkinter.CTkButton(home,text="Edit Saved Team",command=edit_list)  # add command later
edit_another_list2.grid(row=4,column=3)

def game_details():
        details_page = customtkinter.CTkToplevel(home)
        details_page.geometry("500x300")

        frame4 = ttk.Frame(details_page)
        frame4.grid(row=0,column=0)
        details_page.grid_rowconfigure(0, weight=1)
        details_page.grid_rowconfigure(1, weight=1)
        details_page.grid_rowconfigure(2, weight=1)
        details_page.grid_rowconfigure(3, weight=1)
        details_page.grid_rowconfigure(4, weight=1)
        
        details_page.grid_columnconfigure(0, weight=1)
        details_page.grid_columnconfigure(1, weight=1)
        details_page.grid_columnconfigure(2, weight=1)
        details_page.grid_columnconfigure(3, weight=1)

        batteam_label = customtkinter.CTkLabel(details_page,text='Batting team')
        batteam_label.grid(row=0,column=0)
        players_entry = customtkinter.CTkEntry(details_page,placeholder_text='Team name...',width=100)
        players_entry.grid(row=1,column=0)
        players_textbox = customtkinter.CTkTextbox(details_page,width=340,height=150)
        players_textbox.grid(row=2,column=0,columnspan=2)
        def load_team():   #user can load any team as batting team or balling team.
                conn = sqlite3.connect('batteam.db')
                c = conn.cursor()
                c.execute('SELECT PLAYERS_BAT FROM BATTEAM WHERE TEAM_BATTING = ?',(players_entry.get(),))
                rows = c.fetchall()
                conn.commit()
                conn.close()
                conn = sqlite3.connect('ballteam.db')
                c = conn.cursor()
                c.execute('SELECT PLAYERS_BALL FROM BALLTEAM WHERE TEAM_BALLING = ?',(players_entry.get(),))
                rows2 = c.fetchall()
                conn.commit()
                conn.close()
                print("row",rows,"\nrow2",rows2)
                if len(rows) == 0:
                            players_textbox.insert("1.0",rows2[0])
                elif len(rows2) == 0:
                            players_textbox.insert("1.0",rows[0])
                
        load_button = customtkinter.CTkButton(details_page,text='Load',command=load_team) # command Loading data from db to be added later
        load_button.grid(row=3,column=0)

        save_button = customtkinter.CTkButton(details_page,text='Save')   #save button saves details to DETAILS.db
        save_button.grid(row=3,column=1)                                  # command to be added later

        ballingteam_label = customtkinter.CTkLabel(details_page,text='Balling team')
        ballingteam_label.grid(row=0,column=2)
        players_entry2 = customtkinter.CTkEntry(details_page,placeholder_text='Team name...',width=100)
        players_entry2.grid(row=1,column=2)
        players_textbox2 = customtkinter.CTkTextbox(details_page,width=340,height=150)
        players_textbox2.grid(row=2,column=2,columnspan=2)
        load_button2 = customtkinter.CTkButton(details_page,text='Load')   # command Loading data from db to be added later
        load_button2.grid(row=3,column=2)

        save_button2 = customtkinter.CTkButton(details_page,text='Save')   #save button saves details to DETAILS.db
        save_button2.grid(row=3,column=3) 

start_button = customtkinter.CTkButton(home,text="Start Match",command=game_details)   
start_button.grid(row=3,column=2)

feedback_button = customtkinter.CTkButton(home,text="Help?")     # add command later
feedback_button.grid(row=4,column=0)

home.mainloop()