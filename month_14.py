
import re

month_re = '(1[0-2])'

print re.match(month_re, '12').group()