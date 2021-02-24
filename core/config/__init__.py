import os


def load_config():
    """
    Load config according to environment.
    """
    mode = os.environ.get('MODE')

    if mode == 'PRODUCT':
        print('if.MODE:', mode)
        from .product import ProductConfig
        return ProductConfig
    elif mode == 'TESTING':
        print('elif.MODE:', mode)
        from .test import TestConfig
        return TestConfig
    elif mode == 'RELEASE':
        print('elif.MODE:', mode)
        from .release import ReleaseConfig
        return ReleaseConfig
    else:
        print('else.MODE:', mode)
        from .test import TestConfig
        return TestConfig



config = load_config()

