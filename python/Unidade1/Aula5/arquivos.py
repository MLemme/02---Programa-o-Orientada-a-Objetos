#abre o arquivo, e indica método de escrita - w substiui o conteudo ; a+ anexa conteudo novo
#open cria o arquivo se não existir
arquivo = open('pessoas.txt','w') # aramazena o arquivo em memória

#escreve no arquivo
arquivo.write('Mauricio\n')
arquivo.write('Milton\n')
arquivo.write('Myrna\n')

#fecha o arquivo liberando a memória
arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura: #permite o tratamento do arquivo em bloco fechando ao sair
    for linha in arquivoLeitura:
        print(linha)