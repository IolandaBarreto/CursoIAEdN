'''2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"'''
    
import requests

# URL da API
url = "https://randomuser.me/api/"

# Fazendo a requisição à API
response = requests.get(url)

# Verificando se a resposta foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta para JSON
    data = response.json()
    
    # Extraindo as informações do usuário
    user = data["results"][0]
    nome = f"{user['name']['first']} {user['name']['last']}"
    email = user["email"]
    pais = user["location"]["country"]
    
    # Exibindo as informações
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao obter os dados da API")

    
    


