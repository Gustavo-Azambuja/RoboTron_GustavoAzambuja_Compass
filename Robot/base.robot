*** Settings ***
Documentation    Arquivo simples para requisicoes HTTP em APIs Rest
Library          RequestsLibrary
Resource         usuarios_keywords.robot    
Resource         produtos_keywords.robot
Resource         login_keywords.robot

*** Variables ***
${URL} =     http://localhost:3000
&{login}=    email=fulano@qa.com    password=teste       
${response}
${user_id}  


#token dura 10 minutos
*** Test Cases ***
Cenario: POST Realizar Login 200
    [tags]    POSTLOGIN
    Criar Sessao
    POST Endpoint /login
    Validar Status Code "200"

Cenario: GET Todos os usuarios 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint /usuarios
    Validar Status Code "200"
    Validar Quantidade "${3}"
    Printar Conteudo Response

Cenario: POST cadastrar Usuario 201
    [Tags]    POST    
    Criar Sessao
    POST Endpoint /usuarios
    Validar Status Code "201"
    Validar Se Mensagem Contem "sucesso"

Cenario: PUT Editar Usuario 200
    [Tags]    PUT
    Criar Sessao
    PUT Endpoint /usuarios
    Validar Status Code "200"

Cenario: DELETE Deletar Usuario 200
    [Tags]    DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"

Cenario: GET produto por Id 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint /produtos/"BeeJh5lz3k6kSIzA"
    Validar Status Code "200"

Cenario: POST Cadastrar Usuario 201
    [Tags]    POST
    Criar Sessao
    POST Endpoint /Usuarios
    Validar Status Code "201"
    Validar Se Mensagem Contem "sucesso"

Cenario: PUT Editar Usuario Criado 200
    [Tags]    PUT
    Criar Sessao
    PUT Endpoint /Usuarios
    Validar Status Code "200"
    
Cenario: DELETE Usuario Editado 200
    [Tags]    DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"

*** Keywords ***
Criar Sessao
    Create Session    serverest     https://serverest.dev

GET Endpoint /usuarios
    ${response}            GET On Session    serverest    /usuarios
    Set Global Variable    ${response}

POST Endpoint /usuarios
    &{payload}        Create Dictionary        nome=jerson priest    email=testejersonp123@gmail.com        password=123        administrador=true
    ${response}        POST On Session    serverest    /usuarios        data=&{payload}
    Log To console    Response: ${response.content} 
    Set Global Variable    ${response}

Validar Status Code "${statuscode}"
    Should Be True    ${response.status_code} == ${statuscode}

Validar Quantidade "${quantidade}" 
    Should Be Equal    ${response.json()["quantidade"]}    ${quantidade}

DELETE Endpoint /usuarios
    ${response}    DELETE On Session    serverest    /usuarios/BuDTuUzJKv8EohZI
    Log To console    Response: ${response.content}
    Set Global Variable    ${response} 

Validar Se Mensagem Contem "${palavra}"
    Should Contain    ${response.json()["message"]}    ${palavra}

Printar Conteudo Response
    Log To Console    Response: ${response.json()["usuarios"][0]["nome"]}
PUT Endpoint /usuarios
    &{payload}        Create Dictionary        nome=jade priest    email=testejadep123@gmail.com        password=123        administrador=true
    ${response}    PUT On Session    serverest    /usuarios/BuDTuUzJKv8EohZI    data=&{payload}
    Log To console    Response: ${response.content} 
    Set Global Variable    ${response}
POST Endpoint /login
    &{payload}        Create Dictionary    nome=jade marg     email=testejadep123@gmail.com            password=123        administrador=true    
    ${response}        POST On Session        serverest    /login
    Set Global Variable    ${response}
GET Endpoint /produtos
    &{payload}        Create Dictionary        nome=jade priest    email=testejadep123@gmail.com        password=123        administrador=true
    ${response}         GET On Session    serverest        /produtos/"BeeJh5lz3k6kSIzA"    data=&{payload}
    Log To console    Response: ${response.content} 
    Set Global Variable    ${response}
