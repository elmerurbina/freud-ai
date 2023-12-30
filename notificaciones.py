from plyer import  notification
from frases import ramdom_phrase



def show_notification(title, message):
    notification.notify(
        title="Freud AI",
        message=ramdom_phrase(),
        app_icon=None,
        timeout=10
    )