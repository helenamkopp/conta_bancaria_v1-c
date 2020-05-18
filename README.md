# conta_bancaria_v1-c

Pequeno projeto Orientado a Objetos, construído utilizando o PyCharm com o objetivo de reforçar o conhecimento sobre classe abstrata. 
Continuação do projeto conta_bancária_v1-b

Principal alteração:

- Tornando a classe Account uma abstract class (abc.ABC).
- Tornando o método update um abstract method.
- Criação de uma nova classe, chamada Investment.

- Percebemos que por se trataem de classes filhas de Account, SavingAccount, CheckingAccount e IvestmentAccount obrigatoriamente precisam 
ter um metodo update. 

- Arquivo main.py: contém um pequeno teste chamando tres clientes, e os tres tipos de conta, apenas para certificar que o método esta 
funcionando como deveria. 
