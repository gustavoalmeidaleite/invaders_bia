Os arquivos dentro da pasta Legíveis/py_contexto.py contém os arquivos de aula da disciplina de Programação Orientada a Objetos, ministrada pelo professor Dr. Edson Nascimento. Use-os como referência para responder às perguntas.

SUMÁRIO

1 INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS
1.1 PARADIGMAS DE PROGRAMAÇÃO
1.1.1 Programação Imperativa
1.1.2 Programação Estruturada
1.1.3 Programação Orientada a Objetos (POO)
1.2 CONCEITOS FUNDAMENTAIS DE POO
1.2.1 Modelo de Objetos
1.2.2 Tipos Abstratos de Dados
1.2.3 Classes
1.2.4 Atributos e Propriedades
1.2.5 Métodos
1.2.6 Instâncias

2 PILARES DA PROGRAMAÇÃO ORIENTADA A OBJETOS
2.1 ENCAPSULAMENTO E VISIBILIDADE
2.1.1 Acesso Público e Privado
2.2 HERANÇA
2.2.1 Superclasses e Subclasses
2.3 POLIMORFISMO
2.3.1 Sobrescrita de Métodos
2.4 ABSTRAÇÃO
2.4.1 Classes Abstratas
2.4.2 Métodos Abstratos
2.5 INTERFACES

3 ELEMENTOS AVANÇADOS DE POO
3.1 CONSTRUTORES
3.2 ESCOPO DE VARIÁVEIS
3.2.1 Variáveis de Instância
3.2.2 Variáveis de Classe
3.2.3 Variáveis Globais
3.2.4 Variáveis Locais
3.3 MENSAGENS E COMUNICAÇÃO ENTRE OBJETOS

4 RELACIONAMENTOS ENTRE CLASSES
4.1 ASSOCIAÇÃO
4.1.1 Navegabilidade
4.2 AGREGAÇÃO
4.3 COMPOSIÇÃO
4.4 DELEGAÇÃO

5 INTRODUÇÃO À LINGUAGEM DE MODELAGEM UNIFICADA (UML)
5.1 HISTÓRICO E PROPÓSITO DA UML
5.2 TIPOS DE DIAGRAMAS UML
5.2.1 Diagramas Estruturais/Estáticos
5.2.2 Diagramas Comportamentais/Dinâmicos
5.3 DIAGRAMA DE CLASSES
5.3.1 Representação de Classes, Atributos e Métodos
5.3.2 Representação de Relacionamentos
5.3.2.1 Associação
5.3.2.2 Herança e Especialização
5.3.2.3 Realização/Implementação
5.3.2.4 Agregação
5.3.2.5 Composição
5.3.2.6 Dependência
5.3.3 Multiplicidade
5.3.4 Classe Associativa
5.3.5 Associação Ternária






Agora, escreva os conceitos, baseado nos slides para os itens do capítulo 1



1 INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS

1.1 PARADIGMAS DE PROGRAMAÇÃO

1.1.1 Programação Imperativa

1.1.2 Programação Estruturada

1.1.3 Programação Orientada a Objetos (POO)

1.2 CONCEITOS FUNDAMENTAIS DE POO

1.2.1 Modelo de Objetos

1.2.2 Tipos Abstratos de Dados

1.2.3 Classes

1.2.4 Atributos e Propriedades

1.2.5 Métodos

1.2.6 Instâncias




Mostrar raciocínio
Com certeza. Seguem os conceitos do Capítulo 1, elaborados com base no conteúdo dos slides fornecidos.

1 INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS
1.1 PARADIGMAS DE PROGRAMAÇÃO
1.1.1 Programação Imperativa
A programação imperativa, que surgiu em meados da década de 1950 com linguagens como FORTRAN, ALGOL e COBOL, baseia-se em ações e comandos que alteram o estado do programa por meio de variáveis. Caracteriza-se pela definição de tipos de dados, expressões, atribuições e uma sequência de comandos que podem incluir saltos (labels & goto), formando um programa em um bloco único.



1.1.2 Programação Estruturada
Iniciada no final dos anos 1950, a programação estruturada é uma evolução da imperativa. Seu foco está em oferecer maior controle sobre o fluxo do programa através de estruturas de sequência, decisão e iteração. O paradigma se baseia no uso de procedimentos e funções, além de módulos que são enviados ao compilador juntamente com o programa principal.



