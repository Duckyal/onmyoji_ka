import os


# 获取当前文件夹中的所有文件和文件夹名
files_and_dirs = os.listdir('.')

# 过滤出只有文件的列表
py_files = [f for f in files_and_dirs if f.endswith('.py')]

# 尝试移除特定的文件
for filename in ['start.py', '模板.py', '答题.py']:
    try:
        py_files.remove(filename)
    except ValueError:
        pass

output = ''
for i in range(len(py_files)):
    if (i+1)%3 == 0:
        txt = '{0}.{1}\n'.format(i+1, py_files[i])
        output += txt
    else:
        txt = '{0}.{1}\t'.format(i+1, py_files[i])
        output += txt

while True:
    print(output)
    try:
        seq = int(input('0.退出\t选择:'))-1
        if seq == -1:
            break
        else:
            print(f'正在初始化<{py_files[seq]}>中……')
            os.system(f'python3 {py_files[seq]}')
    except:
        print('序号输入错误\f')
        