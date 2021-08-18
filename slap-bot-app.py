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

@app.command(SLAP_COMMAND)
def handle_some_command(ack, body, logger):
    ack()
    print(f"<@{body['user_name']}> slapped you!")
    
    logger.info(body)

    rainbow(board)
    playZeldaChest(board)

# Listens to incoming messages that contain "hello"
# To learn available listener method arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click",
                },
            }
        ],
        text=f"Hey there <@{message['user']}>!",
    )


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


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
