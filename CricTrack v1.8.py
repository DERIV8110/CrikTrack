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
        global players_textbox
        global players_textbox2
        global radio_var2
        global players_entry
        global players_entry2
        global date_entry
        global venue_entry
        global innings_entry
        global overs_entry
        details_page = customtkinter.CTkToplevel(home)
        details_page.geometry("900x400")

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
        details_page.grid_columnconfigure(4, weight=2)
        details_page.grid_columnconfigure(5, weight=1)
#--------team to bat and ball chosen by toss using radiobutton-------------------------------
        radio_var2 = customtkinter.StringVar(value="teama")
        team1_radiobtn = customtkinter.CTkRadioButton(details_page,text='Won the toss',variable=radio_var2,value='teama')
        team1_radiobtn.grid(row=3,column=0)
        team2_radiobtn = customtkinter.CTkRadioButton(details_page,text='Won the toss',variable=radio_var2,value='teamb')
        team2_radiobtn.grid(row=3,column=2)

        batteam_label = customtkinter.CTkLabel(details_page,text='Team A')
        batteam_label.grid(row=0,column=0)
        players_entry = customtkinter.CTkEntry(details_page,placeholder_text='Team name...',width=100)    #it's team name not player name
        players_entry.insert(0,"PAK2")          #<< Remove it later!!
        players_entry.grid(row=0,column=1)
        players_textbox = customtkinter.CTkTextbox(details_page,width=340,height=150)
        players_textbox.grid(row=2,column=0,columnspan=2)
#--------load team A----------------------------------------
        def load_team_a():   #user can load any team as batting team or balling team.
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
                #print("row",rows,"\nrow2",rows2)
                if len(rows) == 0:
                            players_textbox.insert("1.0",rows2[0])
                elif len(rows2) == 0:
                            players_textbox.insert("1.0",rows[0])
                
        load_button = customtkinter.CTkButton(details_page,text='Load',command=load_team_a) # command Loading data from db to be added later
        load_button.grid(row=4,column=0)
#--------save all data of details page to MATCH.db for scoreboard---------------------------------
        #save_button = customtkinter.CTkButton(details_page,text='Save')   #save button saves details to MATCH.db
        #save_button.grid(row=4,column=1)                                  # command to be added later

        ballingteam_label = customtkinter.CTkLabel(details_page,text='Team B')
        ballingteam_label.grid(row=0,column=2)
        players_entry2 = customtkinter.CTkEntry(details_page,placeholder_text='Team name...',width=100)   #it's team name not player name
        players_entry2.insert(0,"Aus")          #<< Remove it later!!
        players_entry2.grid(row=0,column=3)
        players_textbox2 = customtkinter.CTkTextbox(details_page,width=340,height=150)
        players_textbox2.grid(row=2,column=2,columnspan=2)
#--------load team B------------------------------------------------
        def load_team_b():   #user can load any team as batting team or balling team.
                conn = sqlite3.connect('batteam.db')
                c = conn.cursor()
                c.execute('SELECT PLAYERS_BAT FROM BATTEAM WHERE TEAM_BATTING = ?',(players_entry2.get(),))
                rows = c.fetchall()
                conn.commit()
                conn.close()
                conn = sqlite3.connect('ballteam.db')
                c = conn.cursor()
                c.execute('SELECT PLAYERS_BALL FROM BALLTEAM WHERE TEAM_BALLING = ?',(players_entry2.get(),))
                rows2 = c.fetchall()
                conn.commit()
                conn.close()
                #print("row",rows,"\nrow2",rows2)
                if len(rows) == 0:
                            players_textbox2.insert("1.0",rows2[0])
                elif len(rows2) == 0:
                            players_textbox2.insert("1.0",rows[0])

        load_button2 = customtkinter.CTkButton(details_page,text='Load',command=load_team_b)   # command Loading data from db to be added later
        load_button2.grid(row=4,column=2)
