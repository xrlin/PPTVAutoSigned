import os, sys

# 获取当前python解释器的路径
execute_path = sys.executable
cwd = os.getcwd()
script_file = os.path.join(cwd, 'pptv.py')

# 设置每天下午9点执行脚本
template = '(crontab -l 2>/dev/null; echo "0 21 * * * {execute_path} {script_file}") | crontab -'

os.system(template.format(execute_path=execute_path, script_file=script_file))