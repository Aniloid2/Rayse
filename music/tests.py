from django.test import TestCase

# Create your tests here.

import re

string = 'Brian Formento'

a = re.split(' ', string )

print a[0], a[1]