# Int
year = 2018
year = int('2018')

# Float
pi = 3.14159265
pi = float('3.14159265')
inf = float('inf')
minus_inf = float('-inf')

# Fixed point
from decimal import Decimal
price = Decimal('0.02')


text = "This is the way the world ends"

text = 'This is the way the world ends'

text = """This is the wat \n
the world ends"""

text = '''This is the wat \n
the world ends'''


initialize_me = None


items = []

items = [1, 2, 3]

items.append('four')

items.extend([5, 6, 7])


thing = {}

thing['name'] = 'James'

thing[(1, 2)] = 'position'


thing = False

thing = bool('any object')  # True

all_false = False or 0 or '' or [] or {} or None

all_true = True or 1 or 'hello!' or [1, 2, 3] or {'name': 'James'} or None






a = 10     # 10
a += 1     # 11
a -= 1     # 10

b = a + 1  # 11
c = a - 1  # 9

d = a * 2  # 20
e = a / 2  # 5
f = a % 3  # 1
g = a ** 2 # 100

