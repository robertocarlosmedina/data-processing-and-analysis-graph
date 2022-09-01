import json
import os


# Get the list of .txt files and directories that contein the training datas
path = "./"
dir_list = os.listdir(path)
all_data_files = [item for item in dir_list if ".txt" in item]


for file_name in all_data_files:

    data_list = []
    file = open(file_name, "r")
    file_name = file_name.split(".")[0]
    print(f"Getting {file_name} datas...")

    for line in file.readlines():

        if "|" in line and "epoch" in line:
            line_data = line.split(" | ")
            line_data = line_data[:2] + line_data[2].split(" - ")
            line_data = line_data[:3] + line_data[3].split(" -- ")
            epoch = int(line_data[1].split(": ")[1])
            loss = float(line_data[2].split(": ")[1])
            acc = float(line_data[3].split(": ")[1])
            # print(f"epoch: {epoch}; loss: {loss}; acc: {acc}")
            if data_list:
                if epoch != data_list[len(data_list)-1][0]:
                    data_list.append([epoch, loss, acc])
            else:
                data_list.append([epoch, loss, acc])

    # Serializing json
    json_object = json.dumps(data_list, indent=4)
    
    # Saving the data on json file
    with open(f"{file_name}.json", "w") as outfile:
        outfile.write(json_object)
