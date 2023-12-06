
import requests

from bot_message.shemas import SMessage
from config import IND, TG_BOT_TOKEN, Fore, logger
from libs.text import get_dt_now, get_time_now


class UrlRequest:
    method = None
    url = None
    keyarg_dict = {}

    def __init__(self, method: str = None, url: str = None, **kwargs):
        self.method = method
        self.url = url
        self.keyarg_dict = kwargs

    def __repr__(self) -> str:
        return f'{self.method} -> {self.url}'

    def send(self) -> None:

        if self.method and self.url:

            if self.method == 'post':
                r = requests.post(str(self.url), self.keyarg_dict)
                self.status_code = r.status_code
                # print(f'{IND} {get_time_now()} Reuqest[{self.url}] -> {self.status_code}')

            if self.method == 'get':
                r = requests.get(str(self.url), self.keyarg_dict)
                self.status_code = r.status_code
                # print(f'{IND} {get_time_now()} Reuqest[{self.url}] -> {self.status_code}')

            else:
                print(f'{IND} {get_time_now()} method not correct')

        else:
            print(f'{get_time_now()} {Fore.RED}Request.send() -> not data')


def bot_send_message(user_id, message: SMessage) -> None:

    status_code = 0

    message_text = f'{get_dt_now()}\n{message.message}'

    try:

        if user_id and message:

            url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={user_id}&text={message_text}&parse_mode=html"

            request = UrlRequest(method='get', url=url, timeout=2)
            request.send()

            status_code = request.status_code

            return status_code

    except Exception as e:
        print(f'{Fore.RED} bot_send_message -> error: {e}')
        logger.error(f'{Fore.RED} bot_send_message -> error: {e}')
