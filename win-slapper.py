import os, atexit
from circuitplayground import CircuitPlayground
from circuitplayground.tones.zelda_songs import playNotificationSong
from circuitplayground.pixels import rainbow
from notifications import notifications

SERIAL_PORT = os.environ.get("SERIAL_PORT")

board = None

@atexit.register
def closeboard():
    if board:
        board.close()

def notification_listener(app_name, title, body):
    print("\n============\n")
    print("App Name: ", app_name)
    print("Notification title: ", title)
    print(body)
    print("\n============\n")

    if board:
        if "1 minute until this event:" in body:
            playNotificationSong(board)
        rainbow(board)

if __name__ == "__main__":
    SERIAL_PORT="COM4"
    board = CircuitPlayground(SERIAL_PORT)

    rainbow(board)
    playNotificationSong(board)

    notifications(notification_listener)
