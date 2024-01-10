import os

from circuitplayground import CircuitPlayground
from circuitplayground.pixels import rainbow
from circuitplayground.tones.zelda_songs import playNotificationSong

SERIAL_PORT = os.environ.get("SERIAL_PORT", "COM4")

if __name__ == "__main__":
    board = CircuitPlayground(SERIAL_PORT)
    playNotificationSong(board)
    rainbow(board)
    board.close()
