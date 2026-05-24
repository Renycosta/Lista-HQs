import csv
HQs = []

with open("HQs.csv", mode="r", encoding="utf-8") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        HQs.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("-"*40)

def top10_melhores_notas():
    titulo("Top 10 HQs com as melhores notas")

    ordenar = sorted(HQs, key=lambda hq: float(hq['Rating'] or 0), reverse=True)

    print(f"{'Nº':2s} | {'ID':10s} | {'Título':35s} | {'Editora':30s} | {'Nota':4s}")
    print("-" * 75)

    for x, hq in enumerate(ordenar[0:10], start=1):
        nota = float(hq['Rating'] or 0)
        print(f"{i:2d} | {hq['comic_id']:10s} | {hq['Title']:35s} | {hq['Studio/Publisher']:30s} | {nota:4.1f}")

def HQs_premiadas():
    titulo("HQs premiadas")
    premios_agrupados = {}

    for hq in HQs:
        if hq['Awards'] != "None":
            premio = hq['Awards']
            if premio not in premios_agrupados:
                premios_agrupados[premio] = []
            premios_agrupados[premio].append(hq['Title'])

    for nome_premio, lista_titulos in premios_agrupados.items():
        print(f"\nPrêmio: {nome_premio.upper()}")
        for titulo_hq in lista_titulos:
            print(f"  -> {titulo_hq}")

    titulo("HQs não premiadas")
    nao_premiadas = [hq for hq in HQs if hq['Awards'] == "None"]
    nao_premiadas.sort(key=lambda x: x['Title'])

    print(f"{'Nº':2s} | {'Título':35s} | {'Ano':4s} | {'Nota':4s} | {'Status'}")
    print("-" * 70)
    for i, hq in enumerate(nao_premiadas[:50], start=1):
        print(f"{i:2d} | {hq['Title']:35s} | {hq['Release Year']:4s} | {float(hq['Rating']):4.1f} | N/A")

def analisar_marca():
    titulo("Analisar marca específica")

    nome_busca = input("Digite o nome da marca (Studio/Publisher): ")

    titulos_encontrados = []
    soma_notas = 0.0
    total_volumes = 0
    contador = 0

    for hq in HQs:
        if hq['Studio/Publisher'].strip().lower() == nome_busca.strip().lower():
            titulos_encontrados.append(hq['Title'])
            soma_notas += float(hq['Rating'])
            total_volumes += int(hq['Volume Count'])
            contador += 1

    if contador > 0:
        media_notas = soma_notas / contador
        
        print(f"\nResultados para '{nome_busca}':")
        print(f"Quantidade de HQs encontradas: {contador}")
        print(f"Média de notas: {media_notas:.2f}")
        print(f"Total de volumes publicados: {total_volumes}")
        print("Títulos encontrados:")
        for x in titulos_encontrados:
            print(f"- {x}")
    else:
        print("\nMarca não encontrada ou sem HQs cadastradas.")

def comparar_marcas():
    titulo("Comparação entre duas marcas")
    
    marca1_nome = input("Digite o nome da primeira marca: ")
    marca2_nome = input("Digite o nome da segunda marca: ")

    titulos1 = {hq['Title'] for hq in HQs if hq['Studio/Publisher'].lower() == marca1_nome.lower()}
    titulos2 = {hq['Title'] for hq in HQs if hq['Studio/Publisher'].lower() == marca2_nome.lower()}

    comuns = titulos1.intersection(titulos2)
    exclusivos1 = titulos1.difference(titulos2)
    exclusivos2 = titulos2.difference(titulos1)

    print(f"\n--- Comparação: {marca1_nome} vs {marca2_nome} ---")    
    print(f"\nTítulos em comum ({len(comuns)}):")
    for t in comuns: print(f" * {t}")
    print(f"\nTítulos exclusivos de {marca1_nome} ({len(exclusivos1)}):")
    for t in exclusivos1: print(f" * {t}")
    print(f"\nTítulos exclusivos de {marca2_nome} ({len(exclusivos2)}):")
    for t in exclusivos2: print(f" * {t}")

while True:
    titulo("Jogadores do brazileirão")
    print("1. Top 10 HQs com melhores notas")
    print("2. HQs prêmiadas")
    print("3. Analisar marca especifica")
    print("4. Comparar 2 marcas entre si")
    print("5. Comparação de quantidade volumes por marcas")
    print("6. Comparar os gêneros das HQs")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top10_melhores_notas()
    elif opcao == 2:
        HQs_premiadas()
    elif opcao == 3:
        analisar_marca()
    elif opcao == 4:
        comparar_marcas()
    elif opcao == 5:
        comparar_volumes()
    elif opcao == 6:
        comparar_generos()
    else:
        break