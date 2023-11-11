#imports
import pygame
import os

#initializing pygame
pygame.init()
pygame.mixer.init()

#creating the window
screen = pygame.display.set_mode((1200,500))
#title of the application
pygame.display.set_caption("Cadence")
#--------------------*------------------------------------------*-----------------
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



#Start event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space was Pressed")
                play_song(os.path.join(music_dir, songs[0]))  # Play the first song using index 0
            if event.key == pygame.K_RIGHT:
                print("Next")
                next_song()
            if event.key == pygame.K_LEFT:
                print("Previous")
                previous_song()

pygame.quit()
quit()