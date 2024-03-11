# Interface do Jogo e Habilidades

## Visão Geral
Este script em Python implementa uma interface de jogo simples usando a biblioteca Tkinter. O jogo apresenta um personagem com vários atributos e habilidades, e o usuário pode interagir com o personagem selecionando e executando diferentes habilidades. O script também inclui recursos para ajustar a energia e a vida do personagem.

## Classes

### `Personagem`
- Representa o personagem do jogo com atributos como vida, energia, força, agilidade e várias habilidades.
- Métodos para modificar a vida e a energia.

### `HabilidadeBase`
- Classe base para habilidades do personagem.
- Inclui métodos para rolar dados e exibir mensagens.

### `LuciferPassiva`
- Subclasse de `HabilidadeBase` que representa uma habilidade específica do personagem chamada "Lucifer".
- Implementa diferentes ações, como ataques, nocautes, buffs, debuffs e mais.

### `Belzebub`
- Subclasse de `HabilidadeBase` que representa outra habilidade do personagem chamada "Belzebub".
- Implementa uma habilidade especial com consumo de energia e um teste de manifestação de presença.

### `AjusteEnergiaVida`
- Interface para ajustar a energia e a vida do personagem.
- Permite ao usuário inserir valores para ajuste e fornece botões para adicionar ou reduzir energia e vida.

### `InterfaceSelecaoHabilidade`
- Interface para selecionar habilidades do personagem.
- Exibe botões para as habilidades disponíveis e permite ao usuário escolher uma.

### `InterfaceGrafica`
- Interface principal do jogo que exibe informações sobre a habilidade selecionada e o status do personagem.
- Botões para executar diferentes ações associadas à habilidade escolhida.

## Uso
1. Execute o script em um ambiente Python.
2. O script abrirá uma janela para selecionar as habilidades do personagem.
3. Escolha uma habilidade, e uma nova janela será aberta com a interface do jogo.
4. Use os botões para executar diferentes ações e interagir com o personagem.

**Nota:** Certifique-se de ter a biblioteca Tkinter instalada (`pip install tk`) para executar o script.

Divirta-se jogando com o personagem e explorando as várias habilidades!
