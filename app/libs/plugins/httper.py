"""
Created by Ricky Yang on 24/10/19
@File: httper.py
@Description:
"""
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url, headers={'Connection': 'close'})
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
