import numpy as np

def generate_blank(image_size=(8,8)):
    empty_image = np.zeros(image_size, dtype=int)
    return empty_image

def generate_horizontal_line():
    line_index = np.random.randint(8)
    empty_image = generate_blank()
    empty_image[line_index] = [1,1,1,1,1,1,1,1]
    return empty_image



# print(generate_horizontal_line())
#labels
#num_samples

def generate_image_dataset(samples_per_class=100):
    X_list = []
    y_list = []
    for i in range(samples_per_class):
        X_list.append(generate_blank().flatten())
        y_list.append(0)
        X_list.append(generate_horizontal_line().flatten())
        y_list.append(1)
        X_list.append(generate_vertical_line().flatten())
        y_list.append(2)
    return np.array(X_list),np.array(y_list)

def generate_vertical_line():
    image = generate_horizontal_line()
    image = np.rot90(image, k=1, axes=(0, 1))
    return image

    # row_index = np.random.randint(8)
    # empty_image = generate_blank()
    # for i in range(8):
    #     empty_image[i][row_index] = 1
    # return empty_image