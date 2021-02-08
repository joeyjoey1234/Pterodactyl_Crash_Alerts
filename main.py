import subprocess
import time

import requests

clear = 'echo " " > /var/log/pterodactyl/wings.log'
subprocess.call(clear, shell=True)

mailbox_Name = ''  ###https://api.mailgun.net/v3/BLAHBLAHBLAH.mailgun.org
from_who = ''  ### "Mailgun Sandbox <postmaster@BLAHBLAHBLAH.mailgun.org>"
to_who = ''  ### Example bob jones <bob.jones@coolemail.com>
api_key = ''  ### your api key

f = open('/var/log/pterodactyl/wings.log', 'r')


def send_simple_message(message, subject):
    return requests.post(
        "{}/messages".format(mailbox_Name),
        auth=("api", api_key),
        files=[("attachment", open('/var/log/pterodactyl/wings.log'))],
        data={"from": from_who,
              "to": to_who,
              "subject": subject,
              "text": message})


def process(x):
    if 'ERROR' in x:
        send_simple_message(x, 'Error on Atomic')
        print('sending error')
    elif 'crashed' in x:
        send_simple_message(x, 'Container Crash on Atomic')
        print('sending Crash email')
    elif 'stacktrace' in x:
        send_simple_message(x, 'Stacktrace on Nitro ')
        print('sending Crash email')
    else:
        pass


while True:
    line = ''
    while len(line) == 0 or line[-1] != '\n':
        tail = f.readline()
        if tail == '':
            time.sleep(0.2)
            continue
        line += tail
    process(line)
