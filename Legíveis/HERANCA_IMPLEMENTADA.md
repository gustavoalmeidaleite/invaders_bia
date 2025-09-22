# IMPLEMENTAÇÃO COMPLETA DO CONCEITO DE HERANÇA

## 📋 RESUMO DA IMPLEMENTAÇÃO

Implementação completa do conceito de **HERANÇA** no projeto Space Invaders, seguindo rigorosamente os princípios das aulas do Dr. Edson Nascimento sobre Programação Orientada a Objetos.

---

## 🎯 HIERARQUIA DE CLASSES IMPLEMENTADA

### **SUPERCLASSE: EntidadeJogo**

**Arquivo**: `Dados/entidade_jogo.py`

**Responsabilidade**: Classe base que contém atributos e métodos comuns a todas as entidades do jogo.

**Atributos Comuns**:
- `_x`, `_y` (posição)
- `_largura`, `_altura` (dimensões)
- `_rect` (retângulo para colisão)
- `_sprite` (imagem da entidade)

**Métodos Comuns**:
- Properties para `x`, `y`, `largura`, `altura`, `rect`, `sprite`
- `atualizar_posicao(novo_x, novo_y)`
- `obter_centro()` - retorna centro da entidade
- `esta_dentro_da_tela()` - verifica se está na tela
- `__str__()` - representação em string

---

## 🔄 SUBCLASSES IMPLEMENTADAS

### **1. SUBCLASSE: Jogador**

**Arquivo**: `Dados/jogador.py`

**Herança Implementada**:
```python
class Jogador(EntidadeJogo):
    def __init__(self, x: int, y: int, largura: int = 50, altura: int = 30):
        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, "player_ship.png")
        
        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__velocidade = VELOCIDADE_JOGADOR
        self.__tiros = []
```

**Especialização**:
- ✅ **Atributos Específicos**: `velocidade`, `tiros`
- ✅ **Sobrescrita de Setters**: Validação específica para limites da tela
- ✅ **Métodos Específicos**: `adicionar_tiro()`, `remover_tiro()`, `limpar_tiros()`
- ✅ **Sobrescrita de `__str__()`**: Inclui informações específicas do jogador

**Exemplo de Sobrescrita**:
```python
@x.setter
def x(self, novo_x: int):
    """SOBRESCRITA: Validação específica do jogador."""
    if 0 <= novo_x <= LARGURA_TELA - self.largura:
        super(Jogador, self.__class__).x.fset(self, novo_x)
    else:
        # Mantém dentro dos limites da tela
        if novo_x < 0:
            super(Jogador, self.__class__).x.fset(self, 0)
        else:
            super(Jogador, self.__class__).x.fset(self, LARGURA_TELA - self.largura)
```

### **2. SUBCLASSE: Inimigo**

**Arquivo**: `Dados/inimigo.py`

**Herança Implementada**:
```python
class Inimigo(EntidadeJogo):
    def __init__(self, x: int, y: int, largura: int = 40, altura: int = 25, tipo: int = 1):
        # Determina sprite baseado no tipo
        sprite_names = {1: "invader_type1.png", 2: "invader_type2.png", 3: "invader_type3.png"}
        sprite_name = sprite_names.get(tipo, "invader_type1.png")
        
        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, sprite_name)
        
        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__direcao = 1  # 1 = direita, -1 = esquerda
        self.__tipo = tipo
```

**Especialização**:
- ✅ **Atributos Específicos**: `tipo`, `direcao`
- ✅ **Sobrescrita de Setters**: Permite movimento além das bordas da tela
- ✅ **Validação Específica**: Direção aceita apenas -1 ou 1
- ✅ **Sobrescrita de `__str__()`**: Inclui tipo e direção

### **3. SUBCLASSE: Projetil**

**Arquivo**: `Dados/projetil.py`

**Herança Implementada**:
```python
class Projetil(EntidadeJogo):
    def __init__(self, x: int, y: int, largura: int = 6, altura: int = 15, eh_inimigo: bool = False):
        # Determina sprite e cor baseado no tipo
        if eh_inimigo:
            sprite_name = "bullet_enemy.png"
            cor_fallback = COR_TIRO_INIMIGO
        else:
            sprite_name = "bullet_player.png"
            cor_fallback = COR_TIRO
        
        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, sprite_name)
        
        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__eh_inimigo = eh_inimigo
        self.__cor_fallback = cor_fallback
```

**Especialização**:
- ✅ **Atributos Específicos**: `eh_inimigo`, `cor_fallback`
- ✅ **Sem Sobrescrita de Setters**: Usa validação da superclasse (movimento livre)
- ✅ **Método Especializado**: `atualizar_posicao()` usa `super()`
- ✅ **Sobrescrita de `__str__()`**: Inclui tipo de projétil

---

## 📊 BENEFÍCIOS DA HERANÇA IMPLEMENTADA

### **1. REUTILIZAÇÃO DE CÓDIGO**

**Antes da Herança**:
```python
# Código duplicado em cada classe
class Jogador:
    def __init__(self, x, y, largura, altura):
        self.__x = x
        self.__y = y
        self.__largura = largura
        self.__altura = altura
        self.__rect = pygame.Rect(x, y, largura, altura)
        # ... properties duplicadas

class Inimigo:
    def __init__(self, x, y, largura, altura):
        self.__x = x  # DUPLICAÇÃO
        self.__y = y  # DUPLICAÇÃO
        # ... mesmo código repetido
```

