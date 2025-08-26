*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${HOST}               https://dummyjson.com
${ADD_NEW_PRODUCT}    products/add

*** Keywords ***
Adicionar um novo produto
    Create Session    api    ${HOST}
    &{headers}    Create Dictionary    Content-Type=application/json
    ${body}    Create Dictionary    title=Galaxy S20    description=Celular Samsung    price=2500    brand=Samsung
    
    ${response}    POST On Session    api    ${ADD_NEW_PRODUCT}    headers=&{headers}    json=${body}
    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

*** Test Cases ***
TC01 - Realizar adição de um novo produto
    Adicionar um novo produto
