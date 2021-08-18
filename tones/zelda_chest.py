# Translated from https://github.com/witnessmenow/attiny85-zelda-chest
import time

notes = "gabygabyxzCDxzCDabywabywzCDEzCDEbywFCDEqywFGDEqi        azbC" # a space represents a rest
beats = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 16]
tempo = 75

def playNote(board, note, duration):
    names = ['c', 'd', 'e', 'f', 'g', 'x', 'a', 'z', 'b', 'C', 'y', 'D', 'w', 'E', 'F', 'q', 'G', 'i']
    # c = C4, C = C5. These values have been tuned.
    tones[] = [1898, 1690, 1500, 1420, 1265, 1194, 1126, 1063, 1001, 947, 893, 843, 795, 749, 710, 668, 630, 594]

    for i in range(18):
        if names[i] == note:
            board.tone(tones[i], duration)

def delay(duration):
    time.sleep(duration / 1000.)

def playZeldaChest(board):
    for i in range(len(notes)):
        if notes[i] == ' ':
            delay(beats[i] * tempo)
        else:
            playNote(board, notes[i], beats[i] * tempo)
        
        # pause between notes
        delay(tempo / 2)
