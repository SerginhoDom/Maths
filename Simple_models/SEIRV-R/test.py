try:
    from fenics import *
except ImportError as e:
    print("FEniCS не установлен или путь не настроен правильно.")
    raise e