import re
LEVELS=('CRITICAL','ERROR','WARNING','WARN','INFO','DEBUG')
def parse(lines):
 counts={x:0 for x in LEVELS}; matches=[]
 for line in lines:
  m=re.search(r'\b(CRITICAL|ERROR|WARNING|WARN|INFO|DEBUG)\b',line.upper())
  if m: counts[m.group(1)]+=1; matches.append({'level':m.group(1),'message':line.strip()})
 return {'counts':counts,'matches':matches}
