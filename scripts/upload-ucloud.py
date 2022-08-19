# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import logging
import os
import sys
import subprocess


def do_upload_cli(file, public_key, private_key, region):
    cmd = '../scripts/tools/us3cli-linux64'

    if not os.path.exists(cmd):
        print('can not find us3cli command')
        return 'error'

    subprocess.run(['chmod', '+x', cmd])

    if os.path.isdir(file):
        subprocess.run(
            [cmd, 'cp', '-r', file, 'us3://community-github', '--accesskey', public_key, '--secretkey',
             private_key,
             '--endpoint',
             region])
    elif os.path.isfile(file):
        subprocess.run(
            [cmd, 'cp', file, 'us3://community-github', '--accesskey', public_key, '--secretkey', private_key,
             '--endpoint',
             region])


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) != 4:
        logging.error('args not right')
    else:
        public_key = argv[1].strip('public_key=')
        private_key = argv[2].strip('private_key=')
        region = argv[3].strip('region=')

        logging.info(public_key + private_key + region)

        for file in os.listdir():
            logging.info(file)
            print(do_upload_cli(file, public_key, private_key, region))
