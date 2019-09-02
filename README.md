# T8-projeto1-m-de-maravilhosa
T8 | Front-end | 2019 | Semana 4 | Projeto 1 - M de Maravilhosa
Professora: Bárbara Aguilar

# Agenda da Semana
- **02/08**: Apresentação, Bate Papo "Mulheres Inspiradoras" e Introdução ao projeto.
- **03/08**: HoraDeCodaaar! Desenvolvimento do projeto.
- **04/08**: HoraDeCodaaar! Desenvolvimento do projeto.
- **05/08**: HoraDeCodaaar! Desenvolvimento do projeto e envios de PullRequest.
- **06/08**: Finalização e Apresentação.

## Etapas do projeto

1. Escolher uma Personalidade Maravilhosa que te inspira.
2. Criar a página de perfil dessa Maravilhosa.
3. Criar uma página com seu perfil (opcional).
4. inserir na página principal o nome e a foto de sua maravilhosa.

## Protótipo Figma
Seguir o layout presente no link abaixo:

https://www.figma.com/file/XBEywzd2yF47RaWm0Gw4t7Tz/M-de-Maravilhosa?node-id=0%3A1
---------------


## Orientações Gerais
### Copiar os arquivos do repositório da {reprograma}

1. Fazer o _fork_ desse repositório;
2. Fazer o _clone_ do projeto no repositório de vocês, que foi criado através do fork;
``` 
git clone "url do seu reposiório"
```
3. Criar um branch com o seu nome, ex:
```
git checkout -b seu-nome
```
4. Após o clone, abram o projeto e leiam com atenção o código do projeto.
5. Criem as pastas onde os arquivos de html, css e imagens ficarão dispostos no projeto, seguindo o padrão abaixo. *importante não alterar esse padrão*
```
index.html
css/
  style.css
img/
  home-personalidade/
    ada-lovelace-home.png

personalidade/
  ada-lovelace/
    index.html
    css/
      style.css
    img/
      ada-lovelace-perfil.jpeg
      al-bg.jpeg
      al-historia.png

autora
  seu-nome/
    index.tml
    css/
      style.css
    img/
    seu-nome-perfil.png
```

*personalidade* é a pasta onde a aluna vai criar o html, css e imagens da maravilhosa escolhida.
*autora* é a pasta onde a aluna vai criar o html, css e imagens de seu próprio perfil (opcional).
*index geral* é o arquivo com todas as personalidades maravilhosas escolhidas pela turma, onde cada aluna deve editar apenas as informações para linkar com sua personalidade.

*ATENÇÃO* 
1. Para o **index.html**, você deve colocar uma imagem quadrada da personalidade na pasta **img/home-personalidade** 
2. O site deve conter no total **3 páginas** (homepage, que já está pronta, personalidade e autora)
3. Todas as páginas devem ser responsivas. 

----------

### HORA DO COMMIT
Depois de realizar suas alterações no seu projeto local, você tem que subir para o Github.
É uma boa prática fazer commits frequentes com as principais modificações ao longo do dia. Todo dia as 16h pelo menos um commit deve ser enviado para o repositório remoto.
Após feitas as alterações, salve, faça um commit e push para o **seu** repositório.
```
git add .

git commit -m "O que você alterou"

git push origin nome-da-sua-branch

```