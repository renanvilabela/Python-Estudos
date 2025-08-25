*** Settings ***
Library    RequestsLibrary  
Library   String

*** Variables ***
${HOST}   https://dummyjson.com

#Rotas
${GET_ALL_PRODUCTS}    products
${GET_SIGLE_PRODUCT}    products/id-produto

*** Keywords ***
Pegar todos os produtos

    &{headers}    Create Dictionary    Content-Type=application/json

    GET    url=${HOST}/${GET_ALL_PRODUCTS}    headers=${headers}

Pegar um único produto de id ${id}

    &{headers}    Create Dictionary    Content-Type=application/json

    ${GET_SIGLE_PRODUCT}=    Replace String    ${GET_SIGLE_PRODUCT}    id-produto    ${id}

    GET    url=${HOST}/${GET_ALL_PRODUCTS}    headers=${headers}
          
*** Test Cases ***
TC01 - Realizar busca de todos os produtos
    Pegar todos os produtos

TC02 - Realizar busca de um único produto
    Pegar um único produto de id 5