1.1.3 Programação Orientada a Objetos (POO)
Surgindo em meados dos anos 1970 com o Smalltalk, a Programação Orientada a Objetos é uma evolução da programação estruturada. A principal característica deste paradigma é a modelagem do mundo a partir de objetos. As funções passam a ser chamadas de métodos, que alteram os estados dos objetos. A POO baseia-se em classes de objetos, e esses objetos se comunicam por meio da troca de mensagens.




1.2 CONCEITOS FUNDAMENTAIS DE POO
1.2.1 Modelo de Objetos
O modelo de objetos é o conceito central da POO, que propõe a modelagem do mundo a partir de seus elementos constituintes, que são os objetos.

1.2.2 Tipos Abstratos de Dados
Diferente dos tipos primitivos de dados (como int, float, char), os tipos abstratos são aqueles cujo comportamento lógico é definido por um conjunto de valores e as operações que podem ser realizadas sobre eles. Exemplos incluem 



String, coleções e classes como Pessoa ou Produto.


1.2.3 Classes
Uma classe é a representação de um conjunto de objetos que compartilham os mesmos atributos e métodos. Por exemplo, a classe 

Estudante representa todos os estudantes e define o que cada um deles terá.

1.2.4 Atributos e Propriedades
Atributos são as características ou propriedades que definem os objetos de uma classe. Para uma classe 

Estudante, os atributos poderiam ser: nome, matrícula e e-mail.

1.2.5 Métodos
Métodos são as ações ou funções que podem ser executadas por um objeto. Eles são responsáveis por modificar os estados dos objetos. Por exemplo, na classe 


Estudante, métodos poderiam ser trancarMatricula ou gerarHistorico.

1.2.6 Instâncias
Uma instância é um objeto único criado a partir de uma classe. Cada estudante específico, por exemplo, é uma instância única da classe 

Estudante.






2 PILARES DA PROGRAMAÇÃO ORIENTADA A OBJETOS

2.1 ENCAPSULAMENTO E VISIBILIDADE

2.1.1 Acesso Público e Privado

2.2 HERANÇA

2.2.1 Superclasses e Subclasses

2.3 POLIMORFISMO

2.3.1 Sobrescrita de Métodos

2.4 ABSTRAÇÃO

2.4.1 Classes Abstratas

2.4.2 Métodos Abstratos

2.5 INTERFACES




Mostrar raciocínio
Com certeza. Seguem os conceitos do Capítulo 2, elaborados com base no conteúdo dos slides fornecidos.

2 PILARES DA PROGRAMAÇÃO ORIENTADA A OBJETOS
2.1 ENCAPSULAMENTO E VISIBILIDADE
Encapsulamento é o pilar que trata da visibilidade e do controle de acesso aos métodos e atributos de uma classe. A ideia é proteger os dados internos de um objeto, restringindo a modificação direta de suas propriedades e expondo apenas as operações seguras.



2.1.1 Acesso Público e Privado
A visibilidade define como os atributos e métodos de um objeto podem ser acessados. O acesso pode ser:

Público: Permite que qualquer parte do código acesse o membro da classe.


Privado: Restringe o acesso ao membro apenas para dentro da própria classe, protegendo-o de modificações externas indesejadas.

2.2 HERANÇA
Herança é um mecanismo que permite a uma classe (subclasse) herdar atributos e métodos de outra classe (superclasse). É a ideia de especializar uma classe mais geral. A classe filha possui os mesmos métodos e atributos da classe mãe, podendo adicionar novos ou modificar os herdados.



2.2.1 Superclasses e Subclasses
Superclasse (ou classe mãe): É a classe mais genérica que cede suas características. No exemplo dos slides, 

Animal é a superclasse.

Subclasse (ou classe filha): É a classe que herda da superclasse, representando uma especialização dela. Por exemplo, 

Mamifero é uma subclasse de Animal.

2.3 POLIMORFISMO
É a capacidade de um objeto assumir a forma de sua classe mãe. Isso permite que objetos de diferentes subclasses que herdam de uma mesma superclasse possam ser tratados de maneira uniforme, por exemplo, ao serem passados como parâmetro para um método que espera um objeto da superclasse.



