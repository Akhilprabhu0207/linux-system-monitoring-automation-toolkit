import argparse,json
from .monitor import snapshot,apply_thresholds
from .logparser import parse
def main():
 p=argparse.ArgumentParser(); s=p.add_subparsers(dest='command',required=True); s.add_parser('monitor').add_argument('--json',action='store_true'); s.add_parser('logs').add_argument('file'); a=p.parse_args()
 if a.command=='monitor': print(json.dumps(apply_thresholds(snapshot())))
 else:
  with open(a.file,encoding='utf-8',errors='replace') as f: print(json.dumps(parse(f)))
if __name__=='__main__':main()
