import requests


def send_notification(message: str):
    """
    Sends notification via ntfy.sh
    """

    topic = "ravi-nifty-alert"  # you can change this
    url = f"https://ntfy.sh/{topic}"

    try:
        requests.post(url, data=message.encode("utf-8"))
        print(f"NOTIFY: {message}")
    except Exception as e:
        print(f"Notification failed: {e}")
