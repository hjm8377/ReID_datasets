# from .dukemtmcreid import DukeMTMCreID
# from .market1501 import Market1501
# from .msmt17 import MSMT17
# from .veri import VeRi
from .knight import KnightC1C2
from .dataset_loader import ImageDataset

__factory = {
    # 'market1501': Market1501,
    # # 'cuhk03': CUHK03,
    # 'dukemtmc': DukeMTMCreID,
    # 'msmt17': MSMT17,
    # 'veri': VeRi,
    'knight': KnightC1C2,
}


def get_names():
    return __factory.keys()


def init_dataset(name, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown datasets: {}".format(name))
    return __factory[name](*args, **kwargs)