import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Substitua com sua chave de API e endpoint do Azure
subscription_key = os.getenv("API_KEY")
endpoint = os.getenv("ENDPOINT")

# URL para a API de OCR
ocr_url = endpoint + "/vision/v3.2/ocr"

# Número de imagens para processar
QTD_IMGS = 4

# Configuração dos parãmetros para fazer o reconhecimento das imagens
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'detectOrientation': 'true'}

# Lista para armazenar os resultados
all_results = []

# Analisando o texto presente em imagens
for i in range(QTD_IMGS):
    image_path = f'input/img{i}.jpg'

    # Abrir a imagem e enviar para a API
    with open(image_path, 'rb') as image_data:
        response = requests.post(ocr_url, headers=headers, params=params, data=image_data)

    # Verificar a resposta
    if response.status_code == 200:
        result = response.json()
        print(f"Texto reconhecido na imagem {image_path}:")
        
        image_text = []  # Lista para armazenar o texto de cada imagem

        # Extrair o texto das respostas da API
        for region in result.get('regions', []):
            for line in region.get('lines', []):
                line_text = " ".join([word['text'] for word in line['words']])
                image_text.append(line_text)
        
        # Armazenar os resultados da imagem na lista
        all_results.append({
            'image': image_path,
            'text': image_text
        })
        
        # Exibir o texto extraído para esta imagem
        for line_text in image_text:
            print(line_text)
        print("\n--------------\n")
    else:
        print(f"Erro ao processar a imagem {image_path}: {response.status_code}")
        print(response.text)

# Opcional: Salvar os resultados em um arquivo JSON na pasta output
with open('output/resultados.json', 'w') as json_file:
    json.dump(all_results, json_file, indent=4)

print("Fim das análises!")
