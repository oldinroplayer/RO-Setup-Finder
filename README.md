

---

# 📦 RO-Setup-Finder

O **RO Setup Finder** é uma ferramenta desenvolvida para **varrer, identificar e registrar automaticamente links válidos** de instaladores, patches e arquivos antigos do servidor **rofull.gnjoy.com**, gerando uma lista completa de downloads disponíveis.

---

## 🔍 Funcionalidades

* ✅ Teste automático de múltiplos padrões de URL
* ✅ Geração dinâmica de datas (YYMMDD / YYYYMMDD)
* ✅ Varredura completa entre intervalo de anos
* ✅ Execução assíncrona com controle de limite de conexões
* ✅ Salvamento automático dos links válidos
* ✅ Detecção de erros e tentativas seguras
* ✅ Evita bloqueios do servidor utilizando delays inteligentes
* ✔ Ideal para localizar instaladores antigos ou ocultos

---

## 🚀 Como funciona

O programa gera URLs a partir de padrões como:

```
http://rofull.gnjoy.com/ZERO_SETUP_YYMMDD.exe
http://rofull.gnjoy.com/RagnarokZero_YYMMDD.zip
http://rofull.gnjoy.com/ROZ_SETUP_YYYYMMDD_Sak.zip
http://rofull.gnjoy.com/RAG_SETUP_YYMMDD.exe
http://rofull.gnjoy.com/RAG_SETUP_YYMMDD_SAK.zip
http://rofull.gnjoy.com/Ragnarok_YYMMDD.zip
```

E faz testes assíncronos usando `aiohttp`, limitando as conexões e evitando flood.

Links válidos são gravados automaticamente em:

```
links_validos.txt
```

---

## ⚡ Tecnologias utilizadas

* **Python 3.9+**
* **asyncio**
* **aiohttp**

---

## 📄 Requisitos

Instalar dependências:

```bash
pip install aiohttp
```

---

## 🏁 Execução

Rodar o script:

```bash
python3 rosetupfinder.py
```

---

## 🗂 Saída gerada

O arquivo `links_validos.txt` conterá:

```
http://rofull.gnjoy.com/ZERO_SETUP_230105.exe
http://rofull.gnjoy.com/RagnarokZero_220607.zip
...
```

---

## 📌 Aviso

O programa **não baixa** nenhum arquivo — apenas testa disponibilidade.
Ideal para fins de catalogação, preservação e estudo.

---


