from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import json
import os
STATUS = "Select Input File"
FILE_SELECTED = False
Main_Window = Tk()
NEWTEST = []
import time
Checks_By_Location = [
    [
        "DMC Hammer Grotto",
        "DMC Deku Scrub Grotto Left",
        "DMC Deku Scrub Grotto Center",
        "DMC Deku Scrub Grotto Right"
    ],  #DMC Hammer Grotto
    [
        "DMC Upper Grotto",
        "DMC Upper Grotto Chest"
    ],  #DMC Upper Grotto
    [
        "DMT Storms Grotto",
        "DMT Storms Grotto Chest"
    ],  #DMT Storms Grotto
    [
        "DMT Cow Grotto",
        "DMT Cow Grotto Cow"
    ],  #DMT Cow Grotto
    [
        "Colossus Grotto",
        "Colossus Deku Scrub Grotto Rear",
        "Colossus Deku Scrub Grotto Front"
    ],  #Colossus Grotto
    [
        "GV Storms Grotto",
        "GV Deku Scrub Grotto Rear",
        "GV Deku Scrub Grotto Front"
    ],  #GV Storms Grotto
    [
        "GC Grotto",
        "GC Deku Scrub Grotto Left",
        "GC Deku Scrub Grotto Center",
        "GC Deku Scrub Grotto Right"
    ],  #GC Grotto
    [
        "Graveyard Composers Grave",
        "Song from Composers Grave",
        "Graveyard Composers Grave Chest"
    ],  #Graveyard Composers Grave
    [
        "Graveyard Heart Piece Grave",
        "Graveyard Heart Piece Grave Chest"
    ],  #Graveyard Heart Piece Grave
    [
        "Graveyard Dampes Grave",
        "Graveyard Dampe Race Freestanding PoH",
        "Graveyard Hookshot Chest"
    ],  #Graveyard Dampes Grave
    [
        "Graveyard Shield Grave",
        "Graveyard Shield Grave Chest"
    ],  #Graveyard Shield Grave
    [
        "HC Storms Grotto",
        "HC GS Storms Grotto"
    ],  #HC Storms Grotto
    [
        "HF Cow Grotto",
        "HF GS Cow Grotto",
        "HF Cow Grotto Cow"
    ],  #HF Cow Grotto
    [
        "HF Inside Fence Grotto",
        "HF Deku Scrub Grotto"
    ],  #HF Inside Fence Grotto
    [
        "HF Near Kak Grotto",
        "HF GS Near Kak Grotto"
    ],  #HF Near Kak Grotto
    [
        "HF Near Market Grotto",
        "HF Near Market Grotto Chest"
    ],  #HF Near Market Grotto
    [
        "HF Open Grotto",
        "HF Open Grotto Chest"
    ],  #HF Open Grotto
    [
        "HF Southeast Grotto",
        "HF Southeast Grotto Chest"
    ],  #HF Southeast Grotto
    [
        "HF Tektite Grotto",
        "HF Tektite Grotto Freestanding PoH"
    ],  #HF Tektite Grotto
    [
        "Kak Open Grotto",
        "Kak Open Grotto Chest"
    ],  #Kak Open Grotto
    [
        "Kak Redead Grotto",
        "Kak Redead Grotto Chest"
    ],  #Kak Redead Grotto
    [
        "KF Storms Grotto",
        "KF Storms Grotto Chest",
    ],  #KF Storms Grotto
    [
        "Deku Theater",
        "Deku Theater Skull Mask",
        "Deku Theater Mask Of Truth",
    ],  #Deku Theater
    [
        "LW Scrubs Grotto",
        "LW Deku Scrub Grotto Rear",
        "LW Deku Scrub Grotto Front",
        "LW Scrubs Grotto"
    ],  #LW Scrubs Grotto
    [
        "LH Grotto",
        "LH Deku Scrub Grotto Left",
        "LH Deku Scrub Grotto Center",
        "LH Deku Scrub Grotto Right",
    ],  #LH Grotto
    [
        "LLR Grotto",
        "LLR Deku Scrub Grotto Left",
        "LLR Deku Scrub Grotto Center",
        "LLR Deku Scrub Grotto Right"
    ],  #LLR Grotto
    [
        "LW Near Shortcuts Grotto",
        "LW Near Shortcuts Grotto Chest"
    ],  #LW Near Shortcuts Grotto
    [
        "SFM Wolfos Grotto",
        "SFM Wolfos Grotto Chest"
     ],  #SFM Wolfos Grotto
    [
        "SFM Storms Grotto",
        "SFM Deku Scrub Grotto Rear",
        "SFM Deku Scrub Grotto Front"
    ],  #SFM Storms Grotto
    [
        "ZR Open Grotto",
        "ZR Open Grotto Chest"
    ],  #ZR Open Grotto
    [
        "ZR Storms Grotto",
        "ZR Deku Scrub Grotto Rear",
        "ZR Deku Scrub Grotto Front"
    ],  #ZR Storms Grotto
    [
        "DMT Great Fairy Fountain",
        "DMT Great Fairy Reward"
    ],  #DMT Great Fairy Fountain
    [
        "Colossus Great Fairy Fountain",
        "Colossus Great Fairy Reward"
    ],  #Colossus Great Fairy Fountain
    [
        "OGC Great Fairy Fountain",
        "OGC Great Fairy Reward"
    ],  #OGC Great Fairy Fountain
    [
        "GC Shop",
        "GC Shop Item 1",
        "GC Shop Item 2",
        "GC Shop Item 3",
        "GC Shop Item 4",
        "GC Shop Item 5",
        "GC Shop Item 6",
        "GC Shop Item 7",
        "GC Shop Item 8"
    ],  #GC Shop
    [
        "HC Great Fairy Fountain",
        "HC Great Fairy Reward"
    ],  #HC Great Fairy Fountain
    [
        "Kak Potion Shop Back",
        "Kak Potion Shop Item 1",
        "Kak Potion Shop Item 2",
        "Kak Potion Shop Item 3",
        "Kak Potion Shop Item 4",
        "Kak Potion Shop Item 5",
        "Kak Potion Shop Item 6",
        "Kak Potion Shop Item 7",
        "Kak Potion Shop Item 8"
    ],  #Kak Potion Shop Back
    [
        "Kak Impas House Back",
        "Kak Impas House Cow",
        "Kak Impas House Freestanding PoH"
    ],  #Kak Impas House Back
    [
        "Kak Bazaar",
        "Kak Bazaar Item 1",
        "Kak Bazaar Item 2",
        "Kak Bazaar Item 3",
        "Kak Bazaar Item 4",
        "Kak Bazaar Item 5",
        "Kak Bazaar Item 6",
        "Kak Bazaar Item 7",
        "Kak Bazaar Item 8"
    ],  #Kak Bazaar
    [
        "Kak House of Skulltula",
        "Kak 10 Gold Skulltula Reward",
        "Kak 20 Gold Skulltula Reward",
        "Kak 30 Gold Skulltula Reward",
        "Kak 40 Gold Skulltula Reward",
        "Kak 50 Gold Skulltula Reward"
    ],  #Kak House of Skulltula
    [
        "Kak Impas House",
        "Kak Impas House Cow"
    ],  #Kak Impas House
    [
        "Kak Potion Shop Front",
        "Kak Potion Shop Item 1",
        "Kak Potion Shop Item 2",
        "Kak Potion Shop Item 3",
        "Kak Potion Shop Item 4",
        "Kak Potion Shop Item 5",
        "Kak Potion Shop Item 6",
        "Kak Potion Shop Item 7",
        "Kak Potion Shop Item 8"
    ],  #Kak Potion Shop Front
    [
        "Kak Shooting Gallery",
        "Kak Shooting Gallery"
    ],  #Kak Shooting Gallery
    [
        "Kak Windmill",
        "Song from Windmill",
    ],  #Kak Windmill
    [
        "KF Kokiri Shop",
        "KF Shop Item 1",
        "KF Shop Item 2",
        "KF Shop Item 3",
        "KF Shop Item 4",
        "KF Shop Item 5",
        "KF Shop Item 6",
        "KF Shop Item 7",
        "KF Shop Item 8"
    ],  #KF Kokiri Shop
    [
        "KF Links House",
        "KF Links House Cow"
    ],  #KF Links House
    [
        "KF Midos House",
        "KF Midos Top Left Chest",
        "KF Midos Top Right Chest",
        "KF Midos Bottom Left Chest",
        "KF Midos Bottom Right Chest"
    ],  #KF Midos House
    [
        "LH Fishing Hole",
        "LH Adult Fishing",
        "LH Child Fishing"
    ],  #LH Fishing Hole
    [
        "LH Lab",
        "LH Lab Dive",
        "LH GS Lab Crate"
    ],  #LH Lab
    [
        "LLR Stables",
        "LLR Stables Left Cow",
        "LLR Stables Right Cow"
    ],  #LLR Stables
    [
        "LLR Talons House",
        "LLR Talons Chickens"
    ],  #LLR Talons House
    [
        "LLR Tower",
        "LLR Freestanding PoH",
        "LLR Tower Left Cow",
        "LLR Tower Right Cow"
    ],  #LLR Tower
    [
        "Market Bazaar",
        "Market Bazaar Item 1",
        "Market Bazaar Item 2",
        "Market Bazaar Item 3",
        "Market Bazaar Item 4",
        "Market Bazaar Item 5",
        "Market Bazaar Item 6",
        "Market Bazaar Item 7",
        "Market Bazaar Item 8"
    ],  #Market Bazaar
    [
        "Market Bombchu Bowling",
        "Market Bombchu Bowling First Prize",
        "Market Bombchu Bowling Second Prize"
    ],  #Market Bombchu Bowling
    [
        "Market Bombchu Shop",
        "Market Bombchu Shop Item 1",
        "Market Bombchu Shop Item 2",
        "Market Bombchu Shop Item 3",
        "Market Bombchu Shop Item 4",
        "Market Bombchu Shop Item 5",
        "Market Bombchu Shop Item 6",
        "Market Bombchu Shop Item 7",
        "Market Bombchu Shop Item 8"
    ],  #Market Bombchu Shop
    [
        "Market Potion Shop",
        "Market Potion Shop Item 1",
        "Market Potion Shop Item 2",
        "Market Potion Shop Item 3",
        "Market Potion Shop Item 4",
        "Market Potion Shop Item 5",
        "Market Potion Shop Item 6",
        "Market Potion Shop Item 7",
        "Market Potion Shop Item 8"
    ],  #Market Potion Shop
    [
        "Market Shooting Gallery",
        "Market Shooting Gallery",
    ],  #Market Shooting Gallery
    [
        "Market Treasure Chest Game",
        "Market Treasure Chest Game",
    ],  #Market Treasure Chest Game
    [
        "Market Guard House",
        "Market 10 Big Poes",
        "Market GS Guard House"
    ],  #Market Guard House
    [
        "Temple of Time",
        "Sheik at Temple",
        "ToT Light Arrows Cutscene",
        "Master Sword Pedestal"
    ],  #Temple of Time
    [
        "ZD Shop",
        "ZD Shop Item 1",
        "ZD Shop Item 2",
        "ZD Shop Item 3",
        "ZD Shop Item 4",
        "ZD Shop Item 5",
        "ZD Shop Item 6",
        "ZD Shop Item 7",
        "ZD Shop Item 8"
    ],  #ZD Shop
    [
        "ZF Great Fairy Fountain",
        "ZF Great Fairy Reward"
    ]  #ZF Great Fairy Fountain
]
LOCATION_CONVERT = {
    "DMC Hammer Grotto": None,
    "DMC Upper Grotto": None,
    "DMT Storms Grotto": None,
    "DMT Cow Grotto": None,
    "Colossus Grotto": None,
    "GV Storms Grotto": None,
    "GC Grotto": None,
    "Graveyard Composers Grave": None,
    "Graveyard Heart Piece Grave": None,
    "Graveyard Dampes Grave": None,
    "Graveyard Shield Grave": None,
    "HC Storms Grotto": None,
    "HF Cow Grotto": None,
    "HF Inside Fence Grotto": None,
    "HF Near Kak Grotto": None,
    "HF Near Market Grotto": None,
    "HF Open Grotto": None,
    "HF Southeast Grotto": None,
    "Kak Open Grotto": None,
    "Kak Redead Grotto": None,
    "KF Storms Grotto": None,
    "Deku Theater": None,
    "LW Scrubs Grotto": None,
    "LH Grotto": None,
    "LLR Grotto": None,
    "LW Near Shortcuts Grotto": None,
    "SFM Wolfos Grotto": None,
    "SFM Storms Grotto": None,
    "ZR Open Grotto": None,
    "ZR Storms Grotto:": None,
    "DMT Great Fairy Fountain": None,
    "Colossus Great Fairy Fountain": None,
    "OGC Great Fairy Fountain": None,
    "GC Shop": None,
    "HC Great Fairy Fountain": None,
    "Kak Potion Shop Back": None,
    "Kak Impas House Back": None,
    "Kak Bazaar": None,
    "Kak House of Skulltula": None,
    "Kak Impas House": None,
    "Kak Potion Shop Front": None,
    "Kak Shooting Gallery": None,
    "Kak Windmill": None,
    "KF Kokiri Shop": None,
    "KF Links House": None,
    "KF Midos House": None,
    "LH Fishing Hole": None,
    "LH Lab": None,
    "LLR Stables": None,
    "LLR Talons House": None,
    "LLR Tower": None,
    "Market Bazaar": None,
    "Market Bombchu Bowling": None,
    "Market Bombchu Shop": None,
    "Market Potion Shop": None,
    "Market Shooting Gallery": None,
    "Market Treasure Chest Game": None,
    "Market Guard House": None,
    "Temple of Time": None,
    "ZD Shop": None,
    "ZF Great Fairy Fountain": None
}
Playthrough = []
TEMP = []
# Establishes new file data to be created
FILE_DATA = ["FIXED LOCATIONS"]
ENTRANCE_POINTERS = []
ENTRANCES = []
playthroughloc = []
NEW_ENTRANCES = []


def Fix_Entrances():
    for i in range(len(FILE_DATA)):
        if '"entrances"' in FILE_DATA[i]:
            ENTRANCE_POINTERS.append(i + 1)
        elif '"locations"' in FILE_DATA[i]:
            ENTRANCE_POINTERS.append(i - 1)
    for i in range(len(FILE_DATA)):
        if '":playthrough":' in FILE_DATA[i]:
            playthroughloc.append(i + 1)
        elif 'entrance_playthrough' in FILE_DATA[i]:
            playthroughloc.append(i - 1)
    for i in range(ENTRANCE_POINTERS[0],ENTRANCE_POINTERS[1]):
        ENTRANCES.append(FILE_DATA[i])
    for i in range(playthroughloc[0],playthroughloc[1]):
        Playthrough.append(FILE_DATA[i])
    for i in range(len(ENTRANCES)):
        while '  ' in ENTRANCES[i]:
            ENTRANCES[i] = ENTRANCES[i].replace('  ', ' ')
        ENTRANCES[i] = ENTRANCES[i].split(' -> ')
        if "region" not in ENTRANCES[i][1]:
            p1, p2 = ENTRANCES[i][1].split('": "')
            ENTRANCES[i][1] = p1
            ENTRANCES[i].append(p2)
            NEW_ENTRANCES.append(ENTRANCES[i])
    for i in range(len(Checks_By_Location)):
        for x in range(len(NEW_ENTRANCES)):
            if Checks_By_Location[i][0] in NEW_ENTRANCES[x][2]:
                LOCATION_CONVERT[Checks_By_Location[i][0]] = NEW_ENTRANCES[x][1]
                break
    for i in range(len(Playthrough)):
        TEMP = Playthrough[i].split(":")
        TEMP[0] = TEMP[0].lstrip()
        TEMP[0] = TEMP[0].replace('"', "")
        for x in range(len(Checks_By_Location)):
            if TEMP[0] in Checks_By_Location[x]:
                TEMP2 = Playthrough[i].replace(Checks_By_Location[x][0], LOCATION_CONVERT[Checks_By_Location[x][0]])
                FILE_DATA[i+playthroughloc[0]] = TEMP2
                break



