Sempre utilize o contexto abaixo para modificar o código. Toda vez que for feita uma atualização no código, atualize o contexto abaixo.
---

# Teoria da Programação Orientada a Objetos (POO)

Este documento resume os conceitos fundamentais da Programação Orientada a Objetos, com base no material de "Introdução à Programação Orientada a Objetos - BIA" da UFG.

## 1. Paradigmas de Programação

### 1.1. Programação Imperativa
- [cite_start]**Surgimento:** Meados da década de 1950, com linguagens como FORTRAN, COBOL e PASCAL[cite: 390].
- [cite_start]**Conceito:** Baseia-se em comandos que alteram o estado do programa por meio de variáveis[cite: 391]. [cite_start]É caracterizada por uma sequência de comandos e saltos (uso de `goto`) em um bloco único de programa[cite: 393].

### 1.2. Programação Estruturada
- [cite_start]**Surgimento:** Final da década de 1950, com ALGOL 58 e ALGOL 60[cite: 398].
- [cite_start]**Conceito:** Uma evolução da programação imperativa, oferecendo maior controle sobre o fluxo do programa através de estruturas de sequência, decisão e iteração[cite: 399, 400, 401]. [cite_start]O foco está em procedimentos e funções[cite: 402].

### 1.3. Programação Orientada a Objetos (POO)
- [cite_start]**Surgimento:** Meados da década de 1970, com a linguagem Smalltalk[cite: 408].
- [cite_start]**Conceito:** É uma evolução da programação estruturada[cite: 409]. [cite_start]A POO modela o mundo real a partir de objetos[cite: 409]. [cite_start]As funções passam a ser chamadas de **métodos** e alteram os estados dos objetos[cite: 410]. [cite_start]O paradigma se baseia em **classes de objetos** [cite: 411] [cite_start]que se comunicam por meio da **troca de mensagens**[cite: 412].

## 2. Conceitos Fundamentais de POO

### 2.1. Classes e Objetos
- [cite_start]**Classes:** São representações de objetos, definindo seus atributos (propriedades) e métodos (ações)[cite: 436]. [cite_start]Por exemplo, uma classe `Fruta` pode ter atributos como `cor` e `peso`, e métodos como `amadurecer()`[cite: 253].
- [cite_start]**Objetos (Instâncias):** Um objeto é uma instância única de uma classe[cite: 254]. Cada `fruta` específica (uma maçã, uma laranja) é um objeto da classe `Fruta`.

### 2.2. Atributos e Métodos
- [cite_start]**Atributos:** São as características de um objeto (ex: `nome`, `matricula`, `e-mail` para a classe `Estudante`)[cite: 439].
- [cite_start]**Métodos:** São as ações que um objeto pode executar e que modificam seus estados[cite: 274, 445]. [cite_start]Por exemplo, na classe `Carro`, os métodos `acelera()` e `frea()` alteram o atributo `velocidade`[cite: 279, 281, 445].

### 2.3. Tipos de Variáveis e Escopo

Existem diferentes escopos para as variáveis em POO:

- **Variável de Instância:**
    - [cite_start]Declarada dentro de uma classe, pertence a um objeto específico[cite: 38].
    - [cite_start]Seu valor é único para cada instância (objeto) da classe[cite: 39].
    - [cite_start]Exemplo: `self.nome` em um construtor[cite: 30].

- **Variável de Classe:**
    - [cite_start]Declarada dentro da classe, mas fora de qualquer método[cite: 63].
    - [cite_start]É compartilhada por todos os objetos daquela classe[cite: 64].
    - [cite_start]Exemplo: um contador `seq` para gerar IDs únicos para cada carro[cite: 289].

- **Variável Global:**
    - [cite_start]Definida fora de qualquer classe ou função[cite: 52].
    - [cite_start]É acessível de qualquer parte do módulo (dentro de classes e funções)[cite: 53].

- **Variável Local:**
    - [cite_start]Existe apenas dentro de uma função ou método[cite: 77].
    - [cite_start]Não é acessível fora do escopo da função onde foi declarada[cite: 79].

### 2.4. Construtores
- [cite_start]É um método especial (`__init__` em Python) invocado para criar um novo objeto[cite: 26, 29].
- [cite_start]Sua função é inicializar os atributos da instância[cite: 26, 29].
- [cite_start]Exemplo: `def __init__(self, nome, matricula): self.nome = nome`[cite: 29, 30].