#--------save all data of details page to MATCH.db for scoreboard---------------------------------
        #save_button2 = customtkinter.CTkButton(details_page,text='Save')   #save button saves details to MATCH.db
        #save_button2.grid(row=4,column=3) 
        
        date_label2 = customtkinter.CTkLabel(details_page,text='Date')
        date_label2.grid(row=0,column=4)
        date_entry = customtkinter.CTkEntry(details_page)
        date_entry.grid(row=0,column=5)
        date_entry.insert(0,now.year * 10000 + now.month * 100 + now.day)        # date is stored in MATCH.db 

        venue_label = customtkinter.CTkLabel(details_page,text='Venue')
        venue_label.grid(row=1,column=4)
        venue_entry = customtkinter.CTkEntry(details_page)
        venue_entry.insert(0,"Wankhede")        #<< Remove it later!!
        venue_entry.grid(row=1,column=5)

        innings_label = customtkinter.CTkLabel(details_page,text='Innings')
        innings_label.grid(row=2,column=4)
        innings_entry = customtkinter.CTkEntry(details_page)
        innings_entry.insert(0,"1")             #<< Remove it later!!
        innings_entry.grid(row=2,column=5)

        overs_label = customtkinter.CTkLabel(details_page,text='Overs Per\nInning')
        overs_label.grid(row=3,column=4)
        overs_entry = customtkinter.CTkEntry(details_page)
        overs_entry.insert(0,"10")              #<< Remove it later!!         
        overs_entry.grid(row=3,column=5)
        #-----------open batsman selector window-----------------------------------------------------------
        def batsman_selector_window():
                     global selected_batsman   
                     raw = players_textbox.get("1.0", "end").strip().strip("{}")
                     player_names = [name.strip() for name in raw.split(',') if name.strip()]

                     selector_window = customtkinter.CTkToplevel(details_page)
                     selector_window.geometry("300x500")

                     frame6 = customtkinter.CTkFrame(selector_window)  # fixed: was ttk.Frame
                     frame6.grid(row=0, column=0, sticky="nsew")

                     selector_window.grid_rowconfigure(tuple(range(16)), weight=1)   #tuple(range(16))>> replaces 16 repeated grid_rowconfigure lines
                     selector_window.grid_columnconfigure(0, weight=1)
                     selector_window.grid_columnconfigure(1, weight=1)

                     # -------- fetching data from CTkTextbox and building radio buttons --------
                     selected_batsman = ttk.StringVar()  # fixed: was ttk.StringVar (doesn't exist)

                     for name in player_names:
                         row_frame = customtkinter.CTkFrame(frame6)   # fixed: was self.selector_window
                         row_frame.pack(fill='x', padx=10, pady=2)

                         radio_btn = customtkinter.CTkRadioButton(
                             row_frame,
                             text=name,
                             variable=selected_batsman,
                             value=name,
                             font=("Arial", 16)   # increase size here                               # fixed: was values=name
                         )
                         radio_btn.pack(side='left', padx=5)

        #--------------get the radio var value and parse it to the database to update that batsman score
        #--------------if the wicket buton is clicked in scoreboard window>> load this selector window again 
        #--------------choose the batsman and update the data in db and so on------------------------------
        select_batsman_window = customtkinter.CTkButton(details_page,text='Choose\n Batsman',command=batsman_selector_window)
        select_batsman_window.grid(row=4,column=5)
        load_dash = customtkinter.CTkButton(details_page,text='Start',command=load_scoreboard)
        load_dash.grid(row=4,column=4)
