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
import time

from alert_webhook import alter_webhook


def do_upload_cli(file, public_key, private_key, region, bucket):
    cmd = '../scripts/tools/us3cli-linux64'

    bucket = 'us3://' + bucket

    if not os.path.exists(cmd):
        logging.error('can not find us3cli command')
        return 'error'

    subprocess.run(['chmod', '+x', cmd])

    if os.path.isdir(file):
        out = subprocess.run(
            [cmd, 'cp', '-r', file, bucket, '--accesskey', public_key, '--secretkey',
             private_key,
             '--endpoint',
             region])
    elif os.path.isfile(file):
        out = subprocess.run(
            [cmd, 'cp', file, bucket, '--accesskey', public_key, '--secretkey', private_key,
             '--endpoint',
             region])

    if out.returncode != 0:
        raise Exception("ucloud upload error", out.returncode)


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) != 5:
        raise Exception('args not right', argv)
    else:
        public_key = argv[1].split('=')[1]
        private_key = argv[2].split('=')[1]
        region = argv[3].split('=')[1]
        bucket = argv[4].split('=')[1]

        logging.debug(public_key + private_key + region + bucket)

        try:
            for file in os.listdir():
                logging.info(file)
                do_upload_cli(file, public_key, private_key, region, bucket)

            alter_webhook(bucket, message="success")

        except Exception as e:
            logging.error(e)
            alter_webhook(bucket, message="error")
