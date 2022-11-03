import json

import requests
from bot.misc.env import InnoID


def is_authorised(user_id: int) -> bool:
    request = requests.get(f"https://api.innoid.ru/v1/users/{user_id}",
                           headers={"Authorization": f"Bearer {InnoID.app_token}"})
    data: dict = json.loads(request.text)
    is_authorized_json = "is_authorized"
    try:
        if is_authorized_json in data.keys():
            return data[is_authorized_json]
        return False
    except Exception as e:
        raise type(e)(str(e).rstrip() + ': json parsing error in func is_authorised()')
