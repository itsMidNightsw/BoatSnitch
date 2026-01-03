import os

import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches


def id_to_path(fileid, image_or_label):
    """ Takes the id for the image as an input and returns either its path as an image, or as the label"""
    if image_or_label == 'label':
        return "Training_datasets/ship_dataset_v0/" + fileid + '.txt'
    if image_or_label == 'image':
        return "Training_datasets/ship_dataset_v0/" + fileid + '.jpg'
    else:
        raise ValueError('Bad input for image_or_label, please use "label" or "image"')



def read_label(label_path):
    """ Reads the .txt file and returns the denormalized labels"""
    all_labels = []
    with open(label_path, 'r') as f:
        for line in f:
            elements = line.split()
            if not elements:
                continue
            _, x_c, y_c, w, l = [float(x) for x in elements]
            all_labels.append((x_c * 256, y_c * 256, w * 256, l * 256))
    return all_labels

print(read_label(label_path = id_to_path("Sen_ship_hv_02017071802012015", "label"))) # test



def show_image_boxes(img_id: str):
    """ Reads the id and returns the image with the boxes around it"""
    image = Image.open(id_to_path(img_id, 'image'))
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')

    labels = read_label(label_path = id_to_path(img_id, 'label'))

    for x_c, y_c, w, l in labels:
        box = patches.Rectangle(
            (x_c - w / 2, y_c - l / 2),
            w, l,
            linewidth=2,
            edgecolor='b',
            facecolor='none'
        )
        ax.add_patch(box)

    plt.show()

show_image_boxes(img_id = "Sen_ship_hv_02017071802012015")



