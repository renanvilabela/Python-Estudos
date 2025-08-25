*** Settings ***
Library    RequestsLibrary
Library    String

*** Variables ***
${HOST}               https://dummyjson.com

#rotas
${UPDATE_PRODUCT}    products/id-produto

*** Keywords ***
Atualizar um produto
    [Arguments]    ${id}    ${title}    ${description}    ${price}    ${brand}

    Create Session    api    ${HOST}

    &{headers}    Create Dictionary    Content-Type=application/json
    &{body}       Create Dictionary    title=${title}    description=${description}    price=${price}    brand=${brand}

    ${update_product}=    Replace String    ${UPDATE_PRODUCT}    id-produto    ${id}

    ${response}=    PUT On Session    api    /${update_product}    headers=&{headers}    json=&{body}

    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

*** Test Cases ***
TC01 - Realizar atualização de um produto
    Atualizar um produto    88    Iphone 13    Celular Apple    7000    Apple
