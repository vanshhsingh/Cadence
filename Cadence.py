import customtkinter
import pygame
import os
from PIL import Image, ImageTk

#Initializing Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

#Setting appearance mode
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")



app = customtkinter.CTk() #Create a customtkinter window just like you do with tkinter
app.geometry("1200x600")
app.title("Cadence")
current_song = None
#Set the music directory
music_dir = "music"

#Get list of all songs 
songs = os.listdir(music_dir)
# print(songs)

# Define a function to play a song
def play_song(song_path = os.path.join(music_dir, songs[0])):
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

#Master Play button
def master_play():
    global current_song
    if current_song == None:
        play_song()
    elif pygame.mixer.music.get_busy():
        pause_song()
    else:
        resume_song()
        


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

def update_progress():
    global current_song

    if current_song is not None:
        progress_bar = pygame.mixer.music.get_pos() / pygame.mixer.music.get_length()
        print(progress_bar)

def button_function():
    print("button pressed")


#Basic Icons
#Play Icon
play_icon = Image.open("Frontend\icons\play.png")
play_icon = play_icon.resize((20, 20))
play_icon_image = ImageTk.PhotoImage(play_icon)

#Use customtkinter buttons instead of usual tkinter buttons

#Master Play Button
button = customtkinter.CTkButton(master=app, text="", image=play_icon_image, command=master_play)
button.place(relx = 0.5, rely=0.5, anchor=customtkinter.CENTER)

#Next song Button
button = customtkinter.CTkButton(master=app, text = "Next", command=next_song)
button.place(relx = 0.75, rely=0.5, anchor=customtkinter.CENTER)

#Previous Song Button
button = customtkinter.CTkButton(master=app, text = "Previous", command=previous_song)
button.place(relx = 0.25, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text = "Print Progress", command=update_progress)
button.place(relx = 0.10, rely=0.25, anchor=customtkinter.CENTER)

app.mainloop()