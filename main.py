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