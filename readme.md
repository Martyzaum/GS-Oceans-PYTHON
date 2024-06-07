# Projeto de Monitoramento da Qualidade da Água

## RMS

    - GUILHERME FERNANDES DE FREITAS - RM554323
    - JOÃO PEDRO CHIZZOLINI DE FREITAS - RM553172

## Descrição do Projeto

Este projeto é um sistema de monitoramento da qualidade da água que gera dados de sensores simulados e disponibiliza esses dados através de uma API. Os sensores simulados geram dados para os seguintes parâmetros: pH, turbidez, nível de água, temperatura e sólidos totais dissolvidos.

## Instruções de Uso

1. Clone o repositório para o seu computador local.
2. Instale as dependências do projeto usando o comando `pip install -r requirements.txt`.
3. Execute o script Python usando o comando `python main.py`.
4. Acesse os dados do sensor através da API em `http://localhost:5000/sensor_data`.

## Requisitos

- Python 3.6 ou superior
- Flask

## Dependências

- Flask: Um microframework para Python usado para desenvolver aplicações web.

## Informações Adicionais

Este projeto foi desenvolvido como parte de uma tarefa de curso. Embora os dados dos sensores sejam gerados aleatoriamente e não representem dados reais de qualidade da água, o sistema foi projetado para simular uma aplicação real de monitoramento da qualidade da água.
