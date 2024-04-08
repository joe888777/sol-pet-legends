import requests
import json
from dateutil import parser

def timestamp_to_unixTime(timestamp):
  utc_dt = parser.parse(timestamp)
  unix_time  = utc_dt.timestamp()
  return int(unix_time)
             


def get_tx_history(address):
  tx_info = []
  response = request_api(address)
  res = json.loads(response.text)
  
  for i in res['result']:
    info = {"txHash": i['signatures'][0], "unix_time": timestamp_to_unixTime(i['timestamp'])}
    tx_info.append(info)

  return tx_info

def request_api(address):
  url = f"https://api.shyft.to/sol/v1/transaction/history?network=mainnet-beta&tx_num=10&account={address}&enable_raw=false"
  payload={}
  headers = {
    'x-api-key': 'y_OMZq-GM-yxttQP'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  return response


if __name__ == "__main__":
  address = 'GFDnrt7ykCc5T8DhrdswVHqve5XaRCgWfKtG9PneoR8a'

  print(get_tx_history(address))