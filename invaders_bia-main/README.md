# Space Invaders - Projeto de Programação Orientada a Objetos

Este é um jogo Space Invaders desenvolvido como projeto acadêmico no **Bacharelado de Inteligência Artificial da UFG**, na disciplina de **Programação Orientada a Objetos** do professor **Vinícius Sebba Patto**. O projeto demonstra a aplicação prática e rigorosa dos conceitos fundamentais e pilares da POO.

## Paradigma de Programação Orientada a Objetos

Este projeto exemplifica a **Programação Orientada a Objetos (POO)** como paradigma de programação, contrastando com a programação imperativa e estruturada. A POO permite modelar o mundo real através de objetos que interagem entre si, proporcionando maior organização, reutilização e manutenibilidade do código.

## Conceitos Fundamentais de POO Implementados

### Modelo de Objetos
O jogo modela entidades do mundo real como objetos computacionais:
- **Jogador**: Representa a nave espacial controlada pelo usuário
- **Inimigo**: Representa as naves invasoras
- **Projétil**: Representa os tiros disparados
- **Pontuação**: Representa o sistema de pontos e vidas

### Classes e Instâncias
Cada entidade é definida por uma **classe** que serve como molde, e durante o jogo são criadas **instâncias** específicas:

```python
# Classe define o molde
class Jogador:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__largura = 50
        self.__altura = 30

# Instância específica criada durante o jogo
jogador = Jogador(400, 550)  # Nave na posição específica
```

### Atributos e Propriedades
Todas as classes implementam **encapsulamento completo** com atributos privados e **properties** para acesso controlado:

```python
class Jogador:
    def __init__(self, x, y):
        self.__x = x           # Atributo privado
        self.__y = y           # Atributo privado
        self.__velocidade = 5  # Atributo privado
        self.__tiros = []      # Lista privada

    @property
    def velocidade(self):      # Property para acesso controlado
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade):
        if 0 <= nova_velocidade <= 20:  # Validação
            self.__velocidade = nova_velocidade
```

### Métodos
Cada classe possui métodos que definem seus comportamentos específicos:
- **Métodos de Dados**: Getters e setters para acesso controlado
- **Métodos de Negócio**: Lógicas específicas de cada entidade
- **Métodos de Controle**: Coordenação e renderização

## Pilares da POO Implementados

### Encapsulamento e Visibilidade
**Implementação Completa**: Todos os atributos são privados (usando `__atributo`) com acesso controlado através de properties.

**Acesso Público e Privado**:
- **Público**: Properties e métodos de interface
- **Privado**: Atributos internos protegidos com validação

```python
# Acesso público controlado
jogador.x = 100  # Usa property com validação de limites

# Acesso privado protegido
# jogador.__x = 100  # Erro - atributo privado inacessível
```



## Elementos Avançados de POO

### Construtores
Todas as classes implementam construtores adequados usando `__init__()` para inicialização de atributos.

### Variáveis de Instância
Cada objeto possui suas próprias variáveis de instância, permitindo múltiplas entidades independentes:

```python
# Cada inimigo tem suas próprias variáveis
inimigo1 = Inimigo(100, 50, 1)  # Posição e tipo específicos
inimigo2 = Inimigo(200, 50, 2)  # Diferentes do primeiro
```

### Comunicação Entre Objetos
O projeto demonstra comunicação estruturada entre objetos através de métodos e delegação:

```python
# Jogo coordena comunicação entre objetos
def verificar_colisoes(self):
    for tiro in self.jogador.obter_tiros():
        for inimigo in self.inimigos:
            if tiro.rect.colliderect(inimigo.rect):
                # Objetos interagem através de métodos
                self.jogador.remover_tiro(tiro)
                self.inimigos.remove(inimigo)
```

## Relacionamentos Entre Classes

### Composição
A classe `Jogo` **contém** instâncias de outras classes, demonstrando o relacionamento "tem um":

```python
class Jogo:
    def __init__(self):
        self.jogador = Jogador(400, 550)      # Jogo TEM UM jogador
        self.inimigos = self.criar_inimigos() # Jogo TEM inimigos
        self.pontuacao = Pontuacao()          # Jogo TEM pontuação
```

### Delegação
O controlador delega responsabilidades específicas para classes especializadas:

```python
# Jogo delega movimento para JogadorBusiness
def mover_jogador_esquerda(self):
    self.jogador_business.mover_esquerda(LARGURA_TELA)

# Jogo delega lógica de pontuação para PontuacaoBusiness
def adicionar_pontos(self, pontos):
    self.pontuacao_business.adicionar_pontos(pontos)
```

## Arquitetura do Projeto

### Separação de Responsabilidades
```
Dados/                    → Estruturas de dados puras
├── jogador.py           → Dados do jogador
├── inimigo.py           → Dados dos inimigos
├── projetil.py          → Dados dos projéteis
└── pontuacao.py         → Dados de pontuação

Business/                 → Regras de negócio
├── jogador_business.py  → Lógicas do jogador
├── inimigo_business.py  → Lógicas dos inimigos
├── projetil_business.py → Lógicas dos projéteis
└── pontuacao_business.py → Lógicas de pontuação

jogo.py                   → Controlador principal
main.py                   → Ponto de entrada
utils.py                  → Utilitários e constantes
```

### Benefícios da Arquitetura POO
- **Manutenibilidade**: Mudanças localizadas em classes específicas
- **Reutilização**: Código organizado em classes especializadas
- **Extensibilidade**: Fácil adição de novos tipos de entidades
- **Testabilidade**: Classes isoladas facilitam testes unitários
- **Organização**: Responsabilidades claramente definidas

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pygame

### Instalação e Execução
```bash
# Instalar dependências
pip install pygame

# Executar o jogo
python main.py
```

### Controles
- **Movimento**: Setas direcionais ou WASD
- **Atirar**: Z ou Espaço
- **Menu**: Enter para selecionar, ESC para voltar

## Funcionalidades Implementadas

- ✅ **Sistema de Menu**: Navegação completa com teclado
- ✅ **Movimento 4 Direções**: Controle total da nave
- ✅ **Sistema de Tiro**: Projéteis do jogador e inimigos
- ✅ **Colisões Avançadas**: Incluindo projétil vs projétil
- ✅ **Sistema de Pontuação**: Pontos e vidas com persistência
- ✅ **Efeitos Visuais**: Explosões animadas
- ✅ **Hierarquia de Inimigos**: 3 tipos com pontuações diferentes

## Demonstração dos Conceitos POO

Este projeto serve como exemplo prático de como a **Programação Orientada a Objetos** permite:

1. **Modelar o mundo real** através de classes e objetos
2. **Proteger dados** através de encapsulamento
3. **Organizar responsabilidades** através de separação de camadas
4. **Facilitar manutenção** através de arquitetura bem estruturada

O resultado é um código **limpo, organizando, extensível e academicamente correto**, demonstrando a aplicação prática dos conceitos fundamentais da Programação Orientada a Objetos.