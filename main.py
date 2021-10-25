import os
import logging
from pathlib import Path
from datetime import date

import get_pass
import send_email


DIR_NAME = 'saved_passes'
output_image = 'trojan-pass-' + str(date.today()) + '.png'

logging.debug('TrojanPass started in dir="' + str(Path.cwd()) + '", output_image="' + output_image + '"')

# simple environment variable detection
if 'TROJAN_PASS_NETID' not in os.environ:
    logging.error("TROJAN_PASS_NETID not found in environment variables, aborting!")
    logging.error("It is possible that you're using crontab and this requires further setup")

if not Path(DIR_NAME).exists():
    Path("DIR_NAME").mkdir(parents=True, exist_ok=False)
    logging.info('directory "' + DIR_NAME + '" not exists and got created')

next_test_remainder = get_pass.get_pass_and_remainder(output_image)

logging.debug(output_image + ' is saved and next_test_remainder is "' + next_test_remainder + '"')

send_email.send_from_gmail(os.getenv('TROJAN_PASS_NETID') + "@usc.edu",
                           "Your Daily Trojan Pass",
                           next_test_remainder + "\n\nHave a good day! XD",
                           os.path.join(DIR_NAME, output_image),
                           os.getenv('TROJAN_PASS_GMAIL_ACCOUNT'),
                           os.getenv('TROJAN_PASS_GMAIL_PASSWORD'))

logging.info(output_image + " is saved in " + DIR_NAME + " and sent to your mailbox")
