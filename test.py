#!/usr/bin/python3

str = 'Hello, World!\n'

# r会使\转义失效
print(r"Hello, World!\n")

print(str)

# """为多行段落
print("""这是一个段落，
可以由多行组成\n""")