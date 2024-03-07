import os

from circuitplayground import CircuitPlayground
from circuitplayground.pixels import rainbow

SERIAL_PORT = os.environ.get("SERIAL_PORT", "COM4")

if __name__ == "__main__":
    board = CircuitPlayground(SERIAL_PORT)
    rainbow(board)
    board.close()