**Depois da Herança**:
```python
# Código comum na superclasse
class EntidadeJogo:
    def __init__(self, x, y, largura, altura, sprite_nome):
        self._x = x
        self._y = y
        # ... código comum uma única vez

# Subclasses reutilizam o código
class Jogador(EntidadeJogo):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 30, "player_ship.png")  # REUTILIZAÇÃO
        # ... apenas código específico
```

### **2. MANUTENIBILIDADE**

- **Mudanças Centralizadas**: Alterações na `EntidadeJogo` afetam todas as subclasses
- **Código Limpo**: Eliminação de duplicação
- **Facilidade de Extensão**: Novas entidades herdam automaticamente funcionalidades básicas

### **3. POLIMORFISMO PREPARADO**

```python
# Agora é possível tratar todas as entidades de forma uniforme
def processar_entidade(entidade: EntidadeJogo):
    centro = entidade.obter_centro()  # Funciona para qualquer subclasse
    print(entidade)  # Chama o __str__ específico de cada subclasse
```

---

## 🧪 TESTES DE VALIDAÇÃO

### **Teste de Herança Executado**:

```python
from Dados.jogador import Jogador
from Dados.inimigo import Inimigo
from Dados.entidade_jogo import EntidadeJogo

jogador = Jogador(100, 200)
print(f'Jogador é instância de EntidadeJogo: {isinstance(jogador, EntidadeJogo)}')
# Resultado: True

inimigo = Inimigo(150, 100, tipo=2)
print(f'Inimigo é instância de EntidadeJogo: {isinstance(inimigo, EntidadeJogo)}')
# Resultado: True
```

**✅ RESULTADOS DOS TESTES**:
- ✅ `isinstance(jogador, EntidadeJogo)` = `True`
- ✅ `isinstance(inimigo, EntidadeJogo)` = `True`
- ✅ `isinstance(projetil, EntidadeJogo)` = `True`
- ✅ Sobrescrita de métodos funcionando
- ✅ Especialização de comportamentos implementada
- ✅ Métodos herdados acessíveis

---

## 🎓 CONFORMIDADE COM TEORIA POO

### **Conceitos Implementados Conforme Aulas do Dr. Edson**:

#### **2.2 HERANÇA**
✅ **"Herança é um mecanismo que permite a uma classe (subclasse) herdar atributos e métodos de outra classe (superclasse)"**
- Implementado: `Jogador`, `Inimigo`, `Projetil` herdam de `EntidadeJogo`

#### **2.2.1 Superclasses e Subclasses**
✅ **"Superclasse (ou classe mãe): É a classe mais genérica que cede suas características"**
- Implementado: `EntidadeJogo` é a superclasse genérica

✅ **"Subclasse (ou classe filha): É a classe que herda da superclasse, representando uma especialização dela"**
- Implementado: `Jogador`, `Inimigo`, `Projetil` são especializações

#### **Uso Correto de `super()`**:
```python
# Conforme modelo das aulas
def __init__(self, x, y):
    super().__init__(x, y, largura, altura, sprite_nome)  # Chama construtor da superclasse
    self.__atributo_especifico = valor  # Adiciona especialização
```

---

## 🏗️ ESTRUTURA FINAL

```
EntidadeJogo (SUPERCLASSE)
├── Atributos: _x, _y, _largura, _altura, _rect, _sprite
├── Métodos: properties, atualizar_posicao(), obter_centro(), __str__()
│
├── Jogador (SUBCLASSE)
│   ├── Herda: todos os atributos e métodos da superclasse
│   ├── Adiciona: __velocidade, __tiros
│   ├── Sobrescreve: setters x/y (validação de tela), __str__()
│   └── Especializa: métodos de tiro
│
├── Inimigo (SUBCLASSE)
│   ├── Herda: todos os atributos e métodos da superclasse
│   ├── Adiciona: __tipo, __direcao
│   ├── Sobrescreve: setters x/y (permite além das bordas), __str__()
│   └── Especializa: validação de direção
│
└── Projetil (SUBCLASSE)
    ├── Herda: todos os atributos e métodos da superclasse
    ├── Adiciona: __eh_inimigo, __cor_fallback
    ├── Mantém: setters da superclasse (movimento livre)
    ├── Sobrescreve: __str__()
    └── Especializa: atualizar_posicao() com super()
```

---

## 🏆 RESULTADO FINAL

**HERANÇA 100% IMPLEMENTADA** seguindo rigorosamente os princípios das aulas de POO:

- ✅ **Superclasse Genérica**: `EntidadeJogo` com código comum
- ✅ **Subclasses Especializadas**: `Jogador`, `Inimigo`, `Projetil`
- ✅ **Reutilização de Código**: Eliminação de duplicação
- ✅ **Sobrescrita de Métodos**: Especialização de comportamentos
- ✅ **Uso Correto de `super()`**: Chamadas adequadas à superclasse
- ✅ **Manutenibilidade**: Código organizado e extensível
- ✅ **Preparação para Polimorfismo**: Base para próximos pilares

A implementação demonstra perfeitamente o conceito de **"especializar uma classe mais geral"**, onde `EntidadeJogo` representa o conceito geral de uma entidade do jogo, e as subclasses representam especializações específicas (jogador, inimigo, projétil).
