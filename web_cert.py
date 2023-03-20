import requests

cert_path = 'path/to/your/certificate.pem'

response = requests.get('https://openai.com', verify=cert_path)

if response.status_code == 200:
    print(response.text)
else:
    print('Failed to scrape website')




"""In this example, the requests.get() method is used to send a GET request to the OpenAI website, and the verify parameter is set to the path of the certificate file. If the request is successful, the HTML content of the website is printed to the console. If the request fails, the message "Failed to scrape website" is printed.

Please note that the path you need to use for the cert_path variable will change according to your local machine or server. Also, it is important to make sure that you have the permission to scrape the website before using this script on a website."""
#Please note that disabling certificate verification is not recommended, as it can open your script to man-in-the-middle attacks.
response = requests.get('https://example.com', verify=False)
"""To add a web certificate to your scraping script, you will need to use a library that supports certificate management, such as the requests library in Python. Here is an example of how you can use the requests library to add a certificate to your script:"""
import requests

cert_path = '/path/to/your/certificate.pem'

response = requests.get('https://example.com', verify=cert_path)
"""In the above example, the verify parameter is set to the path of the certificate file, which tells requests to use the specified certificate when making the request.

You can also specify the path to a directory containing multiple CA certificates. The directory should have hashed symbolic links to the certificate files."""

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

try:
    # send a GET request to the URL
    response = requests.get(url)
    
    # raise an error if the response status code is not 200 (OK)
    response.raise_for_status()
    
except requests.exceptions.RequestException as e:
    # handle exception if the request failed
    print("Request failed:", e)
    raise SystemExit(1)

try:
    # parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    
except Exception as e:
    # handle exception if parsing the HTML failed
    print("Failed to parse HTML:", e)
    raise SystemExit(1)

# now you can extract the data you want from the HTML content using BeautifulSoup methods
...
