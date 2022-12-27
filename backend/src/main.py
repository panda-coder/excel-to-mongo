#!/usr/bin/env python3

import sys
from excel_file import ExcelFile


file_name = sys.argv[1]
excel = ExcelFile(file_name)
excel.print_content()