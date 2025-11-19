import numpy as np

def generate_blank(image_size=(8,8)):
    empty_image = np.zeros(image_size, dtype=int)
    return empty_image

def generate_horizontal_line():
    line_index = np.random.randint(8)
    empty_image = generate_blank()
    empty_image[line_index] = [1,1,1,1,1,1,1,1]
    return empty_image


print(generate_horizontal_line())