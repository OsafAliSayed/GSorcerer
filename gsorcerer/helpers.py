import requests
import re
def github_re_filter(organization):
  expressions = [r'^https://github.com/[a-zA-Z0-9]*$']
  for exp in expressions:
    regex = re.compile(exp)
    result = regex.search(organization)
  return False
def get_organizations_info(year, filter=None):
  url = f'https://summerofcode.withgoogle.com/api/program/{year}/organizations/'

  payload = {}
  headers = {
    'authority': 'summerofcode.withgoogle.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'cookie': '_gid=GA1.3.131625652.1705691616; _gat_gtag_UA_53341410_6=1; _ga_DDRZH0K33E=GS1.1.1705737888.20.1.1705738361.0.0.0; _ga=GA1.3.10835740.1703335170',
    'referer': 'https://summerofcode.withgoogle.com/programs/2023/organizations',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Edg/120.0.0.0'
  }
  organizations = requests.request("GET", url, headers=headers, data=payload).json()
  
  if not filter:
    return organizations
  else:
    data = []
    for organization in organizations:
      if filter in organization["source_code"] and github_re_filter(organization["source_code"]):
        data.append(organization)
    return data
      