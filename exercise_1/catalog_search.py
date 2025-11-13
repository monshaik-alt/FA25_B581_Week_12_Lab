import pprint
import requests
from credentials import SYMEDICAL_KEY

# API endpoint
url = "https://edu.symedical.com/SymedicalIUSOICRuntime/Catalog"
# Your API token
token = SYMEDICAL_KEY

# Set the headers with the token
headers = {
    "Authorization": f"Bearer {token}"
}


def get_catalog():
    # Send a GET request with token authentication
    response = requests.get(url, headers=headers)
    print(response.url)
    # Check the response
    if response.status_code == 200:
        data = response.json()
        for item in data:
            print(f'Catalog Name: {item.get(f'CatalogName')}')
            print(f'Mnemonic: {item.get(f'Mnemonic')}')
            print(f'TermCount: {item.get(f'TermCount')}')
            print()
    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    get_catalog()