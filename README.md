# Projeto_Conjunto_de_Mandelbrot_GrupoX

Membros:  
  >Caio Martins Baron Mauricio RA : 278399  
  >Guilherme D'César A. E. R. Esquiante RA : 198562  
  >Lucas Pfeiffer Petinati RA : 197755  
  >Vitor Oriel Ramos  de Jesus RA : 266366  

##  Foco do Código

O objetivo principal deste código é a gerar uma figura matemática de um conjunto de Mandelbrot a partir das posições dos pixels 
em uma imagem de tamanho 900x1200.

## Linguagem utilizada e Bibliotecas

* Linguagem Principal:  Python 3.13
*  Bibliotecas: Numpy, Pillow, Matplotlib
*  * as versões das bibliotecas utilizadas se encontram no arquivo requirements.txt

## Instalação
para testar o projeto, siga os passos abaixo:

1.  Baixe o Código: use a opção Download ZIP.
2.  Descompactar: Descompacte o arquivo ZIP em uma pasta no seu computador.
3.  Acesso da pasta via terminal: Abra o Terminal/Prompt de Comando e vá até a pasta descompactada:
   
   
    ```bash
    cd [caminho da sua pasta]
    ```
    
4.  Configurando o ambiente: Faça a instalação das bibliotecas na versões adequadas pelo requirements.txt também no Prompt de comando:
    ```bash
    pip install -r requirements.txt
    ```

    
5.  Executar o código: Execute o arquivo principal no Prompt de comando:
    ```bash
    python Mandelbrot.py
    ```
* Pode-se rodar o código também ao abrir o arquivo Mandelbrot.py na sua IDE de preferência.
  
 ## Funcionamento do código
  Nessa seção vamos explicar o que cada função personalizada construida pelo grupo está fazendo e como funciona. Além disso será explicado como o processo de gerar a imagem final.

* __Função `fc(z, c)`__:
   * __Objetivo:__ Descrever a forma algebrica da função que gera o conjunto de Mandelbrot
   * __Argumentos:__ `z` e `c` são números complexos `<class 'complex'>`, `z` representa a variável da função e `c` se mantem fixo ou seja temos uma f(z).
   * __Saída:__  um número do tipo `<class 'complex'>` resultado da operação algebrica $Z^2\ +\ c$.
      
* __Função `is_Mandelbrot(c, N)`__:  
   * __Objetivo:__ Determinar se um número complexo `c` pertence ao conjunto de Mandelbrot.
   * __Argumentos:__ `c` é um número complexo na forma algebrica de <class 'complex'>. `N` é um inteiro `<class 'int'>` que determina o número máximo de iterações.
   * __Processo:__ Itera a função `fc(z, c)` por até $N=100$ vezes. Usamos a saída de `fc(z, c)` como nova entrada `z` para a iteração seguinte e calcula-se o módulo do número gerado por `fc(z, c)` a cada iteração.
   * __Condição de parada:__ O teste para se o módulo da variável `z` gerada na iteração excede o valor $M=2$.
   * __Saída:__ Retorna o valor 0 se `c` pertence ao conjunto de Mandelbrot. Retorna o valor de `N - n` caso `c` não pertença ao conjunto, em que `n` é o número de iterações até atigir $M = 2$. O valor `N - n ` representa o quão rápido foi a convergência da sequência dos módulos para o valor $M = 2$. De modo que com isso podemos gerar um degradê na imagem final com base na diferença de rapidez de convergência dos pontos.
 
* __Função `v_is_Mandelbrot(c, N)`__:
   * __Objetivo:__ Vetorizar a função `is_Mandelbrot(c, N)` para possibilitar sua aplicação em arrays numpy.
   * __Argumentos:__  `c` é um array `<class 'numpy.ndarray'>` com dados do tipo `'complex128'` e N é um inteiro `<class 'int'>`.
   * __Saída:__  uma matriz 1200x900 (linhas x colunas) do tipo `<class 'numpy.ndarray'>` com dados do tipo `int64` indo de 0 a 100.
 
* __Função `pix_to_z(lp, cp)`__:  
   * __Objetivo:__ Determinar um número complexo na forma algébrica a partir das coordenadas de um pixel da imagem e já testar se esse complexo pertence ao conjunto de Mandelbrot.
   * __Argumentos:__ `lp` e `cp` são matrizes 1200x 900 (Linhas x colunas) do tipo `<class 'numpy.ndarray'>` com dados do tipo `<class 'int'>`.
   * __Processo:__ `lp` e `cp` são usados para a determinação das partes imaginária e real do complexo `c` a partir das expresões $a\ =\ -2 +\ (cp * 3) / 900$ e $b\ =\ -2 + (lp * 4) / (1200)$. O grupo estabeleceu os intervalos de [-2, 1] no eixo real e de [-2, 2] no eixo imaginário, pois neles podemos representar todos os membros do conjunto de Mandelbrot que são reais puros e ainda temos um bom numero de membros em outras regiões deixando a figura bem completa. Como `lp` e `cp` são matrizes numpy as operações são vetorizadas e aplicadas a todos os elementos das matrizes logo tem-se que as variaveis `a` e `b` armazenam matrizes também da forma 1200x900 com todos os valores possiveis das partes real e imaginária. assim ao combinarmos isso na expressão $c =\ a + b*1j$ temos que a variável `c` passa a armazenar uma matriz 1200 x 900 em que cada elemento é um número complexo determinado a partir da posição correspondente do pixel. Por exemplo, o complexo relativo ao pixel na posição (5,17) está representado no elemento $C_{5,17}$ da matriz `c`. Por fim aplicamos a função `v_is_Mandelbrot(c, N)` sobre `c` ( dai a necessidade de vetorizar a função `is_Mandelbrot(c, N)` anteriormente) e obtemos uma matriz 1200 x 900 de valores `int64` indo de 0 a 100 em que valores iguais 0 correspondem membros do conjunto de mandelbrot e os demais valores já indicam o não pertencimento e a propria rápidez de convergência. 
   * __Saída:__ Retorna uma matriz  chamada `conv` com 1200x900 (linhas x colunas) do tipo `<class 'numpy.ndarray'>` com dados do tipo `int64` indo de 0 a 100. Aqui tem-se a matriz base de onde vamos gerar a imagem, pois cada elemento na posição i,j corresponde a um pixel na posição i,j da imagem e sua cor vai depender do valor entre 0 e 100 na matriz `conv`. Assim podemos gerar inicialmente uma imagem com um degradê de tons de cinza (sem RGB) e posteriormente colorir por meio de um colormap em tons RGB gerando um degradê mais interessante.
 
