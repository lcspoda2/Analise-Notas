def analisar_notas(notas):
    acima_media = []
    abaixo_media = []
    # soma as notas da lista e faz a media
    soma = sum(notas)
    media = soma / len(notas)
    # manda as medias para cada lista conforme a nota
    for n in notas:
        if n >= media:
            acima_media.append(n)
        else:
            abaixo_media.append(n)
    return acima_media, abaixo_media


lista_notas = [9, 2, 3, 4, 5, 6, 7, 8]
 
  # Passa a lista para dentro da funcao
acima, abaixo = analisar_notas(lista_notas)

print(f'Notas acima da media: {acima}')
print(f'Notas abaixo da media: {abaixo}') 
