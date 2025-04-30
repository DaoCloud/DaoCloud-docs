import os
import yaml
import requests
from datetime import datetime
from tabulate import tabulate

def check_url(base_url, path):
    url = f"{base_url}{path}"
    try:
        resp = requests.get(url, timeout=10, allow_redirects=True)
        return resp.status_code < 400, resp.status_code
    except requests.RequestException:
        return False, 0

def main():
    with open('resources/links-on-ui.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    base_url = os.getenv('DOCS_BASE_URL', 'https://docs.daocloud.io')
    results = []
    
    for url in config.get('compatibility_links', []):
        cn_valid, cn_code = check_url(base_url, url)
        en_valid, en_code = check_url(f"{base_url}/en", url)
        
        cn_url = f"{base_url}{url}"
        en_url = f"{base_url}/en{url}"
        
        cn_status = '✅' if cn_valid else f'❌ ({cn_code})'
        en_status = '✅' if en_valid else f'❌ ({en_code})'
        
        # If both are wrong, use cn_url; if only English, use en_url
        if not cn_valid and not en_valid:
            formatted_url = f"[{url}]({cn_url})"
        elif not en_valid:
            formatted_url = f"[{url}]({en_url})"
        else:
            formatted_url = f"[{url}]({cn_url})"
        
        # print(formatted_url, cn_status, en_status)
        results.append([formatted_url, cn_status, en_status])
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report = [
        f"# Compatibility Links Check Report\n",
        f"Check Time: {current_time}\n",
        "## Results\n\n",
        tabulate(
            results,
            headers=['URL', 'Chinese', 'English'],
            tablefmt='github'
        )
    ]
    
    print('\n'.join(report))

if __name__ == '__main__':
    main()
