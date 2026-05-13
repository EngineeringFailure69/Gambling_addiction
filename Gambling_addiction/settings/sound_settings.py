import utils.file_utils as file_utils
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import filedialog
import os, shutil, pygame
import const

def load_playlist():
    playlist_loaded = True
    cancel_loading_process = False
    songs = []
    root = tk.Tk()
    root.withdraw()
    songs = filedialog.askopenfilenames()
    root.destroy()
    if songs:
        return playlist_loaded, songs
    else:
        return cancel_loading_process, songs

def play_current_song():
    if const.playlist:
        pygame.mixer.music.stop()
        const.current_song_index %= len(const.playlist)
        song = const.playlist[const.current_song_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(const.MUSIC_END)

def play_music():
    if const.playlist:
        if not pygame.mixer.music.get_busy():
            const.current_song_index = (const.current_song_index + 1) % len(const.playlist)
            play_current_song()

def grab_all_sounds_from_the_music_drectory():
    playlist = []
    path = file_utils.resource_path("assets\\music_files")
    for file in os.listdir(path):
        if file.endswith((".wav", ".mp3", ".midi")):
            file_path = os.path.join(path, file)
            playlist.append(file_path)
    return playlist

def change_music_volume():
    pygame.mixer.music.set_volume(const.music_volume)

def copy_songs_to_directory(playlist):
    for song in playlist:
        shutil.copy2(song, file_utils.resource_path("assets\\music_files"))