import aiohttp
import asyncio
from datetime import datetime, timedelta

data_inicial = datetime(2025, 10, 2)
data_atual = datetime.now()

padroes = [
    "http://rofull.gnjoy.com/ZERO_SETUP_{d6}.exe",
    "http://rofull.gnjoy.com/RagnarokZero_{d6}.zip",
    "http://rofull.gnjoy.com/ROZ_SETUP_{d8}_Sak.zip",
    "http://rofull.gnjoy.com/RAG_SETUP_{d6}.exe",
    "http://rofull.gnjoy.com/RAG_SETUP_{d6}-1.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d6}-2.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d6}-3.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d8}.exe",
    "http://rofull.gnjoy.com/RAG_SETUP_{d8}-1.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d8}-2.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d8}-3.bin",
    "http://rofull.gnjoy.com/RAG_SETUP_{d6}_SAK.zip",
    "http://rofull.gnjoy.com/Ragnarok_{d6}.zip",
    "http://rofull.gnjoy.com/Ragnarok_{d6}_2.zip"
]

SEM_MAX = 6
sem = asyncio.Semaphore(SEM_MAX)


async def testar_url(session, url, arquivo):
    async with sem:  
        await asyncio.sleep(0.15)  # evita bloqueio do servidor
        try:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    print(f"[VALIDO] {url}")
                    arquivo.write(url + "\n")
                else:
                    print(f"[X] {url} -> {resp.status}")
        except Exception as e:
            print(f"[ERRO] {url} -> {e}")


async def main():
    tarefas = []

    with open("links_validos.txt", "w", encoding="utf-8") as arquivo:
        async with aiohttp.ClientSession() as session:

            dia = data_inicial
            while dia <= data_atual:
                d6 = dia.strftime("%y%m%d")
                d8 = dia.strftime("%Y%m%d")

                for padrao in padroes:
                    url = padrao.format(d6=d6, d8=d8)
                    tarefas.append(asyncio.create_task(testar_url(session, url, arquivo)))

                dia += timedelta(days=1)

            await asyncio.gather(*tarefas)

    print("\n Todos os links válidos foram salvos em links_validos.txt")


asyncio.run(main())
