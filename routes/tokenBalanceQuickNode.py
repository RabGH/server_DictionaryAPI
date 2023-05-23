import requests
import json


def get_wallet_token_balance(address):
    url = "https://methodical-warmhearted-morning.discover.quiknode.pro/6cb4bd4175910fea967b7db58f5032321293eda1/"

    payload = json.dumps({
      "id": 67,
      "jsonrpc": "2.0",
      "method": "qn_getWalletTokenBalance",
      "params": [
        {
          "wallet": address
        }
      ]
    })

    headers = {
        'Content-Type': 'application/json',
        'x-qn-api-version': '1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()
