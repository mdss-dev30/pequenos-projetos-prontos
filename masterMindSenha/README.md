# Este script foi criado para colocar na prática a lógica de programação na linguagem python resolvendo o seguinte desafio:

## 1. Ideia Geral

O jogo da senha, ou do inglês Mastermind, é um jogo de adivinhação e, de
certa forma, estratégia. Um dos jogadores escolhe uma sequência de 4 cores entre
as 6 opções do jogo (amarelo, verde, azul, roxo, vermelho e laranja) e o seu oponente
deve tentar adivinhar qual a sequência determinada.
Para que o jogador que deve adivinhar a senha não apenas jogue cegamente
sequências aleatórias de cores, o que determinou a senha também deve dar dicas
sobre os “chutes” do adversário. Isto é, ele usa pinos brancos e pretos para sinalizar
quão perto a sequência adivinhada está da sequência real, nestes 3 casos:

### ➔ Caso a cor corresponda à cor na exata posição chutada, utiliza-se o pino

branco;

### ➔ Caso a cor corresponda à alguma cor da sequência, mas está na posição

incorreta, utiliza-se o pino preto;

### ➔ Caso a cor não corresponda a nenhuma cor da sequência, deixa-se vazio.

## 2. Codificação

No caso do projeto, vocês terão que codificar o jogo da senha na forma de
um programa Python, de modo a trabalhar os conceitos ensinados durante o curso
do Coding Tank. Neste caso, siga as instruções dadas a seguir.
No início, deve ser criada a senha a ser adivinhada pelo jogador. Nós
daremos duas opções para vocês: fornecer a senha por meio de input, como se um jogador estivesse criando ela para o outro adivinhar, ou tentar gerar aleatoriamente utilizando a biblioteca random do Python. No caso de você querer usar a biblioteca
random, você pode consultar a seguinte documentação: Documentação Random.
Caso encontre qualquer dificuldade em utilizar bibliotecas, que não é um tema
abordado no curso, e tenha interesse em utilizá-la, converse com um dos
professores! Em ambos os casos, é necessário que o programa avalie se a senha é
válida, isto é, se não existe nenhuma repetição de cores. Caso não seja válido, deve
haver o tratamento correto em cada situação. Recomendamos manter a senha em
uma lista. Exemplo:

### senha = [laranja,vermelho,azul,verde]

### senha = [laranja,laranja,azul,verde]

A segunda etapa é um loop em que o jogador deve fornecer os seus chutes
para o código. A quantidade de vezes que será permitido o jogador chutar pode ser
um valor definido, como 10 ou 20, ou pode ser um valor determinado pelo próprio
jogador também, através de um input. Fica a critério de vocês. A única
obrigatoriedade aqui é que haja tanto chutes de senha limitados, quanto uma
limitação no número de pinos de cada cor.
Ou seja, se o limite de jogadas é 10, o jogador só pode chutar 10 sequências
até o final do jogo. Se o limite de pinos de cada cor (no jogo físico há apenas 10
pinos de cada cor) é 10, o jogador só pode usar durante todo o jogo 10 vezes cada
pino. Não se deve contabilizar os pinos usados para definir a senha. Então, o seu
programa não deve apenas contabilizar quantas vezes o jogador faz os chutes, mas
também contabilizar quantas vezes ele usa o pino laranja, o pino amarelo, o pino
verde e assim por diante. Deve ser apresentada uma mensagem de erro caso o
jogador tente usar mais pinos do que ele tem acesso e também, a cada jogada, é
importante ter uma mensagem falando quantas sequências o jogador ainda pode
fazer e quantos pinos de cada cor ele ainda tem disponível. Lembre-se de fornecer
também os pinos brancos, pretos e vazios. Exemplo:

### Caso falte 4 chutes antes de acabar o jogo sem o

jogador acertar a senha, tenha 4 pinos vermelhos, 2 pinos
amarelos, 8 pinos roxos, 6 pinos verdes, 9 pinos laranjas
e 7 pinos azuis.

### senha = [‘laranja’, ‘verde’, ‘amarelo’, ‘vermelho’]

### chute = [‘roxo’, ‘amarelo’, ‘amarelo’, ‘vermelho’]

### [‘vazio’, ‘preto’, ‘branco’, ‘branco’]

Você tem 4 chutes disponíveis
Você tem 4 pinos vermelhos disponíveis
Você tem 2 pinos amarelos disponíveis
Você tem 8 pinos roxos disponíveis
Você tem 6 pinos verdes disponíveis
Você tem 9 pinos laranjas disponíveis
Você tem 7 pinos azuis disponíveis

### Obs.: O chute pode ter valores repetidos, apenas a senha não pode ter valores repetidos.

Quanto à forma como o jogador deve fornecer cada chute, vamos pedir para
que vocês peguem todas as cores em um único input separadas por vírgula. Sobre
estar em maiúsculo ou minúsculo, não deve importar. Faça um tratamento para que
funcione para o caso do jogador fornecer com letras maiúsculas ou minúsculas.
Exemplo:

### Forneça o seu chute: laranja,VERMELHO,AzUl,vErDE

Por fim, é necessário verificar se o jogo chegou ao fim ou não. Existem dois casos
em que o jogo chega ao seu fim: caso o jogador acerte a exata senha (então o jogo
deve dar uma mensagem de parabenização e finalizar automaticamente o jogo) ou
caso o jogador esgote as suas tentativas sem acertar a senha (então o jogo deve dar
uma mensagem de fim de jogo e finalizar o jogo).

## 3. Exemplo de Jogo

Forneça a senha a ser utilizada: laranja,vermelho,verde,verde
Erro: Não é possível ter repetições na senha
Forneça a senha a ser utilizada: laranja,vermelho,verde,azul
Forneça seu chute: laranja,azul,roxo,amarelo

[‘branco’, ‘preto’, ‘vazio’, ‘vazio’]
Você tem 9 chutes disponíveis
Você tem 10 pinos vermelhos disponíveis
Você tem 9 pinos amarelos disponíveis
Você tem 9 pinos roxos disponíveis
Você tem 10 pinos verdes disponíveis
Você tem 9 pinos laranjas disponíveis
Você tem 9 pinos azuis disponíveis

Forneça seu chute: laranja,verde,azul,vermelho
[‘branco’,‘preto’, ‘preto’, ‘preto’]
Você tem 8 chutes disponíveis
Você tem 9 pinos vermelhos disponíveis
Você tem 9 pinos amarelos disponíveis
Você tem 9 pinos roxos disponíveis
Você tem 9 pinos verdes disponíveis
Você tem 8 pinos laranjas disponíveis
Você tem 8 pinos azuis disponíveis

Forneça seu chute: laranja,vermelho,verde,azul

[‘branco’,‘branco’, ‘branco’, ‘branco’]

Você tem 7 chutes disponíveis
Você tem 7 pinos vermelhos disponíveis
Você tem 9 pinos amarelos disponíveis
Você tem 9 pinos roxos disponíveis
Você tem 8 pinos verdes disponíveis
Você tem 7 pinos laranjas disponíveis
Você tem 7 pinos azuis disponíveis

Parabéns, você ganhou o jogo!

## 4. Conclusão

Assim, esperamos que seja possível trabalhar os diferentes conceitos, desde condicionais, loops, strings, listas e possivelmente funções (depende
de você).
Bom trabalho!
