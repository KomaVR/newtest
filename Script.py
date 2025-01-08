import requests
from requests import get

webhook = "https://discord.com/api/webhooks/1318017746079977513/LZqpasyary0HgGgYR970LnpgyzEgCgusNvB4dQ0XRhwYLBwHzPFH_7G5ud4sS_7iWQ1s"

def handler(request, context):
    try:
        ip = get('https://api.ipify.org').text
        send_to_discord(ip)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"message": "Testing", "ip": ip}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": str(e)}
        }

def send_to_discord(ip):
    message = f"IP Logged: {ip}"
    try:
        requests.post(webhook, json={"content": message})
    except requests.exceptions.RequestException as e:
        print(f"Failed to load: {e}")