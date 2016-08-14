print(int('11', base=6))
print(int('11', 6))

import functools
int2 = functools.partial(int, base=8)

print(int2('11'))