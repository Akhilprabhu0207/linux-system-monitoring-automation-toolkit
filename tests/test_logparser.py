from sysmon_tool.logparser import parse
def test_log_levels():
 r=parse(['INFO started','ERROR failed','WARNING slow']); assert r['counts']['ERROR']==1; assert r['counts']['WARNING']==1
