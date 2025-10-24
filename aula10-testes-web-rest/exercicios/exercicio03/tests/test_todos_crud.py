# tests/test_api_todos_crud_basic.py
import pytest
import requests

@pytest.mark.crud
def test_todos_crud(api_base_url):
    novo_todo = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }

    resposta_post = requests.post(f"{api_base_url}/todos", json=novo_todo, timeout=10)
    assert resposta_post.status_code in (200, 201)
    dados_post = resposta_post.json()

    assert "id" in dados_post
    assert dados_post["title"] == novo_todo["title"]
    assert dados_post["completed"] == novo_todo["completed"]
    assert dados_post["userId"] == novo_todo["userId"]
    # ------------------------------------------------------------------

    # -------------------- READ (GET /todos/1) --------------------
    resposta_get = requests.get(f"{api_base_url}/todos/1", timeout=10)
    assert resposta_get.status_code == 200
    dados_get = resposta_get.json()

    # O objeto deve conter os campos esperados
    assert isinstance(dados_get, dict)
    assert "id" in dados_get
    assert "title" in dados_get
    assert "completed" in dados_get
    assert "userId" in dados_get
    assert dados_get["id"] == 1
    
    # ------------------------------------------------------------------

    # -------------------- UPDATE (PATCH /todos/1) --------------------
    dados_atualizados = {"completed": True}
    resposta_patch = requests.patch(f"{api_base_url}/todos/1", json=dados_atualizados, timeout=10)
    assert resposta_patch.status_code == 200
    dados_patch = resposta_patch.json()

    # O serviço normalmente devolve o campo atualizado
    assert isinstance(dados_patch, dict)
    assert dados_patch.get("completed") is True

    # ------------------------------------------------------------------

    # -------------------- DELETE (DELETE /todos/1) --------------------
    resposta_delete = requests.delete(f"{api_base_url}/todos/1", timeout=10)
    assert resposta_delete.status_code in (200, 204)

    if resposta_delete.status_code == 200:
        corpo_delete = resposta_delete.json()
        assert corpo_delete == {} or corpo_delete is None

    # ------------------------------------------------------------------

    # -------------------- VERIFY (GET /todos/1) --------------------
    resposta_verificacao = requests.get(f"{api_base_url}/todos/1", timeout=10)

    if resposta_verificacao.status_code == 404:
        assert True
    elif resposta_verificacao.status_code == 200:
        dados_verificacao = resposta_verificacao.json()
        assert dados_verificacao == {}
    else:
        assert False

    # ------------------------------------------------------------------