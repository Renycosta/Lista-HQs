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

    notas = [x for x in HQs]
    ordenar = sorted(notas, key=lambda hq: float(hq['Rating']), reverse=True)

    for x, hq in enumerate(ordenar[0:10], start=1):
        nota = float(hq['Rating'])
        print(f"{x:2d} {hq['Title']:20s} {hq['Studio/Publisher']:20s} {nota:4.1f} {hq['comic_id']}")

def HQs_premiadas():
    premio = {}
    n_premio = {}

    for x in HQs:
        if x['Awards'] == "None":
            nome = x["Title"]
            n_premio[nome] = n_premio.get(nome, 'Nenhum')
        else:
            nome = x["Title"] 
            award = x["Awards"]
            premio[nome] = premio.get(nome, award)

    pre_ordenar = sorted(premio.items(), key=lambda val: val[1], reverse=True)
    n_pre_ordenar = sorted(n_premio.items(), key=lambda val: val[1], reverse=True)

    titulo("HQs prêmiadas")
    for x, (nome, award) in enumerate(pre_ordenar[0:10], start=1):
        print(f"{x:2d} {nome:20s} {award:20s}")

    titulo("HQs não prêmiadas")
    for x, (nome, award) in enumerate(n_pre_ordenar[0:10], start=1):
        print(f"{x:2d} {nome:20s} {award:20s}")

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