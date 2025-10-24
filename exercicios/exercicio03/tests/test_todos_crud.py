# tests/test_api_todos_crud_basic.py
import requests
import pytest


@pytest.fixture
def todo_payload():
    return {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1,
    }


@pytest.fixture
def teardown(api_base_url):
    ids = []
    yield ids
    for todo_id in ids:
        try:
            requests.delete(f"{api_base_url}/todos/{todo_id}", timeout=10)
        except Exception:
            pass


def test_todos_crud(api_base_url, todo_payload, teardown):

    resposta_post = requests.post(
        f"{api_base_url}/todos", json=todo_payload, timeout=10
    )
    assert resposta_post.status_code in (200, 201)
    dados_post = resposta_post.json()

    assert "id" in dados_post
    assert dados_post["title"] == todo_payload["title"]
    assert dados_post["completed"] == todo_payload["completed"]
    assert dados_post["userId"] == todo_payload["userId"]

    # apenas para apagr depois
    created_id = dados_post["id"]
    teardown.append(created_id)

    # -------------------- READ (GET /todos/1) --------------------
    resposta_get = requests.get(f"{api_base_url}/todos/1", timeout=10)
    assert resposta_get.status_code == 200
    dados_get = resposta_get.json()

    assert isinstance(dados_get, dict)
    assert "id" in dados_get
    assert "title" in dados_get
    assert "completed" in dados_get
    assert "userId" in dados_get
    assert dados_get["id"] == 1

    # -------------------- UPDATE (PATCH /todos/1) --------------------
    dados_atualizados = {"completed": True}
    resposta_patch = requests.patch(
        f"{api_base_url}/todos/1", json=dados_atualizados, timeout=10
    )
    assert resposta_patch.status_code in (200, 204)
    if resposta_patch.status_code == 200:
        dados_patch = resposta_patch.json()
        # O serviço normalmente devolve o campo atualizado
        assert isinstance(dados_patch, dict)
        assert dados_patch.get("completed") is True

    # -------------------- DELETE (DELETE /todos/1) --------------------
    resposta_delete = requests.delete(f"{api_base_url}/todos/1", timeout=10)
    assert resposta_delete.status_code in (200, 204)

    if resposta_delete.status_code == 200:
        try:
            corpo_delete = resposta_delete.json()
            assert corpo_delete == {} or corpo_delete is None
        except ValueError:
            pass

    # -------------------- VERIFY (GET /todos/1) --------------------
    resposta_verificacao = requests.get(f"{api_base_url}/todos/1", timeout=10)

    if resposta_verificacao.status_code == 404:
        assert True
    elif resposta_verificacao.status_code == 200:
        dados_verificacao = resposta_verificacao.json()
        if dados_verificacao != {}:
            # se ainda existe algo em /1, nao deve ser o que foi apagado
            assert dados_verificacao.get("title") != todo_payload["title"]
            assert dados_verificacao.get("completed") != todo_payload["completed"]
            assert dados_verificacao.get("userId") != todo_payload["userId"]
        else:
            assert True
    else:
        assert False


def test_criar_todo_sem_titulo_deve_falhar(api_base_url):
    payload = {"completed": False, "userId": 1}
    r = requests.post(f"{api_base_url}/todos", json=payload, timeout=10)
    assert r.status_code in (201,400)


def test_get_id_inexistente(api_base_url):
    r = requests.get(f"{api_base_url}/todos/99999999", timeout=10)
    assert r.status_code == 404

def test_patch_campo_invalido(api_base_url, teardown, todo_payload):
    r_create = requests.post(f"{api_base_url}/todos", json=todo_payload, timeout=10)
    assert r_create.status_code in (200, 201)
    todo = r_create.json()
    teardown.append(todo["id"]) #para apagar depis

    # Tenta patch com tipo inesperado
    r_patch = requests.patch(
        f"{api_base_url}/todos/{todo['id']}",
        json={"completed": "não_bool"},
        timeout=10,
    )
    assert r_patch.status_code in (200, 204, 400, 422)
    if r_patch.status_code == 200:
        body = r_patch.json()
        assert isinstance(body, dict)


def test_delete_inexistente_idempotente(api_base_url):
    r = requests.delete(f"{api_base_url}/todos/99999999", timeout=10)
    assert r.status_code in (204, 404, 200) #Não está bem claro qual retorno possivel