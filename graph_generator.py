import argparse
import json
import matplotlib.pyplot as plt


arg_parser = argparse.ArgumentParser()
colors = ["#3EC70B", "#FF0000", "#3B44F6", "#FF5B00", "#0E185F", "#243D25"]

arg_parser.add_argument(
    "-m", "--model", nargs="+", required=True,
    choices=[
        'professores_model', 'quem_model', 'que_model', 
        'qual_model', 'porque_model', 'tcc_model', 
        'propina_model', 'main_model', 'notas_model', 
        'quanto_model', 'quando_model', 'onde_model', 
        'matricula_candidatura_model'
    ],

    help="Add the model to use on the graphic plot."
)


def generation_metrics_name(metrics: list) -> str: 
    if "acc" in metrics and "loss" not in metrics: 
        return "Accuracy"
    elif "loss" in metrics and "acc" not in metrics: 
        return "Loss"
    else:
        return "Accuracy & Loss"


def generate_acc_loss_graph(data: dict, model_name: str, metrics=["acc", "loss"]) -> None:
    plt.plot(data["acc"], color=colors[0],
             label="Accuracy") if "acc" in metrics else None
    plt.plot(data["loss"], color=colors[1],
             label="Loss") if "loss" in metrics else None
    acc_values = [value for value in data["acc"] if value <= 1 and value >= 0]
    loss_values = [value for value in data["loss"]
                   if value <= 1 and value >= 0]

    print(f"\n\nARVERAGE {model_name.upper()} MODEL VALUES:\n")
    print(f" * Accuracy Average: {sum(acc_values)/len(acc_values)}")
    print(f" * Loss Average: {sum(loss_values)/len(loss_values)}\n")

    metrics_names = generation_metrics_name(metrics)

    plt.legend()
    plt.title(f"{model_name.capitalize()} Model {metrics_names}", pad=18,
              fontname="Times New Roman", fontweight="bold", fontsize=12,
              )
    plt.xlabel("Epochs", fontname="Times New Roman", fontweight='bold')
    plt.ylabel("Values", fontname="Times New Roman", fontweight='bold')
    plt.grid(axis="y", linewidth=0.4)
    plt.grid(axis="x", linewidth=0.2)
    plt.show()


args = vars(arg_parser.parse_args())
print(args["model"])

for model in args["model"]:
    # opening all the json files
    json_files = open(f'./data/cleaned_data/{model}.json')
    # load all the data
    data = json.load(json_files)

    model_name = model.split("_")[0]

    data_dict = {
        "acc": [value[2] for value in data],
        "loss": [value[1] for value in data],
        "epoch": [value[0] for value in data]
    }

    generate_acc_loss_graph(data_dict, model_name)
    generate_acc_loss_graph(data_dict, model_name, metrics=["acc"])
    generate_acc_loss_graph(data_dict, model_name, metrics=["loss"])
