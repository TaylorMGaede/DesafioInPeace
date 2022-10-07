import sys

##escreverNovoArquivo##
#função que copia o arquivo1 para o arquivo2 alterando a cor de uma variável do arquivo
def escreverNovoArquivo(arquivo2,trocar,novaCor,file,numeroLinha) :
    file.seek(0)                                                   #comando que retorna para a primeira linha do arquivo (foi percorrido em: {função: abrirArquivo | no: for})
    contador = 0
    with open(arquivo2, 'w+') as file2:                           #cria um arquivo para escrita e leitura, armazenando seu object file em "file2"
        while contador < numeroLinha:                              # |o while percorre o arquivo1(file) de linha em linha com o comando
            linha = file.readline()                                # |readline, que lê uma linha e armazena na variável "linha"
            if trocar in linha:                                  #verifica se a variável que deve ser alterada(trocar) se encontra na atual linha do arquivo
                comprimento = len(trocar)                           # armazena o comprimento de trocar (por contagem de caracteres)
                posicao1 = linha.find(trocar) + comprimento - 1                    #encontra o último caractere da variável que deve ser alterada(trocar), guardando em posicao1

                if linha[posicao1+2] == ">":                                       #como padrão, duas posicões depois da última letra das varáveis que podem ser alteradas(as que armazenam cor), à um ">", o if faz com que a linha só seja alterada se realmente for a linha com a variável armazenando uma cor
                    posicao2 = linha.find(">")                                     #guarda a posição de um caractere padrão que tem antes da cor que será alterada, para que possa ser usado como referência ao alterar a linha
                    posicao3 = linha.find("/")                                     #guarda a posição de um caractere padrão que tem depois da cor que será alterada, para que possa ser usado como referência ao alterar a linha
                    linha = linha[0:posicao2+1] + "#" + novaCor + linha[posicao3-1:]      #faz a alteração da cor do arquivo pela nova cor, recopiando a linha com a nova cor prevista
            file2.write(linha)                                                      #escreve a atual linha do looping no arquivo2(file2)
            contador = contador + 1       
    file2.close()

##abrirArquivo##
#função que abre o primeiro arquivo em modo leitura e depois conta o número de linhas do arquivo, para então chamar a função escreverNovoArquivo
def abrirArquivo(arquivo1,arquivo2,trocar,novaCor) :
    with open(arquivo1, 'r') as file:                              #abre o arquivo nomeado em arquivo1 no modo leitura, armazenando o object file em "file"
        numeroLinha = 0                                  
        for linha in file:                                         # |percorre o arquivo de linha em linha contando todas com o numeroLinha, que
            numeroLinha = numeroLinha +  1                         # |será usado como limite em: {função: escreverNovoArquivo | no: while}
        escreverNovoArquivo(arquivo2,trocar,novaCor,file,numeroLinha)
    file.close()


###PRINCIPAL###
#usa sys.argv[] para capturar os argumentos passados na chamada do script
arquivo1 = sys.argv[1]                          #armazena o nome do arquivo que será copiado
arquivo2 = sys.argv[2]                          #armazena o nome do arquivo que será criado recebendo as informações de arquivo1
trocar = sys.argv[3]                            #armazena o nome da variável do arquivo1 que deve alterar de cor
novaCor = sys.argv[4]                           #armazena a nova cor da variável do arquivo1 que será trocada, correspondente a variável trocar
abrirArquivo(arquivo1,arquivo2,trocar,novaCor)

