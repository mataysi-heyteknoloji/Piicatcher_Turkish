#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:46:31 2024

@author: mat
"""

from piicatcher.detectors import DatumDetector, MetadataDetector, register_detector
from typing import Optional
from dbcat.catalog.models import CatColumn
from dbcat.catalog.pii_types import PiiType
import re


class CC(PiiType):
    name = "Credit Card"
    type = "credit_card"
    pass


@register_detector
class ColumnCreditCardDetector(MetadataDetector):

    regex = re.compile("credit_card_no", re.IGNORECASE)
    name = "ColumnNameCreditCardDetector"

    def detect(self, column: CatColumn) -> Optional[PiiType]:
        if self.regex.match(column.name) is not None:
            return CC()

        return None


@register_detector
class DatumCreditCardDetector(DatumDetector):
    regex = re.compile(r"^([0-9]{4})\s?([0-9]{4})\s?([0-9]{4})\s?([0-9]{4})$")
    name = "DatumCreditCardDetector"

    def detect(self, column: CatColumn, datum: str) -> Optional[PiiType]:
        if self.regex.match(datum) is not None:
            return CC()

        return None