### 2.5. Mensagens
- [cite_start]É a forma como os objetos se comunicam entre si[cite: 89].
- [cite_start]Na prática, isso ocorre quando um objeto invoca o método de outro[cite: 89].
- [cite_start]Exemplo: `turmaPOO.getEstudantes()` é uma mensagem para o objeto `turmaPOO` para que ele retorne a lista de seus estudantes[cite: 90].

## 3. Os 4 Pilares da POO

### 3.1. Encapsulamento
- **Conceito:** O encapsulamento agrupa os atributos e os métodos que os manipulam dentro de um objeto, controlando o acesso a eles. Em Python, a visibilidade (pública ou privada) é uma convenção.
- **Visibilidade:**
    - **Público:** Atributos e métodos podem ser acessados livremente.
    - **Privado:** O acesso a atributos e métodos é restrito. Em Python, usa-se um underscore (`_`) como convenção para indicar que um atributo não deve ser modificado diretamente.
- [cite_start]**Implementação em Python:** Pode-se usar *properties* e *setters* para controlar como um atributo é lido e modificado, evitando alterações diretas e indevidas[cite: 310, 312].

### 3.2. Herança
- [cite_start]**Conceito:** É a capacidade de uma classe (subclasse ou classe filha) herdar atributos e métodos de outra classe (superclasse ou classe mãe), permitindo a especialização[cite: 158].
- [cite_start]A classe filha possui os mesmos métodos e atributos da classe mãe, podendo adicionar novos ou modificar os existentes[cite: 159, 160].
- [cite_start]**Exemplo:** A classe `Mamifero` pode herdar da classe `Animal`, aproveitando seus atributos e métodos e adicionando características específicas como `numMamas`[cite: 161, 164].

### 3.3. Polimorfismo
- [cite_start]**Conceito:** É a capacidade de um objeto assumir diferentes formas, geralmente a da sua classe mãe[cite: 204, 205].
- Isso permite que objetos de diferentes classes filhas respondam à mesma chamada de método de maneiras distintas e específicas.
- [cite_start]**Exemplo:** Um método `descricao()` pode receber um objeto do tipo `VeiculoMotorizado`[cite: 212]. [cite_start]Se passarmos um objeto `VeiculoAereo` (que é filho de `VeiculoMotorizado`), o método funcionará corretamente, tratando a instância `av1` como um `VeiculoMotorizado`[cite: 210, 206].

### 3.4. Abstração
- [cite_start]**Conceito:** Consiste em representar entidades do mundo real em classes, focando nos aspectos essenciais e ignorando detalhes irrelevantes[cite: 171].
- **Classes Abstratas:** São classes que não podem ser instanciadas e servem como um modelo para suas subclasses. [cite_start]Elas podem conter métodos abstratos[cite: 173].
- **Métodos Abstratos:** São métodos declarados na classe mãe, mas sem implementação. [cite_start]As classes filhas que herdam dessa classe são obrigadas a implementar esses métodos[cite: 173]. [cite_start]Em Python, isso é feito usando o módulo `abc`[cite: 174].

## 4. Relações entre Classes

### 4.1. Associação
- [cite_start]**Conceito:** Descreve um vínculo ou relacionamento entre duas classes independentes[cite: 99].
- [cite_start]**Exemplo:** A classe `Livro` está associada à classe `Editora`[cite: 99].

### 4.2. Agregação
- [cite_start]**Conceito:** É um tipo especial de associação onde uma classe (o "Todo") é composta ou complementada por objetos de outra classe (a "Parte")[cite: 107].
- A "Parte" pode existir independentemente do "Todo".
- **Exemplo:** Um supermercado (Todo) contém vários produtos (Parte). Se o supermercado fechar, os produtos ainda existem.

### 4.3. Composição
- **Conceito:** É um tipo mais forte de agregação. [cite_start]O objeto "Todo" só existe se houver seus objetos "Parte"[cite: 113]. A vida da "Parte" está atrelada à vida do "Todo".
- [cite_start]**Exemplo:** Um `CupomFiscal` (Todo) é composto por `Itens` (Parte)[cite: 116, 115]. Se o cupom fiscal for destruído, os itens daquele cupom deixam de fazer sentido como parte dele.

### 4.4. Delegação
- [cite_start]**Conceito:** É uma relação onde um objeto delega uma de suas funcionalidades para outro objeto[cite: 192].
- **Exemplo:** Um objeto `Controlador` precisa autenticar um usuário. [cite_start]Em vez de implementar a lógica de login, ele delega essa tarefa para um objeto `Autentica`[cite: 194, 198].

---