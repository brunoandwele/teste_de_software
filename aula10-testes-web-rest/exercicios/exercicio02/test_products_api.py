import requests
def test_listar_produtos():
    response = requests.get("https://fakestoreapi.com/products")

    categorias_esperadas = {"electronics", "jewelery", "men's clothing", "women's clothing"}
    categorias_encontradas = set()
    #Verificar status codes
    assert response.status_code == 200, f"Status code: {response.status_code}"

    #verificar schema
    assert len(response.json()) > 0, "Nenhum produto foi encontrado"
    assert isinstance(response.json(), list), "Resposta não é do tipo list"
    assert "id" in response.json()[0], "Campo id não encontrado"
    assert "title" in response.json()[0], "Campo title não encontrado"
    assert "price" in response.json()[0], "Campo price não encontrado"
    assert "description" in response.json()[0], "Campo description não encontrado"
    assert "category" in response.json()[0], "Campo category não encontrado"
    assert "image" in response.json()[0], "Campo image não encontrado"
    assert "rating" in response.json()[0], "Campo rating não encontrado"

    print("Estrutura válida\n")

    # verificar Categorias disponíveis
    for produto in response.json():
        assert produto["id"], f"Campo Id inválida para: {produto}"
        assert produto["title"], f"Campo title inválida para: {produto}"
        assert produto["price"], f"Campo price inválida para: {produto}"
        assert produto["description"], f"Campo description inválida para: {produto}"
        assert produto["category"], f"Campo category inválida para: {produto}"
        assert produto["image"], f"Campo image inválida para: {produto}"
        assert produto["rating"], f"Campo rating inválida para: {produto}"
        assert produto["rating"]['rate'], f"Campo rate inválida para: {produto}"
        assert produto["rating"]["count"], f"Campo count inválida para: {produto}"

        categorias_encontradas.add(produto["category"])
    
    assert categorias_encontradas == categorias_esperadas, (
        f"Categorias diferentes do esperado.\n"
        f"Encontradas: {sorted(categorias_encontradas)}\n"
        f"Esperadas:   {sorted(categorias_esperadas)}"
    )

    print(f"Números de produtos encontrados: {len(response.json())}" )

def test_buscar_produto_id():
    response = requests.get("https://fakestoreapi.com/products")

    assert response.status_code == 200, f"Status code: {response.status_code}"

    for produto in response.json():
        id = produto["id"]

        response_produto = requests.get(f"https://fakestoreapi.com/products/{id}")

        assert response_produto.status_code == 200 , f"Status code: {response_produto.status_code} para o produto ID: {id}"

        assert produto["id"] == id, f"ID do produto não corresponde para o produto ID: {id}"
    print("Busca de todos os produtos por id feita!")

def test_filtrar_produtos_categoria():
    response = requests.get("https://fakestoreapi.com/products")

    assert response.status_code == 200, f"Status code: {response.status_code}"


    response_categorias = requests.get(f"https://fakestoreapi.com/products/categories")

    assert response_categorias.status_code == 200 , f"Status code: {response_categorias.status_code}"

    categorias = response_categorias.json()
    assert isinstance(categorias, list), f"Tipo inesperado: {type(categorias)}"

    esperadas = {"electronics", "jewelery", "men's clothing", "women's clothing"}
    for cat in esperadas:
        assert cat in categorias, f"Faltou a categoria{cat}"

    for produto in response.json():
        assert produto["category"], f"Campo category inválida para: {produto}"
        print(produto['category'])

    print("Busca de todos os produtos por category feita!")

def test_validar_schema_da_resposta():
    schema = {
        "id": int,
        "title": str,
        "price": float,
        "description": str,
        "category": str,
        "image": str,  # URL
        "rating": {
            "rate": float,
            "count": int,
        },
    }

    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200, f"Status code: {response.status_code}"

    reposta = response.json()

    assert isinstance(reposta, list), "A resposta da API deve ser uma lista de produtos."

    for produto in reposta:
        assert isinstance(produto, dict), f"O item não é um dicionário, mas sim {type(produto)}"
        assert isinstance(produto['id'],int), f"O id do produto é do tipo: {type(produto['id'])}"
        assert isinstance(produto['title'],str), f"O title do produto é do tipo: {type(produto['title'])}"
        assert isinstance(produto['price'],(int, float)), f"O price do produto é do tipo: {type(produto['price'])}"
        assert isinstance(produto['description'],str), f"O description do produto é do tipo: {type(produto['description'])}"
        assert isinstance(produto['category'],str), f"O category do produto é do tipo: {type(produto['category'])}"
        assert isinstance(produto['image'],str), f"O image do produto é do tipo: {type(produto['image'])}"
        assert isinstance(produto['rating'],dict), f"O rating do produto é do tipo: {type(produto['rating'])}"
        assert isinstance(produto['rating']['rate'],(int,float)), f"O rate do dicionário rating é do tipo: {type(produto['rating']['rate'])}"
        assert isinstance(produto['rating']['count'],int), f"O count do dicionário rating é do tipo: {type(produto['rating']['rate'])}"
    
    print("Schema válido")

def test_limite_de_produtos_retornados():
    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200, f"Status code: {response.status_code}"

    limite_maximo = 20

    assert len(response.json()) <= limite_maximo, f"Número de produtos retornados excede o limite de {limite_maximo}"
    print(f"Dentro do limite de {limite_maximo}")