"""
    Faça um programa em Python que abra e reproduza o audio de um arquivo MP3.
"""

import pygame

pygame.init()

pygame.mixer.music.load('exerc021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('\n===== EXERCÍCIO 21 ======\n')

print('-'*100)



print('-'*100)