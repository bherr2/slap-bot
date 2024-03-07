from subprocess import run

from notifications import notifications


def notification_listener(app_name, title, body):
    print("\n============\n")
    print("App Name:", app_name)
    print("Notification title:", title)
    print(body)
    print("\n============")

    if "1 minute until this event:" in body:
        run(['python', 'win-slapper-slap.py'])


if __name__ == "__main__":
    run(['python', 'win-slapper-say-hi.py'])
    notifications(notification_listener)
