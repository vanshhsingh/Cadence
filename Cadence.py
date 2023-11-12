import customtkinter
import pygame
import os

#Initializing Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

#Setting appearance mode
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() #Create a customtkinter window just like you do with tkinter
app.geometry("1200x600")

current_song = None
#Set the music directory
music_dir = "music"

#Get list of all songs 
songs = os.listdir(music_dir)
# print(songs)

# Define a function to play a song
def play_song(song_path):
    global current_song, current_song_index

    # Extract the song file name from the full path
    current_song = os.path.basename(song_path)

    # Load the song
    pygame.mixer.music.load(song_path)

    # Update the current song index
    current_song_index = songs.index(current_song)

    # Start playing the song
    pygame.mixer.music.play()

#Defining a function to pause the song
def pause_song():
    global current_song

    if current_song is not None:
        pygame.mixer.music.pause()

#Define a function to play the song
def resume_song():
    global current_song

    if current_song is not None:
        pygame.mixer.music.unpause()

#Define a function to play the next song
def next_song():
    global current_song
    print(current_song)
    #Get list of songs
    songs = os.listdir(music_dir)
    
    print(songs)
    #get current song index
    current_song_index = songs.index(current_song)

    #Increment the song index 
    next_song_index = (current_song_index + 1) % len(songs)

    #Play the next song
    play_song(os.path.join(music_dir, songs[next_song_index]))

def new_func(current_song_index):
    print(current_song_index)

def previous_song():
    global current_song
    print(current_song)
    # Get the list of songs
    songs = os.listdir(music_dir)
    print(songs)    
    # Get the current song index
    print(current_song)
    current_song_index = songs.index(current_song)

    # Decrement the song index
    previous_song_index = (current_song_index - 1) % len(songs)

    # Play the previous song
    play_song(os.path.join(music_dir, songs[previous_song_index]))


def button_function():
    print("button pressed")

#Use customtkinter buttons insteada of usual tkinter buttons
button = customtkinter.CTkButton(master=app, text = "Play", command=play_song(os.path.join(music_dir, songs[0])))
button.place(relx = 0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text = "Next", command=next_song)
button.place(relx = 0.75, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text = "Previous", command=previous_song)
button.place(relx = 0.25, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()