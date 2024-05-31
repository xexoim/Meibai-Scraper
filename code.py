import requests
from bs4 import BeautifulSoup
import json

def fetch_baidu_results(query, num_results=10):
    url = f"https://www.baidu.com/s?wd={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for i, result in enumerate(soup.find_all('div', class_='result'), 1):
            if i > num_results:
                break
            title = result.find('h3').text if result.find('h3') else 'No title'
            link = result.find('a')['href'] if result.find('a') else 'No link'
            description = result.find('div', class_='c-abstract').text if result.find('div', class_='c-abstract') else 'No description'
            results.append({'title': title, 'link': link, 'description': description})
        return results
    else:
        return []

if __name__ == "__main__":
    query = "美白"
    results = fetch_baidu_results(query)
    with open('baidu_meibai_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print("Results saved to baidu_meibai_results.json")
