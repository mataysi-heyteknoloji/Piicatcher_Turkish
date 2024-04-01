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
from piicatcher_turkish.detectors import TC_number


@register_detector
class ColumnTCDetector(MetadataDetector):

    regex = re.compile("kimlik_no", re.IGNORECASE)
    name = "ColumnNameTCDetector"

    def detect(self, column: CatColumn) -> Optional[PiiType]:
        if self.regex.match(column.name) is not None:
            return TC_number()

        return None


@register_detector
class DatumTCDetector(DatumDetector):
    regex = re.compile("[^[1-9]{1}[0-9]{9}[02468]{1}$")
    name = "DatumTCDetector"

    def detect(self, column: CatColumn, datum: str) -> Optional[PiiType]:
        if self.regex.match(datum) is not None:
            return TC_number()

        return None
