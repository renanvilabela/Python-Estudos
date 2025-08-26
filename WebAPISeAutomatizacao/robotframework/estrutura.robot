*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${variavel1}    teste1
${variavel2}    teste2
${variavel3}    teste3

*** Keywords ***
abrir navegador
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window


fechar navegador
    Close Browser


abrir site americanas
    Open Browser    https://www.americanas.com.br/    chrome
    Maximize Browser Window
    Sleep    5s


*** Test Cases ***
Cenário 1: teste de abrir navegador
    abrir navegador
    fechar navegador

Cenário 2: teste de abrir site
    abrir site americanas
    fechar navegador
    
    