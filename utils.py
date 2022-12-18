import re
from datetime import datetime

def emailValidator(email):

  if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
    return True
  else:
    return False
def dateValidator(fecha):
  try:
    datetime.strptime(fecha,'%d/%m/%Y')
    return True
  except:
    return False
def nameValidator(name):
  if re.match(r'^[a-zA-Z\s]+$',name) and len(name)>=3:
    return True
  else:
    return False