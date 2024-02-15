import requests
from bs4 import BeautifulSoup
import smtplib
def search_for_whale(url):
    try:
        # Fetch the webpage content

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

        response = requests.get(url, headers=headers)
        #response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

#        with open("output.txt", "w") as file:
#            file.write(str(soup))  # Convert soup to a string before writing

        # Search for the string "whale" in the page
        if 'Orca' in soup.get_text().lower():
            send_email('Orca')
            print("Found 'Orca whale' in West Seattle Blog.")
        else:
            print("No 'orca whale' found on the webpage.")
        if 'orca' in soup.get_text().lower():
            send_email('Orca')
            print("Found 'Orca whale' in West Seattle Blog.")
        else:
            print("No 'Orca whale' found on the webpage.")
        if 'umpback' in soup.get_text().lower():
            send_email('Humpback')
            print("Found 'humpback whale' in West Seattle Blog.")
        else:
            print("No 'humpback whale' found on the webpage.")

    except Exception as e:
        print(f"Error: {e}")


def send_email():
    # Replace with your actual email configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    recipient_email = 'jds@example.com'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        subject = "Whale Alert!"
        body = "The string 'whale' was found on the webpage."

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    webpage_url = "https://www.orcanetwork.org/recent-sightings"  # Replace with the actual webpage URL
    webpage_url = "https://westseattleblog.com/"  # Replace with the actual webpage URL
    search_for_whale(webpage_url)

