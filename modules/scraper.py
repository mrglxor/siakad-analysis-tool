import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_data(data_type, url,output_directory):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    response_time = end_time - start_time

    print(f"Waktu Respons: {response_time} detik")

    if response.status_code == 200:
        print("Permintaan berhasil")
        soup = BeautifulSoup(response.text, 'html.parser')

        if data_type == 'url':
            data = [a['href'] for a in soup.find_all('a', href=True)]
        elif data_type == 'img':
            data = [img['src'] for img in soup.find_all('img', src=True)]
        elif data_type == 'text':
            data = [p.get_text() for p in soup.find_all('p')]
        elif data_type == 'title':
            data = soup.title.string
        elif data_type == 'meta_description':
            data = soup.find('meta', attrs={'name': 'description'})['content']
        elif data_type == 'specific_links':
            data = [a['href'] for a in soup.find_all('a', class_='your_class')]
        elif data_type == 'table_data':
            table_data = []
            for table in soup.find_all('table'):
                for row in table.find_all('tr'):
                    table_data.append([cell.get_text() for cell in row.find_all('td')])
            data = table_data
        else:
            print(f"Data type '{data_type}' not recognized.")
            return

        output_file_path = f'{output_directory}pengumpulan-data-{data_type}.json'
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        print(f"Data {data_type} berhasil disimpan di {output_file_path}")
    else:
        print(f"Permintaan gagal dengan kode status {response.status_code}")