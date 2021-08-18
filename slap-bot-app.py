import os, time, atexit
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from circuitplayground import CircuitPlayground
from circuitplayground.tones.zelda_chest import playZeldaChest
from circuitplayground.pixels import rainbow


SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLAP_COMMAND = os.environ.get("SLAP_COMMAND")
SERIAL_PORT = os.environ.get("SERIAL_PORT")

board = None

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN")
)

def do_slap():
    if board:
        rainbow(board)
        playZeldaChest(board)

@app.command(SLAP_COMMAND)
def handle_some_command(ack, body, logger):
    ack(f"Hi <@{body['user_name']}>, I'll slap him for you!")
    print(f"<@{body['user_name']}> slapped you!")
    logger.info(body)
    do_slap()

@atexit.register
def closeboard():
    if board:
        board.close()

# Start your app
if __name__ == "__main__":
    board = CircuitPlayground(SERIAL_PORT)

    # app.start(port=int(os.environ.get("PORT", 3000)))
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, SLACK_BOT_TOKEN)
    handler.start()
