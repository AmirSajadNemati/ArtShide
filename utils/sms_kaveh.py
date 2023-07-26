from kavenegar import *


def send_activation_code_sms(receptor, message):
    try:
        api = KavenegarAPI('554E4F4E59644341524A536346747071434F392B616962666275655244737A4366706E53396B4A6A5032493D')
        params = {
            'sender': '',  # optional
            'receptor': receptor,
            'message': message,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e.args)
    except HTTPException as e:
        print(e)
