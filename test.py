import re

files = [ '/a/b/c/la_seg_x005_y003.png',
          '/a/b/c/la_seg_x005_y003.npy',
          '/a/b/c/la_seg_x004_y003.png',
          '/a/b/c/la_seg_x004_y003.npy',
          '/a/b/c/la_seg_x003_y003.png',
          '/a/b/c/la_seg_x003_y003.npy', ]

regex = re.compile(r'_x\d+_y\d+\.npy')

selected_files = filter(regex.search, files)
print(selected_files)