2.3.1 Sobrescrita de Métodos
A sobrescrita de métodos, um conceito fundamental para o polimorfismo, não é explicitamente definida nos slides. No entanto, a herança permite que uma subclasse forneça uma implementação específica para um método que já é definido em sua superclasse.

2.4 ABSTRAÇÃO
A abstração se manifesta de duas formas:

Como o conceito geral de representar entidades do mundo real por meio de classes.

Como o uso de classes e métodos abstratos para definir um "contrato" que deve ser seguido por outras classes.

2.4.1 Classes Abstratas
São classes que não podem ser instanciadas diretamente e servem como um modelo para suas subclasses. Elas contêm métodos que precisam ser obrigatoriamente implementados pelas classes que as herdam.


2.4.2 Métodos Abstratos
É um método declarado em uma classe abstrata, mas sem implementação. A classe que herda da classe abstrata é obrigada a fornecer uma implementação para todos os seus métodos abstratos.


2.5 INTERFACES
Em Python, o conceito de interface não existe de forma explícita como em outras linguagens. No entanto, é possível simular seu comportamento através do uso de uma classe abstrata onde todos os seus métodos são abstratos. Dessa forma, qualquer classe que a estenda será obrigada a implementar todos os métodos definidos, funcionando como um "contrato" de implementação.








Com base nos arquivos de aula fornecidos, apresento um índice completo dos conceitos de Programação Orientada a Objetos e UML, estruturado conforme as normas da ABNT para trabalhos acadêmicos.

SUMÁRIO

1 INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS

1.1 PARADIGMAS DE PROGRAMAÇÃO

1.1.1 Programação Imperativa

1.1.2 Programação Estruturada

1.1.3 Programação Orientada a Objetos (POO)

1.2 CONCEITOS FUNDAMENTAIS DE POO

1.2.1 Modelo de Objetos

1.2.2 Tipos Abstratos de Dados

1.2.3 Classes

1.2.4 Atributos e Propriedades

1.2.5 Métodos

1.2.6 Instâncias

2 PILARES DA PROGRAMAÇÃO ORIENTADA A OBJETOS

2.1 ENCAPSULAMENTO E VISIBILIDADE

2.1.1 Acesso Público e Privado

2.2 HERANÇA

2.2.1 Superclasses e Subclasses

2.3 POLIMORFISMO

2.3.1 Sobrescrita de Métodos

2.4 ABSTRAÇÃO

2.4.1 Classes Abstratas

2.4.2 Métodos Abstratos

2.5 INTERFACES

3 ELEMENTOS AVANÇADOS DE POO

3.1 CONSTRUTORES

3.2 ESCOPO DE VARIÁVEIS

3.2.1 Variáveis de Instância

3.2.2 Variáveis de Classe

3.2.3 Variáveis Globais

3.2.4 Variáveis Locais

3.3 MENSAGENS E COMUNICAÇÃO ENTRE OBJETOS




Mostrar raciocínio
Com certeza. Seguem os conceitos do Capítulo 3, elaborados com base no conteúdo dos slides fornecidos.

3 ELEMENTOS AVANÇADOS DE POO
3.1 CONSTRUTORES
Um construtor é um método especial invocado para criar um objeto a partir de uma classe. Em Python, esse método é o 

__init__. Por exemplo, 

e = Estudante('Batman', '2050987654') chama o construtor para criar uma nova instância da classe Estudante.

3.2 ESCOPO DE VARIÁVEIS
Escopo refere-se à visibilidade e ao ciclo de vida de uma variável, determinando onde ela pode ser acessada no código.

3.2.1 Variáveis de Instância
São variáveis declaradas dentro de uma classe, geralmente no construtor. Elas pertencem a uma instância específica do objeto, ou seja, cada objeto tem sua própria cópia desses dados. Por exemplo, 



self.velocidade na classe Carro é uma variável de instância.

3.2.2 Variáveis de Classe
Uma variável de classe é declarada dentro da classe, mas fora de qualquer método. Ela é compartilhada entre todas as instâncias (objetos) daquela classe. Um exemplo é a variável 


seq na classe Carro, que é usada como um contador para todos os objetos criados a partir dela.

3.2.3 Variáveis Globais
É uma variável que existe dentro de um módulo, sendo definida fora de qualquer classe ou função. Ela pode ser acessada de qualquer lugar do módulo, tanto dentro quanto fora das classes e funções.


