import customtkinter
from tkinter import *
import pygame
import os
import mutagen.mp3
from PIL import Image, ImageTk, ImageDraw
import base64
import pymongo
from SongConnect import results


#Initializing Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

#Setting appearance mode
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")


#Global progress bar function
progress_bar = 0

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
def play_song(song_path=os.path.join(music_dir, songs[0])):
    global current_song, current_song_index

    # Extract the song file name from the full path
    current_song = os.path.basename(song_path)

    # Load the song
    pygame.mixer.music.load(song_path)

    # Update the current song index
    current_song_index = songs.index(current_song)

    # Start playing the song
    pygame.mixer.music.play()

# Defining a function to pause the song
def pause_song():
    global current_song

    if current_song is not None:
        pygame.mixer.music.pause()

# Define a function to play the song
def resume_song():
    global current_song

    if current_song is not None:
        pygame.mixer.music.unpause()

# Define a function to play the next song
def next_song():
    global current_song
    print(current_song)
    # Get list of songs
    songs = os.listdir(music_dir)

    print(songs)
    # get current song index
    current_song_index = songs.index(current_song)

    # Increment the song index
    next_song_index = (current_song_index + 1) % len(songs)

    # Play the next song
    play_song(os.path.join(music_dir, songs[next_song_index]))

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

# Function to update the progress of the song
def update_progress():
    global current_song
    global progress_bar
    songs = os.listdir(music_dir)
    current_song_index = songs.index(current_song)
    audioFile = mutagen.mp3.MP3(os.path.join(music_dir, songs[current_song_index]))
    audioFileLength = audioFile.info.length
    if current_song is not None and pygame.mixer.music.get_busy():
        progress_bar_position = (pygame.mixer.music.get_pos()) / 1000
        progress_bar = (progress_bar_position / audioFileLength) * 100
        print(progress_bar)
        # Update the Tkinter slider
        progressSlider.set(progress_bar)
        app.after(1000, update_progress)  # Schedule the next update after 1000 milliseconds

# Master Play button
def master_play():
    global current_song
    global playing
    if current_song == None:
        playing = True
        print(playing)
        play_song()
        update_progress()  # Start updating the progress bar
    elif pygame.mixer.music.get_busy():
        pause_song()
        print(progress_bar)
    else:
        playing = True
        print(playing)
        resume_song()
        print(progress_bar)
        update_progress()  # Start updating the progress bar

#Search bar
def print_entry_text():
    entry_song = entry.get()
    
    # Replace with the actual method to get text from customtkinter entry
    music_dir = "Cadence Tkinter\music"
    songs = os.listdir(music_dir)
    entry_song = entry_song.replace(' ','-')
    entry_song = entry_song+'.mp3'
    print(entry_song)
    for i in songs:
        if i.upper == entry_song.upper():
            print(entry_song)
        else:
            print("enter a valid song name")

# background
canvas = Canvas(app, width=1500, height=800, bg="#404040", relief=FLAT, highlightthickness=0)
canvas.place(relx=0.5, rely=0, anchor=customtkinter.CENTER)
canvas.pack()

# Load the original image
original_image = Image.open("Frontend\post.jpg")

# Resize the original image to the desired size
target_size = (300, 300)
original_image = original_image.resize(target_size, Image.LANCZOS)

# Create a circular mask
mask = Image.new("L", original_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, original_image.size[0], original_image.size[1]), fill=255)

# Create a new image with the desired background color
background_color = "#404040"
background_image = Image.new("RGBA", original_image.size, background_color)

# Resize the circular image to match the resized original image
circular_image = Image.new("RGBA", original_image.size, 0)
circular_image.paste(original_image, mask=mask)

# Paste the circular image onto the background image
final_image = Image.alpha_composite(background_image, circular_image)

# Convert the final image to PhotoImage
final_image = ImageTk.PhotoImage(final_image)

# Create a CTkLabel with the final image
image_label = customtkinter.CTkLabel(app, image=final_image)
image_label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)  # Center the circular image in the window

# background

frame = customtkinter.CTkFrame(master=app, width=1200, height=200, fg_color="#2D2D2D")
frame.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

# Add text above the frame
text_label = Label(app, text="Circles", fg="white", bg="#2D2D2D", font=("Arial", 25))
text_label.place(relx=0.5, rely=0.7, anchor='center')
text_label = Label(app, text="Post malone", fg="white", bg="#2D2D2D", font=("Arial", 14))
text_label.place(relx=0.5, rely=0.75, anchor='center')

# red bg
frame = customtkinter.CTkFrame(master=app, width=1200, height=200, fg_color="#832424")
frame.place(relx=0.5, rely=1, anchor=customtkinter.CENTER)

#Basic Icons
#Play Icon
play_icon = Image.open("Frontend\icons\play.png")
play_icon = play_icon.resize((20, 20))
play_icon_image = customtkinter.CTkImage(play_icon)

# Master Play Button
button = customtkinter.CTkButton(master=app, text="", image=play_icon_image, command=master_play)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

# Next song Button
button = customtkinter.CTkButton(master=app, text="Next", command=next_song)
button.place(relx=0.7, rely=0.9, anchor=customtkinter.CENTER)

# Previous Song Button
button = customtkinter.CTkButton(master=app, text="Previous", command=previous_song)
button.place(relx=0.3, rely=0.9, anchor=customtkinter.CENTER)

#Creating a standard Tkinter slider Slider
progressSlider = customtkinter.CTkSlider(app, from_=0, to=100)
progressSlider.place(relx=0.5,rely = 0.80, anchor= customtkinter.CENTER)

#printing Database results
print(results)

#
entry = customtkinter.CTkEntry(app, placeholder_text="Search Song")
entry.place(relx = 0.5,rely = 0.05, anchor = customtkinter.CENTER)

button = customtkinter.CTkButton(app, text="Enter", command=print_entry_text)
button.place(relx = 0.5,rely = 0.1, anchor = customtkinter.CENTER)

#Initiate Mainloop
app.mainloop()