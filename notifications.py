from winsdk.windows.ui.notifications.management import UserNotificationListener
from winsdk.windows.ui.notifications import KnownNotificationBindings

def handle_notification(app_name, title, body):
    print("\n============\n")
    print("App Name: ", app_name)
    print("Notification title: ", title)
    print(body)
    print("\n============")

def notifications(callback):
    def handler(asd, aasd):
        unotification = asd.get_notification(aasd.user_notification_id)
        if hasattr(unotification, "app_info"):
            app_name = unotification.app_info.display_info.display_name

            text_sequence = unotification.notification.visual.get_binding(
                KnownNotificationBindings.toast_generic).get_text_elements()

            it = iter(text_sequence)
            title = it.current.text
            body = []
            while True:
                next(it, None)
                if it.has_current:
                    body.append(it.current.text)
                else:
                    break

            callback(app_name, title, "\n".join(body))
        else:
            pass

    listener = UserNotificationListener.current
    listener.add_notification_changed(handler)

    while True:
        pass

if __name__ == "__main__":
    notifications(handle_notification)
