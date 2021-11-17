import logging
from pathlib import Path
from dotenv import load_dotenv

from send_email import EmailManager
from get_pass import Passer, Driver
from utils import *
from errors import *


def main(send_mail: bool = True):
    load_dotenv()

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s %(message)s')

    save_path = os.environ.get('SAVE_PATH') or 'saved_passes'
    if not Path(save_path).exists():
        Path(save_path).mkdir(parents=True, exist_ok=False)
        logging.info(f'Directory {save_path} not exists and got created')

    # simple environment variable detection
    if 'TROJAN_PASS_NETID' not in os.environ:
        logging.error("TROJAN_PASS_NETID not found in environment variables, aborting!")
        logging.error("It is possible that you're using crontab and this requires further setup")
        exit(1)

    net_ids = [net_id.strip() for net_id in os.environ.get('TROJAN_PASS_NETID').split('|')]
    net_pws = [net_pw.strip() for net_pw in os.environ.get('TROJAN_PASS_PASSWORD').split('|')]
    mail_account = os.environ.get('TROJAN_PASS_GMAIL_ACCOUNT')
    mail_password = os.environ.get('TROJAN_PASS_GMAIL_PASSWORD')

    # Firefox driver with headless mode on
    email_manager = EmailManager(mail_account, mail_password)

    for net_id, net_pw in zip(net_ids, net_pws):
        recipient = usc_email_address_for(net_id)
        email_title = "Trojan Pass"
        content = ""
        image_name = None
        passer = Passer(net_id, net_pw)

        try:
            content = passer.get_pass_and_reminder()
            email_title = "Your Daily Trojan Pass"
            image_name = str_image(net_id)
        except IncorrectPasswordError as e:
            logging.error(e.message + ' for ' + e.net_id)
            content = "Your given password may be wrong, we cannot do Trojan Check for you."
        except SelfAssessmentNotCompliantError as e:
            logging.error(e.message)
            content = "We failed to do wellness assessment for you.\n\n" + e.notification
        except UnexpectedUrlError as e:
            logging.error(f"Unexpected url: {e.url}. Unable to save pass. Exit.")
            logging.error(f"Screenshot saved as {e.image_name}")
        finally:
            del passer.driver

        if send_mail:
            email = EmailManager.construct_email(mail_account, recipient, email_title, content, image_name)
            email_manager.send_email(email)
            logging.info(f"{image_name} is saved in {save_path} and sent to your mailbox")


if __name__ == "__main__":
    main()
