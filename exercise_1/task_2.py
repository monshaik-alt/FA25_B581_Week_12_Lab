from pprint import pprint
import requests
from credentials import SYMEDICAL_KEY

# API endpoint
url = "https://edu.symedical.com/SymedicalIUSOICRuntime/Term/list"
params = {
    "catalogIdentifier": "SYM_NLM_RXNORM",
    "codes": ['860975', '5640'],
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
    response = requests.get(url, headers=headers, params=params)
    print(response.url)
    # Check the response
    if response.status_code == 200:
        data = response.json()

       for item in data:
            print(f"\nCatalogDisplayName: {item['CatalogDisplayName']}")
            print(f"PreferredDescription: {item['PreferredDescription']}")
            print(f"TermSourceCode: {item['TermSourceCode']}")


    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    get_term_list()
