#Faça um programa em python que abra e reproduza o audio de um arquivo MP3

import pygame

pygame.init()

pygame.mixer.music.load('C:\\Users\\rosa\\Music\\pedro.mp3')#cuidado com as \, o python reconhece como scape em strings

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
   pygame.time.Clock().tick(10)