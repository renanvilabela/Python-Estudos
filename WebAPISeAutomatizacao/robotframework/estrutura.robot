*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${variavel1}    teste1
${variavel2}    teste2
${variavel3}    teste3

*** Keywords ***


*** Test Cases ***
Cenário 1: teste de abrir navegador
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Close Browser

Cenário 2: teste de abrir site
    Open Browser    https://www.americanas.com.br/    chrome
    Maximize Browser Window
    Sleep    5s
    Close Browser
    