# Trabalho-1-De-LingProg

[toc]

---

## Descrição do Projeto
[Fluxograma do Codigo](https://miro.com/app/board/uXjVMkb6eoc=/?share_link_id=681028836505)

## Instruções de Compilação
Utilizamos  o mysql como nosso banco de dados, portanto para que o programa funcione de acordo, devemos iniciar e ter o mysql baixado. Para instalação utilizamos o seguinte [tutorial](https://www.youtube.com/watch?v=zpssr3u1EO8), recomendamos que o siga caso não consiga pelo [site oficial](https://dev.mysql.com/downloads/). Abaixo seguem os comandos utilizados par a criação do nosso banco (foram rodados no workbench, mas pode-se rodar cada um individualmente no seu prompt de comando)

1- Caso não esteja pelo workbench ja logado no seu root, faça o seguinte passos:

```sql
mysql -u root -p
```

Isso chamará a sua senha e basta que você a insira, garantindo assim estar logado no seu root, a partir dai, so seguir os passos adiante.

2 - Insira cada linha individualmente caso esteja no prompt de comando, para evitar erros. Caso esteja no workbench basta copiar, colar e rodar o código pela própria ferramenta. Primeiro criamos o banco de dados pelos comandos abaixo.

```sql
create database if not exists MinervaBots;

use MinervaBots;

create table if not exists usuario (
    nome varchar(255),
    email varchar(255),
    senha varchar(255),
    cargo varchar(255),
    constraint PK_usuario primary key (email)
);

create table if not exists area (
    nome_area varchar(255),
    FK_area_usuario_email varchar(255),
    constraint PK_area primary key (nome_area, FK_area_usuario_email),
    constraint FK_area_usuario foreign key (FK_area_usuario_email) references usuario (email)
);

create table if not exists projeto (
    nome_projeto varchar(255),
    FK_projeto_usuario_email varchar(255),
    constraint PK_projeto primary key (nome_projeto, FK_projeto_usuario_email),
    constraint FK_projeto_usuario foreign key (FK_projeto_usuario_email) references usuario (email)
);

create table horarios_online (
    segunda varchar(80),
    terca varchar(80),
    quarta varchar(80),
    quinta varchar(80),
    sexta varchar(80),
    sabado varchar(80),
    FK_horarios_online_email varchar(255),
    constraint PK_horarios_online primary key (segunda, terca, quarta, quinta, sexta, sabado, FK_horarios_online_email),
    constraint FK_horarios_online foreign key (FK_horarios_online_email) references usuario (email)
);

create table horarios_presencial (
    segunda varchar(80),
    terca varchar(80),
    quarta varchar(80),
    quinta varchar(80),
    sexta varchar(80),
    sabado varchar(80),
    FK_horarios_presencial_email varchar(255),
    constraint PK_horarios_presencial primary key (segunda, terca, quinta, sexta, sabado, FK_horarios_presencial_email),
    constraint FK_horarios_presencial foreign key (FK_horarios_presencial_email) references usuario (email)
);

```

3 - Agora basta você criar o usuario usado no nosso código seguindo os comandos a baixo.

```sql
CREATE USER 'admBots'@'localhost' IDENTIFIED BY 'senha'; 
GRANT ALL PRIVILEGES ON * . * TO 'admBots'@'localhost'; 
FLUSH PRIVILEGES;
``` 

4 - As bibliotecas utilizadas e como baixá-las pelo seu prompt estão abaixo:
```
pip install mysql
pip install webbrowser
pip install threading
pip install flask
```

## Padrão de Commit
Utilizamos tipos de commit para padronizar as mensagens de commit neste projeto. A seguir, estão os tipos de commit a serem utilizados, juntamente com exemplos de sumários correspondentes:

### ADD
Use o tipo "ADD" quando estiver adicionando um novo recurso ou funcionalidade ao código.

Exemplo:
```
"Adiciona funcionalidade de autenticação de usuário"
```

### DROP
O tipo "DROP" é usado para indicar a remoção de um recurso ou funcionalidade do código.

Exemplo:
```
"Remove o módulo de gráficos legados"
```

### FIX
Utilize "FIX" ao realizar correções de bugs e resolver problemas.

Exemplo:
```
"Corrige o erro de formatação na página de perfil do usuário"
```

### BUILD
O tipo "BUILD" é usado quando você atualiza dependências ou realiza alterações nas características de compilação do projeto.

Exemplos:
```
"Atualiza as dependências do servidor de produção"
"Altera as configurações de compilação para suportar a nova biblioteca"
```

### REFACTOR
Use "REFACTOR" quando estiver realizando refatorações no código, melhorando sua estrutura ou desempenho sem alterar sua funcionalidade.

Exemplo:
```
"Refatora a classe de manipulação de dados para melhorar a legibilidade"
```

### DOCS
O tipo "DOCS" é aplicado a alterações relacionadas à documentação, como adição ou atualização de comentários no código ou no README.

Exemplo:
```
"Adiciona documentação de código para o método de autenticação"
```

### STYLE
Utilize o tipo "STYLE" para alterações que afetam apenas o estilo visual do código, como formatação ou estilos de código.

Exemplo:
```
"Melhora a formatação do código de acordo com as diretrizes de estilo"
```

## Modelo de Branchs Neste Projeto
Neste projeto, estamos adotando o GitFlow como nosso modelo de fluxo de trabalho para gerenciar o desenvolvimento e a entrega de software de forma eficiente e organizada.

### Ramificações Principais
- **Master**: A ramificação "master" é a principal linha de desenvolvimento. Ela contém apenas versões estáveis e testadas do software.

- **Develop**: A ramificação "develop" é onde o desenvolvimento ativo ocorre. Todas as novas funcionalidades e correções de bugs são implementadas aqui.

### Ramificações de Recursos
- **Feature**: Ramificações "feature" são criadas a partir de "develop" e são usadas para desenvolver novas funcionalidades ou melhorias. Quando a funcionalidade estiver pronta, ela é mesclada de volta para "develop".