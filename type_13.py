
import re

typere = 'int|float|long|builtin_function_or_method'

print re.search(typere, '<type"long">').group()
