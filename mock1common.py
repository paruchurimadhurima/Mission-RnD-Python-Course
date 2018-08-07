# defines common types and utils that are used across tests.
# DO NOT MODIFY OR ADD TO THIS FILE.
# DO NOT SUBMIT THIS FILE as we will use a common file (our copy) for all tests.

from enum import Enum, auto
from collections import namedtuple

class Corner(Enum):
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_RIGHT = auto()

    # for a more friendly prints of EncryptKey
    def __repr__(self):
        return str(self)


#specifies the encryption parameters specified in the example
EncryptKey = namedtuple("EncryptKey", 'rows cols corner')
