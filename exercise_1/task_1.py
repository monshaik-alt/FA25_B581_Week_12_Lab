from pprint import pprint
import requests
from credentials import SYMEDICAL_KEY

# API endpoint
url = "https://edu.symedical.com/SymedicalIUSOICRuntime/Term/list"
params = {
    "catalogIdentifier": "SYM_SNO_INT_USEXT",
    "codes": ['195967001'],
    'includeAttributes': True,
    'includeDomainChars': False
}

# Your API token
token = SYMEDICAL_KEY

# Set the headers with the token
headers = {
    "Authorization": f"Bearer {token}"
}


def get_term_list():
    # Send a GET request with token authentication
    global data
    response = requests.get(url, headers=headers, params=params)
    print(response.url)
    # Check the response
    if response.status_code == 200:
        data = response.json()

    for item in data:
        print(f"\nTermDescription: {item['TermDescription']}")
        print(f"TermSourceCode: {item['TermSourceCode']}")

    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    get_term_list()

