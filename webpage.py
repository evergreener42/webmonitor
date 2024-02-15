import requests
from bs4 import BeautifulSoup
import smtplib
import subprocess

def run_linux_command(command):
    try:
        # Execute the Linux command
        command = "/home/johns/webmonitor/twilio.sh"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Print the output (stdout and stderr)
        print("Command output:")
        print(result.stdout)
        print("Error (if any):")
        print(result.stderr)
    except Exception as e:
        print(f"Error executing the command: {e}")


def search_for_whale(url):
    try:
        # Fetch the webpage content

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

        response = requests.get(url, headers=headers)
        #response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        with open("output.txt", "w") as file:
            file.write(str(soup))  # Convert soup to a string before writing

        # Search for the string "whale" in the page
        if 'Whale' in soup.get_text().lower():
            run_linux_command('Orca')
            print("Found 'Orca whale' in West Seattle Blog.")
        else:
            print("No 'orca whale' found on the webpage.")
        if 'orca' in soup.get_text().lower():
            run_linux_command('Orca')
            print("Found 'Orca whale' in West Seattle Blog.")
        else:
            print("No 'Orca whale' found on the webpage.")
        if 'umpback' in soup.get_text().lower():
            run_linux_command('Humpback')
            print("Found 'humpback whale' in West Seattle Blog.")
        else:
            print("No 'humpback whale' found on the webpage.")

    except Exception as e:
        print(f"Error: {e}")


def send_email():
    # Replace with your actual email configuration

# Example usage
if __name__ == "__main__":
    webpage_url = "https://www.orcanetwork.org/recent-sightings"  # Replace with the actual webpage URL
    webpage_url = "https://westseattleblog.com/"  # Replace with the actual webpage URL
    search_for_whale(webpage_url)

