# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
import logging
import sys
import requests
import hashlib
import collections


def sort_dict(data: dict = None):
    return collections.OrderedDict(sorted(data.items()))


def dict_to_str(data: dict = None):
    data = sort_dict(data)
    return ''.join(['{}{}'.format(k, v) for k, v in data.items()])


def signature(payload, privatekey):
    sign_str = dict_to_str(payload) + privatekey
    return hashlib.sha1(sign_str.encode('utf-8')).hexdigest()


def refresh_cdn_cache(privatekey, publickey, domain):
    url = "https://api.ucloud.cn/?Action=RefreshNewUcdnDomainCache"

    headers = {
        'Content-Type': 'application/json'
        }

    payload = {
        "PublicKey": publickey,
        "Action": "RefreshNewUcdnDomainCache",
        "ProjectId": "org-ismsmp",
        "Type": "dir",
        "UrlList.0": domain
        }

    payload['Signature'] = signature(payload, privatekey)

    resp = requests.post(url, headers=headers, json=payload)

    logging.info("refresh cdn cache respone code: ".format(resp.status_code))


if __name__ == '__main__':
    argv = sys.argv

    publickey = argv[1].split('=')[1]
    privatekey = argv[2].split('=')[1]
    domain = argv[3].split('=')[1]

    refresh_cdn_cache(privatekey, publickey, domain)
