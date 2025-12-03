Links | 
------|
http://rofull.gnjoy.com/RAG_SETUP_200304.exe
http://rofull.gnjoy.com/ZERO_SETUP_200304.exe
http://rofull.gnjoy.com/RagnarokZero_200304.zip
http://rofull.gnjoy.com/Ragnarok_200304.zip
http://rofull.gnjoy.com/RAG_SETUP_200806.exe
http://rofull.gnjoy.com/ZERO_SETUP_200807.exe
http://rofull.gnjoy.com/Ragnarok_200813.zip
http://rofull.gnjoy.com/ZERO_SETUP_200903.exe
http://rofull.gnjoy.com/RAG_SETUP_200903.exe
http://rofull.gnjoy.com/ZERO_SETUP_201204.exe
http://rofull.gnjoy.com/RAG_SETUP_201204.exe
http://rofull.gnjoy.com/RagnarokZero_210607.zip
http://rofull.gnjoy.com/ZERO_SETUP_210607.exe
http://rofull.gnjoy.com/RAG_SETUP_210607.exe
http://rofull.gnjoy.com/Ragnarok_210607.zip
http://rofull.gnjoy.com/RAG_SETUP_211028_SAK.zip
http://rofull.gnjoy.com/RAG_SETUP_211105.exe
http://rofull.gnjoy.com/ZERO_SETUP_211124.exe
http://rofull.gnjoy.com/RAG_SETUP_220120.exe
http://rofull.gnjoy.com/RAG_SETUP_220307.exe
http://rofull.gnjoy.com/RAG_SETUP_220706.exe
http://rofull.gnjoy.com/ROZ_SETUP_20221021_Sak.zip
http://rofull.gnjoy.com/ZERO_SETUP_221207.exe
http://rofull.gnjoy.com/RagnarokZero_221208.zip
http://rofull.gnjoy.com/RAG_SETUP_240105.exe
http://rofull.gnjoy.com/RAG_SETUP_240108.exe
http://rofull.gnjoy.com/Ragnarok_240418.zip
http://rofull.gnjoy.com/RagnarokZero_240513.zip
http://rofull.gnjoy.com/RAG_SETUP_240610.exe
http://rofull.gnjoy.com/RAG_SETUP_240610-2.bin
http://rofull.gnjoy.com/RAG_SETUP_240610-1.bin
http://rofull.gnjoy.com/RAG_SETUP_240610-3.bin
http://rofull.gnjoy.com/Ragnarok_240610.zip
http://rofull.gnjoy.com/RAG_SETUP_20240809.exe
http://rofull.gnjoy.com/RAG_SETUP_20240809-1.bin
http://rofull.gnjoy.com/RAG_SETUP_20240809-2.bin
http://rofull.gnjoy.com/RAG_SETUP_20240809-3.bin
http://rofull.gnjoy.com/RagnarokZero_250317.zip
http://rofull.gnjoy.com/RAG_SETUP_20250317.exe
http://rofull.gnjoy.com/RAG_SETUP_20250317-1.bin
http://rofull.gnjoy.com/RAG_SETUP_20250317-2.bin
http://rofull.gnjoy.com/Ragnarok_250317.zip
http://rofull.gnjoy.com/RAG_SETUP_20250317-3.bin
http://rofull.gnjoy.com/RAG_SETUP_20250806.exe
http://rofull.gnjoy.com/RAG_SETUP_20250806-1.bin
http://rofull.gnjoy.com/RAG_SETUP_20250806-2.bin
http://rofull.gnjoy.com/RAG_SETUP_20250806-3.bin
http://rofull.gnjoy.com/Ragnarok_250806_2.zip
http://rofull.gnjoy.com/RAG_SETUP_20251002.exe

---

# 📦 RO-Setup-Finder

O **RO Setup Finder** é uma ferramenta desenvolvida para **varrer, identificar e registrar automaticamente links válidos** de instaladores, patches e arquivos antigos do servidor **rofull.gnjoy.com**, gerando uma lista completa de downloads disponíveis.
Ele testa todas as combinações de datas e formatos conhecidos dos arquivos do Kro, Sakray e Zero, incluindo .exe e .zip, e salva os links válidos em um arquivo de texto.

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