3.2.4 Variáveis Locais
Uma variável local existe apenas dentro de uma função ou método. Ela é criada a cada vez que a função é chamada e não é acessível fora desse escopo. No exemplo do método 


calculaDistancia, as variáveis x e y são locais.

3.3 MENSAGENS E COMUNICAÇÃO ENTRE OBJETOS
Mensagem é a forma pela qual um objeto se comunica com outro. Em termos práticos, isso ocorre quando um objeto invoca um método de outro objeto. Por exemplo, a chamada 


turmaPOO.getEstudantes() representa o envio de uma mensagem para o objeto turmaPOO solicitando a lista de seus estudantes.






4 RELACIONAMENTOS ENTRE CLASSES

4.1 ASSOCIAÇÃO

4.1.1 Navegabilidade

4.2 AGREGAÇÃO

4.3 COMPOSIÇÃO

4.4 DELEGAÇÃO




Mostrar raciocínio
Com certeza. Seguem os conceitos do Capítulo 4, elaborados com base no conteúdo dos slides fornecidos.

4 RELACIONAMENTOS ENTRE CLASSES
4.1 ASSOCIAÇÃO
A associação descreve um vínculo ou um relacionamento entre classes. Ela indica que os objetos de uma classe estão conectados aos objetos de outra. Um exemplo é a relação "o livro possui uma editora". Em um diagrama UML, é representada por uma linha contínua que conecta as classes.



4.1.1 Navegabilidade
A navegabilidade indica a direção de um relacionamento em uma associação. Ela pode ser:


Unidirecional: Apenas uma das classes "conhece" a outra.


Bidirecional: Ambas as classes conhecem uma à outra.

A indicação da navegabilidade em um diagrama não é obrigatória.

4.2 AGREGAÇÃO
Agregação é um tipo especializado de associação que representa uma relação "todo-parte". Nela, uma classe (o "Todo") é complementada por objetos de outra classe (a "Parte"). Uma característica chave é que a "Parte" pode existir independentemente do "Todo". O exemplo fornecido é o de 


Carrinho e Produto, onde os produtos existem mesmo sem o carrinho. No diagrama UML, é representada por um losango vazado do lado do "Todo".



4.3 COMPOSIÇÃO
Composição é uma forma mais forte de agregação. Também representa uma relação "todo-parte", mas, neste caso, a existência do objeto "Parte" depende diretamente da existência do objeto "Todo". Se o "Todo" é destruído, as "Partes" também são. Os exemplos são 




Venda e os Produtos daquela venda, ou um Pedido e seus Itens Pedido. No diagrama UML, é representada por um losango preenchido do lado do "Todo".




4.4 DELEGAÇÃO
Delegação é uma relação entre objetos onde um objeto repassa uma tarefa para outro, utilizando suas funcionalidades para completar uma operação. No exemplo, um objeto 

Controlador delega a tarefa de autenticação para um objeto Autentica.






5 INTRODUÇÃO À LINGUAGEM DE MODELAGEM UNIFICADA (UML)

5.1 HISTÓRICO E PROPÓSITO DA UML

5.2 TIPOS DE DIAGRAMAS UML

5.2.1 Diagramas Estruturais/Estáticos

5.2.2 Diagramas Comportamentais/Dinâmicos

5.3 DIAGRAMA DE CLASSES

5.3.1 Representação de Classes, Atributos e Métodos

5.3.2 Representação de Relacionamentos

5.3.2.1 Associação

5.3.2.2 Herança e Especialização

5.3.2.3 Realização/Implementação

5.3.2.4 Agregação

5.3.2.5 Composição

5.3.2.6 Dependência

5.3.3 Multiplicidade

5.3.4 Classe Associativa

5.3.5 Associação Ternária




Mostrar raciocínio
Com certeza. Seguem os conceitos do Capítulo 5, elaborados com base no conteúdo dos slides fornecidos.

5 INTRODUÇÃO À LINGUAGEM DE MODELAGEM UNIFICADA (UML)
5.1 HISTÓRICO E PROPÓSITO DA UML
A UML (Unified Modeling Language) surgiu da unificação de três métodos de modelagem orientada a objetos proeminentes nos anos 1990: OMT de James Rumbaugh, OOSE de Ivar Jacobson e o método de Grady Booch. Criada pelo Object Management Group (OMG), a UML é uma linguagem padrão com o propósito de visualizar, especificar, construir e documentar artefatos de software. A primeira especificação foi proposta em janeiro de 1997.




