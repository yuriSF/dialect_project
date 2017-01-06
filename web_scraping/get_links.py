import os

dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
print dirs

cwd = os.getcwd()

for dir in dirs:
    dir = cwd + '/' + dir
    os.chdir(dir)
    print dir
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            with open(name, 'r') as f:
                data = f.readlines()
                for line in data:
                    if '/resources/doc' in line:
                        print line
                
