#imports
import pygame
import os
import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.slider import MDSlider
from kivy.uix.image import Image
# #title of the application
# pygame.display.set_caption("Cadence")

#--------------------*------------------------------------------*-----------------
global current_song
current_song = None
    #Set the music directory
global music_dir
music_dir = "music"

    #Get list of all songs 
global songs
songs = os.listdir(music_dir)
    # print(songs)


#creating the window
Window.size = (320,600)
class MusicScreen(Screen):
        
    def Next(self):
        next_song()
        print("pressed")
    def Play(self):
        play_song(os.path.join(music_dir, songs[0]))
        print("pressed")  # Play the first song using index 0
    pass
class SongCover(MDBoxLayout):


    def rotate(self):
        pass
    def Play(self):
        pass
class MainApp(MDApp):
    title = 'Cadence'
    def build(self):
        screen = MusicScreen()
        return screen


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
    

# Defining a function to pause the song
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

# Define a function to play the previous song
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