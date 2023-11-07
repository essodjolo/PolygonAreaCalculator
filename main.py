import test_module

if __name__ == '__main__':
    print("Running unit tests...")

    exec("test_module")

    testing = test_module.MyTestCase()

    testing.test_get_area()
    testing.test_get_perimeter()
    testing.test_get_diagonal()
    testing.test__repr__()
    testing.test_get_picture()
    testing.test_get_amount_inside()

    print("Done.")
