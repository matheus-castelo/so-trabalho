# Questão 2

Cinco programadores estão trabalhando em um laboratório. Cada um está desenvolvendo um módulo diferente de um grande sistema, mas todos precisam compilar seus códigos com recursos limitados: um compilador e um banco de dados de dependências compartilhado.

Cada programador:

* Precisa adquirir acesso exclusivo ao compilador.
* Precisa de acesso compartilhado ao banco de dados, mas apenas dois programadores podem acessá-lo simultaneamente para evitar sobrecarga.
* Após compilar, o programador descansa (pensa) por algum tempo e depois tenta compilar novamente.

Regras:

* Apenas um programador pode usar o compilador por vez.
* No máximo dois programadores podem acessar o banco de dados ao mesmo tempo.
* Um programador só pode começar a compilação quando tiver ambos os recursos.
* O sistema deve evitar deadlocks e inanição.

Apresente a saída de forma que seja possível identificar a atividade ou estado de momento de cada programador. Faça com que execute em laço infinito para sua apresentação em sala.

---