def SAVE_FILE():
    global FILE_SELECTED
    if FILE_SELECTED:
        refreshstatus("Patching")
        Fix_Entrances()
        Main_Window.filename = filedialog.asksaveasfilename(initialdir="/Users/"+os.getlogin()+"/Desktop", title="Save File",
                                                            filetypes=[("Json", '*.json'), ("All files", "*.*")])
        NEW_FILE = open(Main_Window.filename+".json", "w+")
        TEST = 0
        for i in range(len(FILE_DATA)):
            refreshstatus("Patching: "+str(FILE_DATA[TEST]).strip())
            Main_Window.update_idletasks()
            if TEST == 0:
                refreshstatus(FILE_DATA[0])
                NEW_FILE.write(FILE_DATA[0] + "\n")
            else:
                NEW_FILE.write(FILE_DATA[TEST])
            TEST = TEST + 1
        NEW_FILE.close()
        #time.sleep(.1)
        refreshstatus("File Created at: "+str(Main_Window.filename))
        Main_Window.withdraw()
        messagebox.showinfo("SUCCESS", "File created at: "+Main_Window.filename)


def refreshstatus(STAT):
    status = Label(Main_Window, text=str(STAT), bd=1, width=28, relief=SUNKEN, anchor=W)
    status.grid(row=1, column=0, columnspan=3, sticky=W + E)


