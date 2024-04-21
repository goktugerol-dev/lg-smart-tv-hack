import requests

def send_command(tv_ip, command):
    base_url = f"http://{tv_ip}:TV_PORT"  # Change port number
    try:
        response = requests.post(f"{base_url}/roap/api/command", json={"command": command})
        response.raise_for_status()
        print(f"Command '{command}' sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending command '{command}': {e}")

# def turn_on_tv(tv_ip):
    # send_command(tv_ip, "poweron")

def turn_off_tv(tv_ip):
    send_command(tv_ip, "poweroff")

# Example usage
tv_ip_address = "TV_IP_ADDRESS"  # Replace with your TV's IP address
# turn_on_tv(tv_ip_address)
# Wait for the TV to turn on or do other operations
turn_off_tv(tv_ip_address)
