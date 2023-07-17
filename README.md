# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo fila de prioridade (Linked Priority Queue);
- Implementar e validar os conceitos relacionados ao métodos de estruturas de dados fila de prioridade com capacidade.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_fila_prioridade.py -v
```

O pytest permite que você realize o teste sobre métodos específicos da sua estrutura de dados lista duplamente ligada. Portanto, também é válido o comando:

```console
$ pytest test/test_fila_prioridade.py -k is_empty -v --no-header
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe FilaPrioridade** no arquivo **fila_prioridade.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

A prioridade com a qual os itens devem ser inseridos na fila é a seguinte:
- Os itens com maior valor de prioridade devem ocupar as primeiras posições na fila;
- Caso dois itens possuam a mesma prioridade, aquele que foi inserido primeiro deverá ter maior prioridade na fila para ser removido;

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **10pts**, o que corresponde a **10pts%** da nota da segunda etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo fila de prioridade
- [ ] **(0pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na fila de prioridade ou False, caso contrário
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **is_full()**
  - [ ] Deve retornar um boolean True se houver itens (Nó) na fila de prioridade ou False, caso contrário
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **frist()**
  - [ ] Deve retornar uma referência para o primeiro item (Nó) da fila de prioridade ou None, caso a fila de prioridade esteja vazia
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(6pts)** Implementar o método **add()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido no início da fila de prioridade
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) em ordem crescente na fila de prioridade
  - [ ] Caso a fila de prioridade tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido em ordem crescente na fila de prioridade e método deverá retornar um boolean True
- [ ] **(2pts)** Implementar o método **remove()**, o qual deve remover o primeiro item da fila de prioridade, caso ela não esteja vazia 
  - [ ] Caso a fila de prioridade esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso a fila de prioridade esteja vazia deverá retornar o primeiro Nó da fila
- [ ] **(2pts)** Implementar o método **display()**, o qual deve retornar uma lista de tuplas com os valores (atributo dado e prioridade) dos itens (Nó) inseridos na fila de prioridade
  - [ ] Caso a fila de prioridade esteja vazia deverá retornar uma lista vazia []
- [ ] **(0pts)** Implementar o método **size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a fila de prioridade esteja vazia, ou, caso possua algum item na fila de prioridade, o valor relativo à quantidade de itens presentes na fila de prioridade
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo