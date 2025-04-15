import requests

webhook_url = 'https://discord.com/api/webhooks/1361597917319790704/Zl5r59KE47NyswnZbStWBnOUcfHydvRNw0SdEMXDB6tV0ra-4-x548MiecWYg1BzC7kL'
data = {
    "content": "Hello from webhook!"
}

response = requests.post(webhook_url, json=data)
