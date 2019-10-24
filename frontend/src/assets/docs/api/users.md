# Usuários `{base_url}/api/users/`
  * **Métodos:** GET, PUT, PATCH, DELETE, HEAD, OPTIONS

---

> **GET** `/api/users/` (Detalhes de todos os Usuários)

  * **Permissões:** Apenas Administradores
  * **Exemplo:** `{base_url}/api/users/`

  * **Respostas:**

  <div class="table-caption table-success">200 Success (Array de Usuários) ✔️</div>

  | Campo       | Tipo    | Descrição | Exemplo(s) |
  |-------------|---------|---------- | ---------- |
  | url         | string  | URL da API para esse Usuário | `"{base_url}/api/users/3/"` |
  | guides      | string  | URL da API para os Guias desse Usuário  | `"{base_url}/api/users/3/guides/"` |
  | ingame_name | string  | Nome do RuneScape desse Usuário | `"NRiver"` |
  | email        | string  | Email do Usuário | `"admin@rsatlantis.com"` |
  | groups | string[] | Lista de Grupos que o Usuário pertence | `[]`
  | is_staff | boolean | Se o Usuário é Administrador ou Não | `true`
  | is_superuser | boolean | Se o Usuário é um Superuser ou não | `false`
  <br>
  <div class="table-caption table-error">401 Unauthorized (Usuário não-autenticado) ❌</div>
  <br>
  <div class="table-caption table-error">403 Forbidden (Usuário não-admin) ❌</div>

---

> **GET** `/api/users/{id:int}` (Detalhes de um Usuário)
  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | id      | int  | Sim | ID do Usuário | `3` |

  * **Permissões:** Todos
  * **Exemplo:** `{base_url}/api/users/3/`

  * **Respostas:**
  <div class="table-caption table-success">200 Success ✔️</div>

  | Campo       | Tipo    | Descrição | Exemplo(s) |
  |-------------|---------|---------- | ---------- |
  | url         | string  | URL da API para esse Usuário | `"{base_url}/api/users/3/"` |
  | guides      | string  | URL da API para os Guias desse Usuário  | `"{base_url}/api/users/3/guides/"` |
  | ingame_name | string  | Nome do RuneScape desse Usuário | `"NRiver"` |
  | username | string  | Nome do Usuário | `"NRiver"` |
  | email        | string  | Email do Usuário | `"admin@rsatlantis.com"` |
  | groups | string[] | Lista de Grupos que o Usuário pertence | `[]`
  | is_staff | boolean | Se o Usuário é Administrador ou Não | `true`
  | is_superuser | boolean | Se o Usuário é um Superuser ou não | `false`

---

> **POST** `/api/users/` (Criar Usuário)
  * **Permissões:** Todos
  * **Exemplo:** `{base_url}/api/users/`

  <div class="table-caption">Parâmetros JSON</div>

  | Campo    | Tipo   | Obrigatório? | Descrição | Exemplo(s) |
  |----------|--------|--------------|---------- | ---------- |
  | username | string | Sim          | Nome do Usuário | `"NRiver"` |
  | password | string | Sim          | Senha do Usuário | `"@secret#PaSsWoRd123dsdfd"` |
  | email    | string | Sim          | Email do Usuário | `"admin@rsatlantis.com"` |
  | ingame_name | string | Sim | Nome do RuneScape do Usuário | `"NRiver"` |

  * **Respostas:**
  <div class="table-caption table-success">201 Created ✔️</div>
  <br>
  <div class="table-caption table-error">400 Bad Request (Algum Campo inválido) ❌</div>

  | Campo    | Tipo   | Descrição | Exemplo(s) |
  |----------|--------|---------- | ---------- |
  | `<nome do campo inválido (ex.: username)>` | `string[]` | Lista de Erros | `"Este campo não pode ser em branco"` |

---

> **PUT** `/api/users/{id:int}` (Atualizar Usuário)
  * **Permissões:** Administrador ou Próprio Usuário sendo atualizado
  * **Exemplo:** `{base_url}/api/users/3/`

  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | id      | int  | Sim | ID do Usuário | `3` |

  <div class="table-caption">Parâmetros JSON</div>

  | Campo    | Tipo   | Obrigatório? | Descrição | Exemplo(s) |
  |----------|--------|--------------|---------- | ---------- |
  | username | string | Não          | Nome do Usuário | `"NRiver"` |
  | email    | string | Não          | Email do Usuário | `"admin@rsatlantis.com"` |
  | ingame_name | string | Não | Nome do RuneScape do Usuário | `"NRiver"` |

  * **Respostas:**
  <div class="table-caption table-success">200 Success ✔️</div>

  <br>

  <div class="table-caption table-error">403 Forbidden (Não é Admin nem Usuário sendo alterado) ❌</div>

---

> **DELETE** `/api/users/{id:int}` (Deletar Usuário)
  * **Permissões:** Apenas Administradores
  * **Exemplo:** `{base_url}/api/users/3/`

  <div class="table-caption">Parâmetros de URL</div>

  | Parâmetro | Tipo    | Obrigatório? | Descrição | Exemplo(s) |
  |-----------|---------|--------------|---------- | ---------- |
  | id      | int  | Sim | ID do Usuário | `3` |

  * **Respostas:**

  <div class="table-caption table-success">204 No Content ✔️</div>
  <br>
  <div class="table-caption table-error">403 Forbidden (Usuário não-admin) ❌</div>
