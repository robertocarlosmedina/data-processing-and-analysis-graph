# Data Processing and Analysis with graph

Clearing terminal output and generation graphs related to loss and accuracy training values of some models

## Como rodar

Before executing the steps make sure the dependencies are installed


- First sort the data by masses;
- Second run clean_data.py to clean the data and sort it in json format
    ```
        python clean_data.py
    ```
- Third, run graph_generator.py to generate graphs relative to a specified model
    ```
        python graph_generator.py -m main_model
    ```
    This will generate 3 graphs for the same model, one for accuracy, one for loss and one for both.