5.2 TIPOS DE DIAGRAMAS UML
Os diagramas UML são divididos em duas categorias principais.


5.2.1 Diagramas Estruturais/Estáticos
Estes diagramas descrevem a estrutura estática do sistema. Os tipos incluem:

Diagrama de Classe 

Diagrama de Objeto 

Diagrama de Pacote 

Diagrama de Componente 

Diagrama de Estrutura 

Diagrama de Implantação 

Diagrama de Perfil 

5.2.2 Diagramas Comportamentais/Dinâmicos
Estes diagramas mostram o comportamento dinâmico do sistema. Os tipos incluem:

Diagrama de Caso de Uso 

Diagrama de Sequência 

Diagrama de Atividade 

Diagrama de Estado 

Diagrama de Comunicação 

Diagrama de Interação 

Diagrama de Tempo 

5.3 DIAGRAMA DE CLASSES
O Diagrama de Classes é um diagrama estático que descreve os atributos, métodos e as restrições de um sistema. É o principal enfoque do curso BIA e o único diagrama que permite um mapeamento direto para o código de linguagens orientadas a objetos. Seu propósito inclui a análise e projeto da visão estática da aplicação, a descrição das responsabilidades do sistema e serve como base para os diagramas de componente e implantação.



5.3.1 Representação de Classes, Atributos e Métodos
Uma classe é representada por um retângulo dividido em três seções:

Nome da Classe: Na parte superior.


Atributos: Na seção do meio, geralmente representados com visibilidade privada (-).


Métodos: Na seção inferior, geralmente representados com visibilidade pública (+).

5.3.2 Representação de Relacionamentos
5.3.2.1 Associação
É representada por uma linha sólida conectando duas classes. Pode ter um rótulo (estereótipo) com um verbo para descrever a relação, como "faz um".




5.3.2.2 Herança e Especialização
É representada por uma linha sólida com uma seta triangular vazia na ponta, apontando da subclasse para a superclasse.


5.3.2.3 Realização/Implementação
Representa a implementação de uma interface por uma classe. É visualizada como uma linha tracejada com uma seta triangular vazia, apontando da classe que implementa para a interface.



5.3.2.4 Agregação
É representada por uma linha sólida conectando as classes, com um losango vazado do lado da classe "todo" (a que agrega). Indica uma relação "tem", como "Turmas tem Estudantes".


5.3.2.5 Composição
É representada por uma linha sólida com um losango preenchido do lado da classe "todo". Indica uma relação "tem" mais forte, como "Pedido tem Itens Pedido".


5.3.2.6 Dependência
Indica que uma classe (cliente) usa informações ou serviços de outra (fornecedora). É representada por uma linha tracejada com uma seta aberta, apontando da classe cliente para a fornecedora, podendo incluir estereótipos como 

<<use>> ou <<create>>.


5.3.3 Multiplicidade
Informa o número mínimo e máximo de objetos que participam de um relacionamento. É indicada nas extremidades da linha de associação. Exemplos de notação incluem:



0..1: Nenhum ou no máximo um.


1..1 ou 1: Exatamente um.



0..* ou *: Nenhum ou muitos.


1..*: No mínimo um ou muitos.

5.3.4 Classe Associativa
É uma classe que surge da associação entre múltiplos objetos e contém informações específicas sobre essa associação. No diagrama, ela é conectada por uma linha tracejada à linha de associação principal.



5.3.5 Associação Ternária
É um tipo de associação que conecta três objetos de classes distintas ao mesmo tempo.







O que são as regras de negócio em um projeto, considerando poo?



Mostrar raciocínio
Ótima pergunta. Unir o conceito de "regras de negócio" com a Programação Orientada a Objetos (POO) é fundamental para criar softwares eficazes e fáceis de manter.

Com base nos conceitos apresentados nas aulas, podemos definir da seguinte forma:

O que são Regras de Negócio?
Regras de negócio são as políticas, restrições, cálculos e procedimentos que definem como uma organização opera. Elas são a "lógica" da empresa traduzida em critérios que o software deve seguir. Essencialmente, elas ditam o que o sistema pode ou não fazer, e em que condições.

