# Translated from https://github.com/mitomon/MitosArduinoScripts/tree/master/zeldaSongPlayer
import time
from .pitches import *


def playSong(board, tones, delayMillis):
  for tone, millis in zip(tones, delayMillis):
    board.tone(tone, millis)
    delay(millis)

def delay(duration):
  time.sleep(duration / 1000.)

def playCorrectSong(board):
  correctSongArray = [D5, F5, A5, C6, D6]
  correctSongDelay = [325, 325, 325, 325, 325]
  playSong(board, correctSongArray, correctSongDelay)

def playSariaSong(board):
  sariaSongArray = [F4, A4, B4, F4, A4, B4, F4, A4, B4, E5, D5, B4, C5, B4, G4, E4, D4, E4, G4, E4]
  sariaSongDelay = [250, 250, 500, 250, 250, 500, 250, 250, 250, 250, 500, 250, 250, 250, 250, 625, 250, 250, 250, 750]
  playSong(board, sariaSongArray, sariaSongDelay)

def playZeldaLullaby(board):
  zeldaLullabyArray = [B4, D5, A4, B4, D5, A4, B4, D5, A5, G5, D5, C5, B4, E4]
  zeldaLullabyDelay = [875, 500, 1000, 875, 500, 1000, 875, 500, 1000, 500, 750, 250, 250, 750]
  playSong(board, zeldaLullabyArray, zeldaLullabyDelay)


if __name__ == '__main__':
  from circuitplayground import CircuitPlayground
  import sys

  # Grab the serial port from the command line parameters.
  if len(sys.argv) != 2:
    print('ERROR! Must specify the serial port as command line parameter.')
    sys.exit(-1)
  port = sys.argv[1]

  board = CircuitPlayground(port)
  
  playSariaSong(board)

  board.close()
