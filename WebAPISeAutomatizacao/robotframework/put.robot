*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${HOST}               https://dummyjson.com

#rotas
${UPDATE_PRODUCT}    products/id-produto
${DELETE_PRODUCT}    products/id-produto-delete

*** Keywords ***
Atualizar um produto
    [Arguments]    ${id}    ${title}    ${price}    ${brand}    ${description}=none

    Create Session    api    ${HOST}

    &{headers}    Create Dictionary    Content-Type=application/json
    &{body}       Create Dictionary    title=${title}    description=${description}    price=${price}    brand=${brand}

    ${update_product}=    Replace String    ${UPDATE_PRODUCT}    id-produto    ${id}

    ${response}=    PUT On Session    api    /${update_product}    headers=&{headers}    json=&{body}

    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

Deletar produto de id
    [Arguments]    ${id}
    Create Session    api    ${HOST}
    &{headers}    Create Dictionary    Content-Type=application/json

    ${delete_product}=    Replace String    ${DELETE_PRODUCT}    id-produto-delete    ${id}

    ${response}=    DELETE On Session    api    /${delete_product}    headers=&{headers}

    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

*** Test Cases ***
TC01 - Realizar atualização de um produto
    Atualizar um produto    88    Iphone 13    7000    Apple

TC02 - Realizar deleção de um produto
    Deletar produto de id    88