#------------start button saves date/venue/innings/overs per inning into MATCH.db--------------------------
def load_scoreboard():
        messagebox.showinfo("Loading","Just a sec...")
            # always get both teams
        batteam = players_textbox.get("1.0", "end").strip()
        ballteam = players_textbox2.get("1.0", "end").strip()
        
        # radio only decides toss winner
        if radio_var2 == 'teama':
            toss_winner = players_entry.get()
        elif radio_var2 == 'teamb':
            toss_winner = players_entry2.get()
        else:
            toss_winner = ""   # problem with toss winner!
        
        conn = sqlite3.connect('match.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS MATCH(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  DATE INTEGER NOT NULL,
                  VENUE TEXT NOT NULL,
                  INNINGS INTEGER NOT NULL,
                  OVERS INTEGER NOT NULL,
                  BATTEAM TEXT NOT NULL,
                  BALLTEAM TEXT NOT NULL,
                  TOSSWINNER TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()
        conn = sqlite3.connect('match.db')
        c = conn.cursor()
        c.execute('INSERT INTO MATCH(DATE,VENUE,INNINGS,OVERS,BATTEAM,BALLTEAM,TOSSWINNER) VALUES (?,?,?,?,?,?,?)',
                  (date_entry.get(),venue_entry.get(),innings_entry.get(),overs_entry.get(),batteam,ballteam,toss_winner))
        conn.commit()
        conn.close()
        #------------retrieve every batter and baller name and each name
        #             should be rows and columns for keeping record of score of each player in that row--------------------
        conn = sqlite3.connect('batsman.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS BATSMAN(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  DATE INTEGER NOT NULL,
                  TEAM TEXT NOT NULL,
                  NAME TEXT NOT NULL,
                  RUNS INTEGER NOT NULL DEFAULT 0,
                  BALLS INTEGER NOT NULL DEFAULT 0,
                  ONES INTEGER NOT NULL DEFAULT 0,
                  TWOS INTEGER NOT NULL DEFAULT 0,
                  THREES INTEGER NOT NULL DEFAULT 0,
                  FOURS INTEGER NOT NULL DEFAULT 0,
                  FIVES INTEGER NOT NULL DEFAULT 0,
                  SIXES INTEGER NOT NULL DEFAULT 0,
                  FOWL INTEGER NOT NULL DEFAULT 0,
                  HOWOUT TEXT
        )''')
        # NOW retrieve batting player names from match db and feed into names of BATSMAN DB
        conn.commit()
        conn.close()
        conn = sqlite3.connect('match.db')
        c = conn.cursor()
        c.execute('SELECT BATTEAM FROM MATCH')
        result2 = c.fetchall()
        print(result2)
        conn.commit()
        conn.close()
        
        for row in result2:
             team_string = row[0]          # get the string from the tuple
             if not team_string:           # skip empty rows like ('',)
                 continue
             team_string = team_string.strip('{}')   # remove { and }
             names = team_string.split(', ')         # split into list
             # use for loop to insert names one by one (different entries create new rows)
             for name in names:
                 conn = sqlite3.connect('batsman.db')
                 c = conn.cursor()
                 c.execute('INSERT INTO BATSMAN(DATE,TEAM,NAME) VALUES (?,?,?)',(now.year * 10000 + now.month * 100 + now.day,players_entry.get(),name))
                 conn.commit()
                 conn.close()
        #-------------balling team code will be written later-----------------------------------------------------

        #-------------Loading Scoreboard GUI and feeding above data in treeview-----------------------------------
        score_page = customtkinter.CTkToplevel(home)
        score_page.geometry("1000x900")

        # Row config — nothing expands
        score_page.grid_rowconfigure(0, weight=0)  # labels row — fixed
        score_page.grid_rowconfigure(1, weight=0)  # treeview row — fixed

        # Column config
        score_page.grid_columnconfigure(0, weight=1)
        score_page.grid_columnconfigure(1, weight=1)
        score_page.grid_columnconfigure(2, weight=1)
        score_page.grid_columnconfigure(3, weight=1)
        score_page.grid_columnconfigure(4, weight=1)
        score_page.grid_columnconfigure(5, weight=1)
        frame5 = ttk.Frame(score_page, width=1300, height=300)  # height 200 → 300
        # Add this RIGHT AFTER score_page = customtkinter.CTkToplevel(home)
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 18), rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 20, "bold"))
        # ── Row 0: Labels ──────────────────────────────────────────
        teama_label = customtkinter.CTkLabel(score_page, text=players_entry.get(), font=("Arial", 16, "bold"))
        teama_label.grid(row=0, column=0, pady=15)

        versus_label = customtkinter.CTkLabel(score_page, text="VS", font=("Arial", 16, "bold"))
        versus_label.grid(row=0, column=1, pady=15)

        teamb_label = customtkinter.CTkLabel(score_page, text=players_entry2.get(), font=("Arial", 16, "bold"))
        teamb_label.grid(row=0, column=2, pady=15)

        teama_toss_label = customtkinter.CTkLabel(score_page, text=players_entry.get(), font=("Arial", 14))
        teama_toss_label.grid(row=0, column=3, pady=15)

        toss_win_label = customtkinter.CTkLabel(score_page, text="Chose to bat", font=("Arial", 14))
        toss_win_label.grid(row=0, column=4, pady=15)

        # ── Row 1: Treeview (col 0-4, fixed size) ─────────────────
        frame5 = ttk.Frame(score_page, width=1300, height=200)
        frame5.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        frame5.grid_propagate(False)  # prevents frame from expanding
        frame5.grid_rowconfigure(0, weight=1)
        frame5.grid_rowconfigure(1, weight=0)
        frame5.grid_columnconfigure(0, weight=1)

        tree1 = ttk.Treeview(frame5,
                             columns=("Team","Player","Runs","Balls","1","2","3","4","5","6","Foul","How Out?"),
                             show="headings",
                             height=5)

        tree1.heading("Team",     text="Team")
        tree1.heading("Player",   text="Player")
        tree1.heading("Runs",     text="Runs")
        tree1.heading("Balls",    text="Balls")
        tree1.heading("1",        text="1")
        tree1.heading("2",        text="2")
        tree1.heading("3",        text="3")
        tree1.heading("4",        text="4")
        tree1.heading("5",        text="5")
        tree1.heading("6",        text="6")
        tree1.heading("Foul",     text="Foul")
        tree1.heading("How Out?", text="How Out?")

        tree1.column("Team",     width=100,  minwidth=100)
        tree1.column("Player",   width=200, minwidth=200)
        tree1.column("Runs",     width=100,  minwidth=100)
        tree1.column("Balls",    width=100,  minwidth=100)
        tree1.column("1",        width=80,  minwidth=80)
        tree1.column("2",        width=80,  minwidth=80)
        tree1.column("3",        width=80,  minwidth=80)
        tree1.column("4",        width=80,  minwidth=80)
        tree1.column("5",        width=80,  minwidth=80)
        tree1.column("6",        width=80,  minwidth=80)
        tree1.column("Foul",     width=80,  minwidth=80)
        tree1.column("How Out?", width=120, minwidth=120)

        h_scroll = ttk.Scrollbar(frame5, orient="horizontal", command=tree1.xview)
        v_scroll = ttk.Scrollbar(frame5, orient="vertical",   command=tree1.yview)
        tree1.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        tree1.grid(   row=0, column=0, sticky="ew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        # ── Load DB data ───────────────────────────────────────────
        conn = sqlite3.connect('batsman.db')
        c = conn.cursor()
        c.execute('SELECT TEAM,NAME,RUNS,BALLS,ONES,TWOS,THREES,FOURS,FIVES,SIXES,FOWL,HOWOUT FROM BATSMAN')
        result3 = c.fetchall()
        conn.commit()
        conn.close()

        for row in result3:
            tree1.insert("", "end", values=row)
                #----------we can everytime insert data into treeview 
                #----------but treeview will have to be in every button and its function it'll make the code longer
                #----------that's the correct intuition anyways at the cost of computation.
                #-----------update treeview by Rewriting it---------------------------------------
        def add_1_run():
              conn = sqlite3.connect('batsman.db')
              c = conn.cursor()
              c.execute('UPDATE BATSMAN SET ONES = ONES+1, RUNS = RUNS+1 WHERE NAME = ?', (selected_batsman.get(),))
              conn.commit()
              conn.close()
              
              # clear existing rows first
              for row in tree1.get_children():
                  tree1.delete(row)
              
              # now reinsert fresh data
              conn = sqlite3.connect('batsman.db')
              c = conn.cursor()
              c.execute('SELECT TEAM,NAME,RUNS,BALLS,ONES,TWOS,THREES,FOURS,FIVES,SIXES,FOWL,HOWOUT FROM BATSMAN')
              result3 = c.fetchall()
              conn.close()
              
              for row in result3:
                  tree1.insert("", "end", values=row)
        run_1_button = customtkinter.CTkButton(score_page,text="1",command=add_1_run)   
        run_1_button.grid(row=2,column=0)
#-------- add functions to all the buttons below like above------------------------------------------
        run_2_button = customtkinter.CTkButton(score_page,text="2")   
        run_2_button.grid(row=2,column=1)
        run_3_button = customtkinter.CTkButton(score_page,text="3")   
        run_3_button.grid(row=2,column=2)
        run_4_button = customtkinter.CTkButton(score_page,text="4")   
        run_4_button.grid(row=2,column=3)
        run_5_button = customtkinter.CTkButton(score_page,text="5")   
        run_5_button.grid(row=2,column=4)
        run_6_button = customtkinter.CTkButton(score_page,text="6")   
        run_6_button.grid(row=2,column=5)

start_button = customtkinter.CTkButton(home,text="Start Match",command=game_details)   
start_button.grid(row=3,column=2)

feedback_button = customtkinter.CTkButton(home,text="Help?")     # add command later
feedback_button.grid(row=4,column=0)

home.mainloop()