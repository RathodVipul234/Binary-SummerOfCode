import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory


root = Tk()
root.minsize(768,500)
root.title('Music Player')
root.configure(background='lightblue')


index = 0
history_tracker = []
listofsongs = []
currentsong=''
var = StringVar()


# loads list of songs with .mp3 and .mp4 from choosen directory
def music_player():
    ch = askdirectory()
    os.chdir(ch)

    for files in os.listdir(ch):
        if files.endswith(".mp3") or files.endswith(".mp4"):
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
 

# maintain current song in playing
def update_label():
    global index
    global currentsong
    var.set(listofsongs[listofsongs.index(currentsong)])
    return currentsong


# play the song 
def playsong(event):
    global currentsong
    try:
        pygame.mixer.music.load(listbox.get(ACTIVE))
        currentsong = listbox.get(ACTIVE)
        history_tracker.append(currentsong)
    except pygame.error:
        # if song's path problem or some problem in your song then plays previosly active song only
        playbutton.bind('<Button-1>',playsong)
    pygame.mixer.music.play()
    update_label()


# stop the song
def stopsong():
    currentsong = ''
    pygame.mixer.music.stop()
    var.set('')
    return currentsong


# next song handler
def nextsong():
    global index
    global currentsong
    index += 1

    try:
        pygame.mixer.music.load(listofsongs[listofsongs.index(currentsong)+1])
        currentsong = listofsongs[listofsongs.index(currentsong)+1]
    except IndexError:
        pygame.mixer.music.load(listofsongs[0])
        currentsong = listofsongs[0]
    except ValueError:
        pygame.mixer.music.load(listofsongs[1])
        currentsong = listofsongs[1]

    history_tracker.append(currentsong)
    pygame.mixer.music.play() 
    update_label()


# prevois song handler
def previoussong():
    global index
    global currentsong
    index -= 1

    try:
        pygame.mixer.music.load(listofsongs[listofsongs.index(currentsong)-1])
        currentsong = listofsongs[listofsongs.index(currentsong)-1]
    except:
        pygame.mixer.music.load(listofsongs[-1])
        currentsong = listofsongs[-1]

    history_tracker.append(currentsong)
    pygame.mixer.music.play(listofsongs.index(currentsong)) 
    update_label()


# track history of song played
def songhistory():
    global currentsong
    window = Toplevel(root)
    window.title('History')
    hist_listbox = Listbox(window,width=100,bg='green',fg='white')

    for item in history_tracker:
        hist_listbox.insert(END,item)
    hist_listbox.pack()


# pause current playing song
def pausesong():
    pygame.mixer.music.pause()


# unpause current paused song
def unpausesong():
    pygame.mixer.music.unpause()


# maintain volume of your music player
def volume(val):
    vol = int(val)/100
    pygame.mixer.music.set_volume(vol)


# search song gives information only that searched song present is your playlist or not ?
def song_search():
    global index
    global currentsong
    query = entry.get()

    search_window = Toplevel(root)
    search_window.title('Search')
    search_listbox = Listbox(search_window,width=100,bg='orange',fg='black')

    for song in listofsongs:
        try:
            if query[0].upper() + query[1:] in song:
                search_listbox.insert(END,song)
        except IndexError:
            # if you clicked directly on search button then it takes query='' and shows all the songs available in playlist
            query = ''
            if query in song:
                search_listbox.insert(END,song)
        search_listbox.pack()
    currentsong = search_listbox.get(ACTIVE)


songlabel = Label(root,textvariable=var,width=100,font=('Bold'),bg='lightblue',fg='black')
songlabel.place(x=10,y=365)
music_player()

label = Label(root,text="Music player",padx=2,pady=2,bd=2,font=("Arial",14,"bold")).pack()
scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill = Y)
listbox = Listbox(root, width=100,yscrollcommand= scroll.set,bg='lightgray')
listbox.pack(side = TOP, fill=BOTH)
scroll.config(command=listbox.yview)

listbox.bind('<Double-1>',playsong)
root.bind('<Return>',playsong)
listbox.pack()

listofsongs.reverse()

for item in listofsongs:
    listbox.insert(0,item)

listofsongs.reverse()

playbutton = Button(root,text='►',fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED)
playbutton.place(x=360,y=200)
playbutton.bind('<Button-1>',playsong)
stopbutton = Button(root,text='■',command=stopsong,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=360,y=300)
previousbutton = Button(root,text='◄◄',command=previoussong,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=50,y=250)
nextbutton = Button(root,text='►►',command=nextsong,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=670,y=250)
pausebutton = Button(root,text='║║',command=pausesong,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=250,y=250)
unpausebutton = Button(root,text='Unpause',command=unpausesong,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=470,y=250)
historybutton = Button(root,text='History',command=songhistory,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=50,y=450)
searchbutton = Button(root,text='Search',command=song_search,fg='white',bg='blue',padx=4,pady=4,bd=4,font=("Arial",12,"bold"),relief=RAISED).place(x=560,y=450)


entry = StringVar(root)
e = Entry(root, textvariable=entry, width=25, font=('arial',18), borderwidth=5).place(x=200,y=450)

# cotrols the volume Scale
scale = Scale(root,from_=0,to_=100,orient=VERTICAL,resolution=10,command=volume).place(x=680,y=390)

root.mainloop()