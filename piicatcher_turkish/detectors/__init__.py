from .TC_number import ColumnTCDetector
from .TC_number import DatumTCDetector
from .credit_card import ColumnCreditCardDetector
from .credit_card import DatumCreditCardDetector

from dbcat.catalog.pii_types import PiiType


class CC_number(PiiType):
    name = "Credit Card"
    type = "credit_card"
    pass


class TC_number(PiiType):
    name = "TC number"
    type = "TC_number"
    pass
