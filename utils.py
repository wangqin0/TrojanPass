from datetime import datetime
import os


def str_today():
    return datetime.today().strftime("%Y-%m-%d")


def str_image(net_id: str):
    save_path = os.environ.get('SAVE_PATH') or "saved_passes"
    image_name = f'{net_id}-' + str_today() + '.png'
    return f"{save_path}/{image_name}"


def usc_email_address_for(net_id: str):
    return f"{net_id}@usc.edu"
