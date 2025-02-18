# 📝 Gerenciador de Tarefas (POO + SOLID)

Este é um **Gerenciador de Tarefas** implementado em Python, utilizando **Princípios de POO (Programação Orientada a Objetos)** e os **Princípios SOLID** para fins de estudo.  

## 🚀 Funcionalidades

- Criar e gerenciar tarefas.
- Marcar tarefas como concluídas.
- Verificar se há tarefas atrasadas.
- Verificar tarefas concluídas.
- Enviar notificações (por e-mail ou SMS) ao adicionar, atrasar ou concluir uma tarefa.

## 🏗️ Conceitos de POO Aplicados

✔ **Encapsulamento** – Uso de atributos privados e métodos públicos nas classes.  
✔ **Herança e Polimorfismo** – Criação da interface `Notifier` e suas subclasses `EmailNotifier` e `SMSNotifier`.  
✔ **Composição** – `User` contém uma lista de `Task` e um `Notifier`.  

## 🧑‍🏫 Princípios SOLID Aplicados

✔ **SRP (Princípio da Responsabilidade Única)** – Cada classe tem uma única responsabilidade.  
✔ **OCP (Princípio Aberto/Fechado)** – Possibilidade de adicionar novos tipos de notificadores sem alterar o código existente.  
✔ **LSP (Princípio da Substituição de Liskov)** – `Notifier` pode ser substituído por qualquer uma de suas subclasses.  
✔ **ISP (Princípio da Segregação de Interface)** – `Notifier` define apenas o necessário para suas subclasses.  
✔ **DIP (Princípio da Inversão de Dependência)** – `User` depende da abstração `Notifier`, e não de uma implementação concreta.  

## 🛠️ Como Executar o Projeto

**OBS: O projeto utiliza o `uv` como ferramenta para gerenciar dependências, ambiente (venv) e versão do python.**

1. Clone o repositório:
   ```sh
   git clone https://github.com/aluisiolucio/poo-solid-task-manager
   cd poo-solid-task-manager
   ```

3. Execute o script:
   ```sh
   python main.py
   ```

## 📂 Estrutura do Projeto

```
📂 poo-solid-task-manager
│── 📄 main.py        # Código principal do sistema
│── 📄 README.md      # Documentação do projeto
```
