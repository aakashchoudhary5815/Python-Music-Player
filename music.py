import os
from pygame import mixer
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3, ID3NoHeaderError
from tkinter import messagebox

listOfSongs =[]
realNames =[]

index = 0

def createWidgets():

    trackLabel = Label(root, text="Select Your Track: ")
    trackLabel.grid(row=0, column=0,  pady=10, padx=10)

    trackEntry = Entry(root, width=40, textvariable = audioTrack)
    trackEntry.grid(row=0, column=1, pady=10, padx=10)

    playBtn = Button(root, text="Play", command=play_music, width=10, bg="#9FEF12")
    playBtn.grid(row=1, column=1, pady=10, padx=10)

    pauseBtn = Button(root, text="Pause", command=pause_music, width=15, bg="#EE126C")
    pauseBtn.grid(row=3, column=0, pady=10, padx=10)

    browseBtn= Button(root, text="Browse", command=browse_music)
    browseBtn.grid(row=0, column=2, pady=10, padx=10)

    resumeBtn = Button(root, text="Resume", command=resume_music, width=15, bg="#57F552")
    resumeBtn.grid(row=2, column=0, pady=10, padx=10)

    stopBtn = Button(root, text="Stop", command=stop_music, width=10, bg="#EF5B12")
    stopBtn.grid(row=2, column=1, pady=10, padx=10)

    volumeUpBtn = Button(root, text="Volume Up", command=volume_up, width = 30, bg="#D812EF")
    volumeUpBtn.grid(row=2, column=2, pady=10, padx=10)

    volumeDown = Button(root, text="Volume Down", command=volume_down, width = 30, bg="#B712EF")
    volumeDown.grid(row=3, column=2, pady=10, padx=10)

    prevBtn = Button(root, text="Previous Song", command=prev_song, width=20, bg="#EFDE12")
    prevBtn.grid(row=1, column=0, pady=10, padx=10)

    nextBtn = Button(root, text="Next Song", command=next_song, width=20, bg="#EFDE12")
    nextBtn.grid(row=1, column=2, pady=10, padx=10)

def play_music():
    
    audioFile = audioTrack.get()

    if audioFile == '':
        messagebox.showerror("ERROR", "NO DIRECTORY SELECTED TO PLAY SONGS!!")

    mixer.music.load(listOfSongs[0])
    mixer.music.set_volume(0.5)
    mixer.music.play()


def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def volume_up():
    mixer.music.set_volume(mixer.music.get_volume()+0.1)

def volume_down():
    mixer.music.set_volume(mixer.music.get_volume()-0.1)

def browse_music():
    audioDir = askdirectory()
    os.chdir(audioDir)
    for files in os.listdir(audioDir):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)

            try:
                audioFile = ID3(realdir)
                realnames.append(audio['TIT2'].text[0])

            except ID3NoHeaderError:
                audioFile = ID3()

            listOfSongs.append(files)
    audioTrack.set(audioDir)

def next_song():
    global index
    index +=1
    mixer.music.load(listOfSongs[index])
    mixer.music.play()

def prev_song():
    global index
    index -=1
    mixer.music.load(listOfSongs[index])
    mixer.music.play()

root = tk.Tk()

root.geometry("700x250")
root.resizable(False,False)
root.title("Python Music Player")
root.configure(background="#3BF6E4")



mixer.init()

audioTrack = StringVar()

createWidgets()

root.mainloop()