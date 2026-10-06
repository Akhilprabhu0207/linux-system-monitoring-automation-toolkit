from sysmon_tool.monitor import apply_thresholds
def test_alert_when_cpu_high(): assert apply_thresholds({'cpu_percent':95,'memory_percent':10,'disk_percent':10})['status']=='ALERT'
def test_ok_when_below_thresholds(): assert apply_thresholds({'cpu_percent':10,'memory_percent':10,'disk_percent':10})['status']=='OK'
