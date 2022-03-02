import sys,os,regex
if len(sys.argv) !=3:
  raise ValueError('Please inter your number')
fname = sys.argv[1]
if not os.path.isfile(fname):
    raise ValueError('file does not exist')

with open(fname) as f:
  contacts  = f.readlines()
clist = []
for str in contacts:
  cstr = regex.re_email(str)
  if 'email' in clist:
    clist.append(cstr,'\n')
  
with open(sys.argv[2],'w') as f:
  f.writelines(clist)