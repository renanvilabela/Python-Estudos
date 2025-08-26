*** Settings ***
Library    RequestsLibrary  
Library    String

*** Variables ***
${HOST}   https://dummyjson.com

#Rotas
${GET_ALL_PRODUCTS}    products
${GET_SINGLE_PRODUCT}  products/id-produto

*** Keywords ***
Pegar todos os produtos
    &{headers}    Create Dictionary    Content-Type=application/json
    ${response}=    GET    ${HOST}/${GET_ALL_PRODUCTS}    headers=${headers}    expected_status=200
    RETURN    ${response}

Pegar um único produto de id
    [Arguments]    ${id}
    &{headers}    Create Dictionary    Content-Type=application/json

    ${endpoint}=    Replace String    ${GET_SINGLE_PRODUCT}    id-produto    ${id}
    ${response}=    GET    ${HOST}/${endpoint}    headers=${headers}    expected_status=200

    RETURN    ${response}
          
*** Test Cases ***
TC01 - Realizar busca de todos os produtos
    ${response}=    Pegar todos os produtos
    Should Be Equal As Strings    ${response.status_code}    200

TC02 - Realizar busca de um único produto
    ${response}=    Pegar um único produto de id    1
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['title']}    Essence Mascara Lash Princess
    Should Be Equal As Numbers    ${response.json()['price']}    9.99
