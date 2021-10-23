import os
import get_pass
import send_email

from datetime import date

# simple environment variable detection
assert(len(os.getenv('TROJAN_PASS_NETID')) != 0)

output_image = 'trojan-pass-' + str(date.today()) + '.png'

next_test_remainder = get_pass.get_pass_and_remainder(output_image)

send_email.send_from_gmail(os.getenv('TROJAN_PASS_NETID') + "@usc.edu",
                           "Your Daily Trojan Pass",
                           next_test_remainder + "\nHave a good day! XD",
                           output_image,
                           os.getenv('TROJAN_PASS_GMAIL_ACCOUNT'),
                           os.getenv('TROJAN_PASS_GMAIL_PASSWORD'))
