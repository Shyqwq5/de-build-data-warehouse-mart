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


def generate_vertical_line():
    image = generate_horizontal_line()
    image = np.rot90(image, k=1, axes=(0, 1))
    return image


def generate_diagonal_line():
    index = np.random.randint(8)
    direction =  np.random.randint(2)
    line_index = 0
    image =  generate_blank()
    if index == 0 or (direction == 0 and index!=7):
        for i in range(index,8):
            image[line_index][i] = 1
            line_index+=1
    else:
        for i in range(index,-1,-1):
            image[line_index][i] = 1
            line_index+=1
    return image



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
        X_list.append(generate_diagonal_line().flatten())
        y_list.append(3)
    return np.array(X_list),np.array(y_list)



# row_index = np.random.randint(8)
# empty_image = generate_blank()
# for i in range(8):
#     empty_image[i][row_index] = 1
# return empty_image