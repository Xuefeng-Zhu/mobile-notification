from gcm import GCM
gcm = GCM('AIzaSyAJ882Hvz_hEacehne7TOIYn-uUvT0LI9s')


def send_notification(receivers=None, message):
    for receiver in receivers:
        if receiver[0] is "android":
            send_android_notification(receiver[1], message)


def send_android_notification(device_token, message):
    data = {'message': message}
    gcm.plaintext_request(registration_id=device_token, data)
