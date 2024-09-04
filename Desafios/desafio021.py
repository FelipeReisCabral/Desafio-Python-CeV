# Desafio021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
while True:
   pygame.init()
   pygame.mixer.music.load('desafio021.mp3')
   pygame.mixer_music.play()
   pygame.event.wait()
