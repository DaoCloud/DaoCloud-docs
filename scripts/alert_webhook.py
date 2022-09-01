# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import json
import logging

import requests


def alter_webhook(bucket: str = None, message: str = None):
    webhook_url = "https://api.ssp.cloud.tencent.com/engine/webhook/31/1560638495413972994"

    payload = json.dumps({
        "result": "{} : {}".format(bucket or "null", message or "error")
        })

    resp = requests.post(url=webhook_url, data=payload)

    logging.info(resp.json())


if __name__ == '__main__':
    alter_webhook(bucket="community-offical", message="error")