def SELECT_FILE():
    Main_Window.filename = filedialog.askopenfilename(initialdir="/Users/"+os.getlogin()+"/Desktop",
                                                      title="Select a Spoiler log",
                                                      filetypes=(("json files", "*.json"),("all files", "*.*")))

    FILE_VAR = open(Main_Window.filename, "r")
    for LINE_NUM in FILE_VAR.readlines():
        FILE_DATA.append(LINE_NUM)
        FILE_VAR.close()

    global FILE_SELECTED
    FILE_SELECTED = True
    refreshstatus(Main_Window.filename)



#Main_Window.resizable(width=False, height=False)
Main_Window.geometry("372x58")
Main_Window.title("Randomizer Companion")
screen_height = Main_Window.winfo_screenheight()
screen_width = Main_Window.winfo_screenwidth()
Button_Select_File = Button(Main_Window, text="Select File", width=24, command=SELECT_FILE)
Button_Select_File.grid(row=0,column=0, sticky=W, pady=(0, 10), padx=(5,2.5))
Button_Fix_Entrances = Button(Main_Window, text="Fix Entrances", width=24, command=SAVE_FILE)
Button_Fix_Entrances.grid(row=0,column=2, pady=(0, 10), padx=(2.5,5))
refreshstatus("Select Input File")
Main_Window.mainloop()
