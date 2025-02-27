import requests
import time
import win32api

def check_server_status():
    url = "https://www.playthroneandliberty.com/de-de/support/server-status"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        if "<span aria-label=\"Fortune server status is Maintenance\"" in response.text:
            return "maintenance"
        else:
            return "online"

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "error"

if __name__ == "__main__":
    while True:
        status = check_server_status()

        if status == "maintenance":
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Server status: Maintenance")

        elif status == "online":
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Server status: Online")
            win32api.MessageBox(0, 'Throne and Liberty is Online', 'Happy', 0x00001000)
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Server status: Error")
            
        time.sleep(30)