* __Gerando a Imagem__:
   * A imagem final é gerada fazendo-se uso da biblioteca `Pillow` uma vez que essa biblioteca oferece funções simples para a construção de uma imagem a partir de uma matriz numpy.
   * Primeiramente geramos a `matriz_base` usando a função `np.fromfunction`. Nessa função passamos como argumentos uma função qualquer e o formato da matriz que desejamos gerar. o que ocoore aqui é que a `np.fromfunction` gera duas matrizes ( uma para linhas e outra para colunas) que descrevem os indices dos elementos da matriz que queremos criar e a essas matrizes é aplicada apenas uma vez a função que passamos no argumento. Em nosso código temos `np.fromfunction(pix_to_z, (1200, 900))`, o que ocorre aqui é que a função `pix_to_z` vai operar as matrizes dos indices criadas pela `np.fromfuntion` ( os índices nesse caso já são a propria posição dos pixels) de forma vetorizada e a saída da matriz `conv` na posição i,j da `pix_to_z` será colocada na posição do elemento i,j da matriz que estamos gerando. Como nossa função `pix_to_z` já espera receber matrizes como agumentos e gerar uma saída no formato de matriz o que estamos fazendo aqui na pratica é utilizando a `np.fromfunction` para gerar as entradas `lp` e `cp` no formato que desejamos (1200 x 900) e aplicando isso a `pix_to_z` para gerar a `matriz_base` evitando loops `for` e `while` que deveriam se repetir por muitas vezes.
   * De posse da `matriz_base` aplicamos uma normalização para manter todos os valores númericos entre 0 e 1, isso é necessario , pois o padrão usado para colorir só aceita números inteiros entre 0 e 255. A princípio como temos na nossa `matriz_base` apenas números inteiros entre 0 e 100 isso seria desnecessário, mas para evitar possíveis erros e para facilitar a aplicação do de um degradê em RGB posterior essa normalização é necessaria. assim produzimos a `matriz_normalizada` de mesmo formato da `matriz_base` mas somente com valores entre 0 e 1.
   * Multiplicando essa `matriz_normalizada` por 255 obtemos uma nova matriz ( chamada de `seca`) que agora pode ser transformada em imagem pela Pillow. É importante ressaltar que essa matriz `seca` não é capaz de gerar uma imagem colorida então o que vemos é um degradê do preto para tons de cinza até o branco. Usamos a função `Image.fromarray()` da Pillow para gerar a imagem, essa função recebe um array numpy (matriz) e gera a imagem em que cada elemento da matriz é um pixel que recebe uma cor, depois mostramos essa imagem ao usuario por meio do método `.show()`.
   *  Para colorir nosso degradê cinza com outras tonalinadades precisariamos sobrepor 3 matrizes onde cada uma representaria uma cor fundamental RGB (Red, Green, Blue) em que essa sobreposição é a responsável por oferecer uma variedade de cores nos pixels. Como já temos uma `matriz_normalizada` que contém um degradê de tons de cinza podemos usar uma função da matplotlib chamada `get_cmap()` que recebe uma matriz qualquer e a colore em RGB a partir dos valores dos elementos, onde cada valor será associado a uma cor de acordo com o mapa selecionado. Vale ressaltar que caso a `matriz_normalizada` não apresetasse valores distintos entre 0 e 1 (ou seja o seu degradê de cinzas) o `get_cmap()` simplesmente ia trocar o preto e o branco para alguma outra cor sólida e degradê nenhum seria visto, alêm disso para aplicação da função de mapeamento é necessário que os valores da matriz alvo estejam entre 0 e 1. Logo aplicamos a função de mapeamento sobre a `matriz_normalizada` e geramos a `figura_Mapeada` que ao multiplicarmos por 255 nos da a `imagem_degrade` que agora pode ser construida e exibida pelas mesmas funções da Pillow que descrevemos anteriormente.
   *  As imagens com degradê colorido podem ser vistas na pasta imagens. Os mapas usados tem o nome `'hot'`  e `'turbo'`. A imagem `fractal_cinza` é a que contém o degradê em tons de cinza (recomendamos dar um zoom para visualizar o degradê com mais clareza, ele está envolvendo a região em preto) e a `fractal_puro` não contem degradê algum.
     
