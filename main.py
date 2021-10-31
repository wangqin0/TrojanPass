import logging
from pathlib import Path
from utils import *

from get_pass import Passer, Driver
from dotenv import load_dotenv
import send_email


def main():
    load_dotenv()

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s %(message)s')

    save_path = os.environ.get('SAVE_PATH') or 'saved_passes'
    if not Path(save_path).exists():
        Path(save_path).mkdir(parents=True, exist_ok=False)
        logging.info(f'directory {save_path} not exists and got created')

    # simple environment variable detection
    if 'TROJAN_PASS_NETID' not in os.environ:
        logging.error("TROJAN_PASS_NETID not found in environment variables, aborting!")
        logging.error("It is possible that you're using crontab and this requires further setup")
        exit(1)

    net_ids = [net_id.strip() for net_id in os.environ.get('TROJAN_PASS_NETID').split(',')]
    net_pws = [net_pw.strip() for net_pw in os.environ.get('TROJAN_PASS_PASSWORD').split(',')]
    mail_account = os.environ.get('TROJAN_PASS_GMAIL_ACCOUNT')
    mail_password = os.environ.get('TROJAN_PASS_GMAIL_PASSWORD')

    # Firefox driver with headless mode on
    driver = Driver()

    for net_id, net_pw in zip(net_ids, net_pws):
        image_name = str_image(net_id)
        logging.debug(f'TrojanPass started in dir={Path.cwd()}, output_image={image_name}')

        passer = Passer(net_id, net_pw, driver=driver)

        remind_text = passer.get_pass_and_reminder()
        logging.debug(f'{image_name} is saved and next_test_reminnder is {remind_text}')

        send_email.send_from_gmail(os.getenv('TROJAN_PASS_NETID') + "@usc.edu",
                                   "Your Daily Trojan Pass",
                                   remind_text + "\n\nHave a good day! XD",
                                   image_name,
                                   mail_account,
                                   mail_password)

        logging.info(f"{image_name} is saved in {save_path} and sent to your mailbox")


if __name__ == "__main__":
    main()
