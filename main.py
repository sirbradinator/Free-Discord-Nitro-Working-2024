import requests
import random
import string
import time

# Define your Discord webhook URL
discord_webhook_url = "YOUR_DISCORD_WEBHOOK_URL_HERE"

def generate_random_string(length):
    """Generate a random alphanumeric string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_to_discord_webhook(message):
    """Send a message to Discord webhook."""
    payload = {
        "content": message
    }
    requests.post(discord_webhook_url, json=payload)

def check_gift_code(code):
    """Check the gift code with the Discord API."""
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord_webhook(f"Valid gift code found: {code}")
        print(f"Valid gift code found: {code}")
        break
    else:
        print(f"Invalid gift code: {code}")

def main():
    """Main function to generate and check gift codes."""
    print("Welcome to Discord Nitro Gift Code Generator!")
    while True:
        code = generate_random_string(18)
        print(f"Checking gift code: {code}")
        check_gift_code(code)
        print("Waiting for next check...")
        time.sleep(0.1)  # Adjust the delay as needed

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
