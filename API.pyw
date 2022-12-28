import json
import httpx
import socket
import ssl
import pandas as pd



def Invoke(Call, Parameters={}, Method = 'POST'):
    url=f'https://io.moonlightcompanies.com/{Call}'
    
    try:
        with httpx.Client(verify=False) as client:
            headers={
                'Token': '3E4C792C-E6EC-489D-AEC0-174E057B9DFA'
            }

            r=client.post(url, headers=headers, data=Parameters)

            return r.json()

    except Exception as e:
        print(f'API URL : {url}')
        print(f'API Exception : {e}')

        raise e
