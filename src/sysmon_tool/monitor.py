import os,platform,subprocess
import psutil

def snapshot():
 d=psutil.disk_usage(os.path.abspath(os.sep)); return {'cpu_percent':psutil.cpu_percent(interval=0.2),'memory_percent':psutil.virtual_memory().percent,'disk_percent':d.percent,'platform':platform.system(),'status':'OK'}
def service_health(service):
 if platform.system()=='Windows':
  p=subprocess.run(['sc','query',service],capture_output=True,text=True); return p.returncode==0 and 'RUNNING' in p.stdout.upper()
 p=subprocess.run(['systemctl','is-active',service],capture_output=True,text=True); return p.returncode==0 and p.stdout.strip()=='active'
def apply_thresholds(data,cpu=90,memory=90,disk=90):
 issues=[]
 if data['cpu_percent']>cpu: issues.append('CPU_HIGH')
 if data['memory_percent']>memory: issues.append('MEMORY_HIGH')
 if data['disk_percent']>disk: issues.append('DISK_HIGH')
 return {**data,'status':'ALERT' if issues else 'OK','issues':issues}
