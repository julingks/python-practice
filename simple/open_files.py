import glob

python_files = glob.glob('*.py')
print python_files
for file_name in sorted(python_files):
    print '---------' + file_name
    with open(file_name) as f:
        for line in f:
            print line.rstrip()
    print
