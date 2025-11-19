from data import generate_image_dataset

def test_generate_image():
    X,y = generate_image_dataset(3)
    assert X.shape == (6, 64)
    assert y.shape == (6,)
    X,y = generate_image_dataset(100)
    assert X.shape == (200, 64)
    assert y.shape == (200,)
