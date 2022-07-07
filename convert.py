#!/usr/bin/python3

# Logo
logo = ("""
                               _
  ___ ___  _ ____   _____ _ __| |_
 / __/ _ \| '_ \ \ / / _ \ '__| __|
| (_| (_) | | | \ V /  __/ |  | |_
 \___\___/|_| |_|\_/ \___|_|   \__| convert yt to mp3/mp4
       Author : Ghanny
    --------------------
    Tools converting yt
  ------------------------
""")

# importing library/module
import os
from pytube import YouTube
from time import sleep

# Strating

print(logo)
pilih = input("MP3/MP4 : ")

def mp3():
	url = input("URL : ")
	yt = YouTube(url)
	result = yt.streams.filter(only_audio=True).first()
	output_file = result.download("download")
	path, _ = os.path.splitext(output_file)

	os.rename(output_file, path + ".mp3")
	print(yt.title, "Berhasil di download di folder download")

def mp4():
	link = input("URL : ")
	yt = YouTube(link)
	stream = yt.streams.get_highets_resolution()
	stream.download()
	print(yt.title, "Berhasil di download di folder ini")

if pilih == "mp3":
	mp3()
elif pilih == "mp4":
	mp4()

# Done
