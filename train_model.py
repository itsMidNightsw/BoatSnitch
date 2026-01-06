import os
from show_training_data import id_to_path
from show_training_data import read_label

files = [f for f in os.listdir("Training_datasets/ship_dataset_v0/") if f.endswith(".jpg")]
ids_list = []

for i in files:
    img_id = i.split(".")
    ids_list.append(img_id[0])



ids_list_hh = [img_id for img_id in ids_list if "hh" in img_id]
print(len(ids_list_hh))

