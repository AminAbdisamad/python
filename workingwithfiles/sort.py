import os
# Change directory
os.chdir('/Users/apple/Downloads/Sawiro')
for f in os.listdir():
    fn, fe = os.path.splitext(f)
