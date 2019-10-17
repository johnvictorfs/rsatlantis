# Guias `{base_url}/api/guides/`
  * **Métodos:** GET, PUT, PATCH, DELETE, HEAD, OPTIONS

---

## GET `/api/guides/` (Detalhes de todos os Guias)
  * **Permissões:** Todos
  * **Exemplo:** `{base_url}/api/guides/guia-yakamaru`
  * **Respostas:**
    <div class="table-caption success">200 Success (Array de Guias) ✔️</div>

    | Campo       | Tipo    | Descrição | Exemplo(s) |
    |-------------|---------|---------- | ---------- |
    | url         | string  | URL da API para esse Guia | `"{base_url}/api/guides/guia-yakamaru/"` |
    | author      | string  | URL da API para esse Usuário  | `"{base_url}/api/users/23/"` |
    | title       | string  | Título do Guia | `"Guia Yakamaru"` |
    | slug        | string  | Versão slug do Título | `"guia-yakamaru"` |
    | category    | string  | Categoria do Guia | `"pvm"` / `"skilling"` / `"other"` |
    | description | string  | Descrição do Guia | `"Como matar o Boss Yakamaru"` |
    | content     | string  | Conteúdo do Guia, em Markdown | `"## Piscina Stun \n (.......) ## Piscina Tendrils \n (.......)"` |
    | approved    | boolean | Se o Guia foi aprovado pela Administração para ser vísivel | `true` / `false` |
    | date_posted | string  | Data que o Guia foi postado | `"2019-06-13T01:27:32.728805Z"` |

---

## GET `/guides/{slug:str}/` (Detalhes de um Guia)
  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | slug      | string  | Sim | Slug do título do Guia | `guia-yakamaru` |

  * **Permissões:** Todos
  * **Exemplo:** `{base_url}/api/guides/guia-yakamaru`
  * **Respostas:**
    <div class="table-caption success">200 Success ✔️</div>

    | Campo       | Tipo    | Descrição | Exemplo(s) |
    |-------------|---------|---------- | ---------- |
    | url         | string  | URL da API para esse Guia | `"{base_url}/api/guides/guia-yakamaru/"` |
    | author      | string  | URL da API para esse Usuário  | `"{base_url}/api/users/23/"` |
    | title       | string  | Título do Guia | `"Guia Yakamaru"` |
    | slug        | string  | Versão slug do Título | `"guia-yakamaru"` |
    | category    | string  | Categoria do Guia | `"pvm"` / `"skilling"` / `"other"` |
    | description | string  | Descrição do Guia | `"Como matar o Boss Yakamaru"` |
    | content     | string  | Conteúdo do Guia, em Markdown | `"## Piscina Stun \n (.......) ## Piscina Tendrils \n (.......)"` |
    | approved    | boolean | Se o Guia foi aprovado pela Administração para ser vísivel | `true` / `false` |
    | date_posted | string  | Data que o Guia foi postado | `"2019-06-13T01:27:32.728805Z"` |

    <div class="table-caption error">404 Not Found ❌</div>

    | Campo       | Tipo    | Descrição | Exemplo(s) |
    |-------------|---------|---------- | ---------- |
    | detail      | string  | Descrição do Erro | `"Não encontrado."` |

---

## POST `/guides/` (Criar Novo Guia)
  * **Permissões:** Requer Usuário Autenticado

  <div class="table-caption">Parâmetros JSON</div>

  | Campo       | Tipo    |  Obrigatório? | Descrição | Exemplo(s) |
  |-------------|---------|---------------|---------- | ---------- |
  | title       | string  | Sim           | Título do Guia | `"Guia Yakamaru"` |
  | category    | string  | Sim           | Categoria do Guia | `"pvm"` / `"skilling"` / `"other"` |
  | description | string  | Sim           | Descrição do Guia | `"Como matar o Boss Yakamaru"` |
  | content     | string  | Sim           | Conteúdo do Guia, em Markdown | `"## Piscina Stun \n (.......) ## Piscina Tendrils \n (.......)"` |

  * **Respostas:**
    <div class="table-caption success">201 Created ✔️</div>
    <br>
    <div class="table-caption error">401 Unauthorized (Usuário não-autenticado ou inativo) ❌</div>

---

## PUT `/guides/{slug:str}` (Atualizar Guia)

  * **Permissões:** Requer Usuário Autenticado que seja Administrador ou Criador do Guia sendo alterado

  <div class="table-caption">Parâmetros JSON</div>

  | Campo       | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-------------|---------|--------------|---------- | ---------- |
  | title       | string  | Não          | Título do Guia | `"Guia Yakamaru"` |
  | category    | string  | Não          | Categoria do Guia | `"pvm"` / `"skilling"` / `"other"` |
  | description | string  | Não          | Descrição do Guia | `"Como matar o Boss Yakamaru"` |
  | content     | string  | Não          | Conteúdo do Guia, em Markdown | `"## Piscina Stun \n (.......) ## Piscina Tendrils \n (.......)"` |

  * **Respostas:**
    <div class="table-caption success">200 Success ✔️</div>
    <br>
    <div class="table-caption error">401 Unauthorized (Usuário não-autenticado) ❌</div>
    <br>
    <div class="table-caption error">403 Forbidden (Usuário / não-autor / não-admin / inativo) ❌</div>

---

## DELETE `/guides/{slug:str}` (Deletar Guia)
  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | slug      | string  | Sim | Slug do título do Guia | `guia-yakamaru` |

  * **Permissões:** Requer Usuário Autenticado que seja Administrador ou Criador do Guia sendo deletado

  * **Respostas:**
    <div class="table-caption success">204 No Content ✔️</div>
    <br>
    <div class="table-caption error">401 Unauthorized (Usuário não-autenticado) ❌</div>
    <br>
    <div class="table-caption error">403 Forbidden (Usuário não-autor / não-admin / inativo) ❌</div>

---

## POST `/guides/{slug:str}/approve/` (Aprovar Guia existente)
  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | slug      | string  | Sim | Slug do título do Guia | `guia-yakamaru` |

  * **Permissões:** Requer Usuário Autenticado que seja Administrador ou Criador do Guia sendo deletado

  * **Respostas:**
    <div class="table-caption success">200 Success ✔️</div>
    <br>
    <div class="table-caption error">401 Unauthorized (Usuário não-autenticado) ❌</div>
    <br>
    <div class="table-caption error">403 Forbidden (Usuário não-autor / não-admin / inativo) ❌</div>
