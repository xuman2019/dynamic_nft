# lambda_function.py

import requests
import json
from datetime import datetime

API_KEY = "4a6df8ce-1ff1-4290-835d-d9300367e731"

# Replace with your metadata URIs
MORNING_URI = "ipfs://bafkreia6byr6cffpnxyvdnoy3doto7juqxmij2i3belwoedngrqucmdaji" 
AFTERNOON_URI = "ipfs://bafkreidfxtqwe74jjp3cfl2u6zqmf2dbjqzbzmvilsfn5qif5o4g2dacli"
NIGHT_URI = "ipfs://bafkreicbusyqreeyofijktof45w2w3wrs5qlchhopn4ymlkew6cps34rpi"
URL = "https://api.nftport.xyz/v0/mints/customizable"
    
    
def lambda_handler(event, context):
    time = datetime.now().hour
    if time >=8 and time <16:
        metadata_uri = MORNING_URI
    elif time >=16 and time<20:
        metadata_uri = AFTERNOON_URI
    else:
        metadata_uri = NIGHT_URI

    # Replace with the contract_address you got from 1 A and token_ID from 1 D
    payload = {
                "chain":"polygon",
                "contract_address": "0xc129030bb284034665dcadb290e23c6dbbb68f91",
                "token_id": "1",
                "metadata_uri": metadata_uri
        
    }
    headers = {
                "Content-Type": "application/json",
                "Authorization": API_KEY
    }
    response = requests.request("PUT", URL, data=json.dumps(payload), headers=headers)
    return {
        'statusCode': 200,
        'body': json.dumps(response.json())
    }
