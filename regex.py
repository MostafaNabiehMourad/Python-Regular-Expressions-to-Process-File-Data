import re 
def re_email():
  regex = r'email:[a-z0-9]._\`+\
  @[a-z0-9]+.{3}[a-z]$'
  pm = re.compile(r'email')
  m = pm.math(str)
  if m:
    result = p.subn('email:'+m.group(),m.group)
    return result[0]
  else:
    return 'invalid email '
  return m.group()