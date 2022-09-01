## Como rodar

Antes de executar os passos tenha certesa que as dependencias estão instaladas


- Primeiro ordenar os dados por pastas;
- Segundo rodar o clean_data.py para limpar os dados e os ordenar em formato json
    ```
        python clean_dat.py
    ```
- Terceiro rodar o graph_generator.py para gerar os gráficos relativo a um modelo fornecido
    ```
        python graph_generator.py -m main_model
    ```
    Isso ira gerar 3 gráficos para o mesmo modelo, um para a accuracy, um para o loss e outro para ambos os dois
