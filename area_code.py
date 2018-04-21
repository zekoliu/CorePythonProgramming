
import re

area_code = '(\d{3}-)?\d{3}-\d{4}'
area_code1 = "\(?\d{3}\)?-?\d{3}-\d{4}"

print re.match(area_code1, '(808)555-1212').group()