Exemplos simples de regras de negócio:

"Um cliente só pode finalizar uma compra se o valor total do pedido for superior a R$ 20,00."

"Produtos da categoria 'eletrônicos' têm garantia estendida de 1 ano."

"Para se cadastrar, o usuário deve ter no mínimo 18 anos."

"Um desconto de 10% é aplicado automaticamente para clientes VIP."

Como as Regras de Negócio se Materializam na POO?
A POO é um paradigma ideal para implementar regras de negócio porque ela permite modelar o mundo real de forma intuitiva. As regras não ficam espalhadas pelo código, mas sim organizadas e contidas dentro dos objetos aos quais elas pertencem.

Veja como os pilares e conceitos da POO são aplicados:


Classes e Objetos: As classes representam as entidades do negócio sobre as quais as regras atuam. Por exemplo, as regras sobre clientes são implementadas na classe 

Cliente, as regras sobre pedidos na classe Pedido, e assim por diante. Elas são os "substantivos" do seu negócio.

Métodos: É aqui que as regras de negócio são efetivamente implementadas. Os métodos contêm a lógica que valida condições, realiza cálculos e altera o estado dos objetos de forma controlada. Um método chamado 

finalizarPedido(), por exemplo, não apenas muda o status do pedido, mas primeiro verifica todas as regras de negócio associadas (valor mínimo, estoque, pagamento, etc.).

Encapsulamento e Visibilidade: Este é talvez o pilar mais importante para garantir a integridade das regras de negócio. O encapsulamento protege os atributos de um objeto, forçando que toda interação seja feita através de seus métodos. Isso impede que um estado inválido seja criado.

Exemplo prático: Você não pode simplesmente fazer pedido.status = "Aprovado". Você deve chamar o método pedido.aprovar(), que por sua vez verificará se o pagamento foi confirmado, se há estoque, etc. A regra de negócio está protegida dentro do método. A tentativa de alterar um atributo diretamente, como a velocidade no exemplo do 

Carro, é frustrada para garantir que as regras (métodos) sejam seguidas.


Herança e Polimorfismo: A herança permite criar especializações de classes que podem ter regras de negócio diferentes. O polimorfismo permite que essas regras diferentes sejam executadas de forma transparente.


Exemplo prático: Você pode ter uma classe base Cliente e duas subclasses: ClienteComum e ClientePremium. Ambas podem ter um método calcularDesconto(), mas a implementação (a regra de negócio) será diferente para cada uma.

Exemplo Prático: Classe Pedido
Vamos imaginar uma classe Pedido que implementa algumas regras de negócio:

Regras de Negócio:

Um pedido não pode ter mais de 10 itens.

Um item só pode ser adicionado se houver estoque disponível.

O pedido só pode ser finalizado se o valor total for maior que R$ 20,00.

Python

# Exemplo conceitual em Python
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.valor_total = 0.0
        self.status = "Aberto"
        self.__LIMITE_ITENS = 10 # Atributo privado para a regra

    def adicionar_produto(self, produto, quantidade):
        # Regra de Negócio 1: Limite de itens
        if len(self.itens) >= self.__LIMITE_ITENS:
            print("Erro: Limite de itens no pedido excedido.")
            return

        # Regra de Negócio 2: Verificação de estoque
        if produto.tem_estoque(quantidade):
            self.itens.append({"produto": produto, "quantidade": quantidade})
            self.valor_total += produto.preco * quantidade
            produto.decrementar_estoque(quantidade)
            print(f"{produto.nome} adicionado ao pedido.")
        else:
            print(f"Erro: Produto {produto.nome} sem estoque suficiente.")

    def finalizar_pedido(self):
        # Regra de Negócio 3: Valor mínimo para finalizar
        if self.valor_total > 20.00:
            self.status = "Finalizado"
            print(f"Pedido finalizado com sucesso! Valor total: R$ {self.valor_total:.2f}")
        else:
            print("Erro: O valor mínimo para finalizar o pedido é de R$ 20,00.")

Neste exemplo, as regras de negócio não são conceitos abstratos; elas são o código dentro dos métodos adicionar_produto e finalizar_pedido, protegidas pelo encapsulamento da classe Pedido.