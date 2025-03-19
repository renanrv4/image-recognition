# Reconhecimento de Texto em Imagens

Este repositório contém um projeto de reconhecimento de texto em imagens utilizando [Azure Cognitive Service].

## Estrutura do repositório

- **input**: Contém as imagens que foram analisadas.
- **output**: Contém os resultados do reconhecimento de texto nas imagens.

## Como Funciona

1. As imagens são enviadas para a ferramenta de OCR.
2. O texto é extraído e os resultados são salvos na pasta **output**.
3. Foram realizadas análises para verificar a precisão do reconhecimento.

## Aprendizados

Durante o desenvolvimento desse projeto, aprendi sobre as técnicas de OCR e a importância do pré-processamento das imagens para melhorar a acurácia do reconhecimento.

## Resultados

```
Texto reconhecido na imagem input/img0.jpg:
"0 fracasso é
apenas oma
oportunidade
para recomeçar
com mais
inteligência."
— HENRY FORD.

--------------

Texto reconhecido na imagem input/img1.jpg:
"Uma pessoa que nunca
cometeu um erro, nunca
tentou nada de novo"
- Albert Einstein.

--------------

Texto reconhecido na imagem input/img2.jpg:
Pensar é mais
interessante do que
saber, mas menos
interessante do que
olhar.
Johann Wolfgang von Goethe
Alemanha 1' Escritor, Cientista, Mestre de Poesia, Drama e Novela
17491' 1' 1832
www.citador.pt

--------------

Texto reconhecido na imagem input/img3.jpg:
"Somos ondas do
mesmo mar,
folhas da mesma
árvore, flores do
mesmo jardim.
escritosdefilosofos.blogspot.com

--------------

Fim das análises!
```
