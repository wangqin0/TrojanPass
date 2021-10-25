import os
import get_pass
import send_email

from datetime import datetime
from dotenv import load_dotenv


def do_the_job(str_today):
    # load system environment variables

    net_ids = [str_id.strip() for str_id in os.environ.get('TROJAN_PASS_NETID').split(',')]
    net_pws = [str_pw.strip() for str_pw in os.environ.get('TROJAN_PASS_PASSWORD').split(',')]

    mail_account = os.environ.get('TROJAN_PASS_GMAIL_ACCOUNT')
    mail_password = os.environ.get('TROJAN_PASS_GMAIL_PASSWORD')

    for net_id, net_pw in zip(net_ids, net_pws):
        next_test_remainder = get_pass.get_pass_and_remainder(net_id, net_pw, str_today)

        send_email.send_from_gmail(net_id + "@usc.edu",
                                   "Your Daily Trojan Pass",
                                   next_test_remainder + "\nHave a good day! XD",
                                   str_today,
                                   mail_account,
                                   mail_password)


if __name__ == '__main__':
    load_dotenv()
    do_the_job(datetime.today().strftime("%Y-%m-%d"))
