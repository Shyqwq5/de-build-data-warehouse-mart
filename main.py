from model import make_model
import numpy as np
import pickle
import os

filename = 'predict_model.txt'
filename1 = 'predict_model_X.txt'
filename2 = 'predict_model_y.txt'
if os.path.exists(filename) and  os.path.exists(filename1) and  os.path.exists(filename2):
    with open('predict_model.txt', 'rb') as p:
        model = pickle.load(p)
    with open('predict_model_X.txt', 'rb') as p:
        X_test = pickle.load(p)
    with open('predict_model_y.txt', 'rb') as p:
        y_test = pickle.load(p)
else:
    model,X_test,y_test = make_model()
    with open('predict_model.txt','wb') as p:
        pickle.dump(model, p)
    with open('predict_model_X.txt', 'wb') as p:
        pickle.dump(X_test,p)
    with open('predict_model_y.txt', 'wb') as p:
        pickle.dump(y_test,p)

# loss,accuracy = model.evaluate(X_test, y_test)

# print(loss,accuracy)
def make_good_image(flatten_image):
    f = flatten_image.copy()
    f = np.array([' ' if x == 0 else '#' for x in f])
    image = f.reshape(8, 8)
    return image

def make_good_label(predict_result):
    label = np.argmax(predict_result)
    return label_dict[label]

label_dict = {
    0:"blank",
    1:"horizontal line",
    2:"vertical line",
    3:'diagonal line'
}



i = np.random.randint(len(X_test))
result  = model(np.array([X_test[i]]))
print("The image:")
print(make_good_image(X_test[i]))
print("The prediction:")
print(make_good_label(result))
print("The true:")
print(label_dict[y_test[i]])
