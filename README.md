# TO-DO Servers

## Descrição

Repositório destinado ao desenvolvimento do projeto de sistemas distribuídos da Universidade Paulista de Campinas, do curso de Ciência da Computação, 8o sem.

## Proposta

Nossa proposta é desenvolver um sistema de lista de tarefas onde teremos um
servidor que salvará as tarefas no banco de dados A, outro servidor B no qual
gerará relatórios sobre as tarefas que foram inseridas no servidor A e um terceiro
servidor que será o cliente, onde realizará acessos em ambos os servidores A e
B, desta forma, teremos um sistema distribuído que se comunicarão entre si.

![Estrutura do Projeto](/Files/Docs/APS/Images/topografia.drawio.png)

## Integrantes

|  Nome  |  RA  |
| ------ | ---- |
| Carlos Eduardo dos Santos Ferreira | N6401C7 |
| Gabriel Menezes de Antonio | F13GJI6 |
| Gustavo Henrique Dos Santos Faria | F22IFG2 |
| Mayara Marques Pereira de Souza | N542DD1 |

## Requisitos e dependências

|  Requisito  |   Versão   |  Servidor   |
| :---------: | :--------: | :---------: |
|   Python    |   3.11.4   | Relatórios  |
|   Dotnet    |  7.0.401   |    TODO     |
|    Node     |   9.6.7    |   Cliente   |

## Servidores

### URL base

* Servidor de tarefas: <http://localhost:5017/>
* Servidor de relatórios: <http://localhost:8000/>
* Cliente: <http://localhost:3000/>

### Inicialização

Para inicializar todos os servidores, execute o script `run_project.bat`

Esse script irá executar o script de inicialização de cada respectivo servidor em sua própria instância do terminal. Os scripts são:

* `/ReportsServer/run_reports_server.bat`
* `/TodoServer/run_todo_server.bat`
* `/Client/run_client_server.bat`
