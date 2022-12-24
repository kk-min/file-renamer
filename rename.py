from pathlib import Path
import sys

argv = sys.argv
argc = len(argv)

if(argc < 3 or argc > 4):
    print("----------")
    print("Usage:\npython rename.py [path_to_dir] [string_to_replace] [replacement_string]")
    print("- Leave replacement_string blank to remove [string_to_replace]")
    print("- For directories or strings with white space, use quotes")
    print("----------")
    quit()

# Directory: 
dir = Path(argv[1])

if(not dir.is_dir()):
    print("Path is not a directory")
    quit()

if(argc == 3):
    # Remove string
    replacement = ""
else:
    # Replace string
    replacement = argv[3]

print("----------")
print('Files renamed in '+str(dir)+':\n')
for filepath in dir.glob('*'+argv[2]+'*'):
    old_name = filepath.name
    renamed_filepath = str(filepath).replace(argv[2], replacement)
    filepath.rename(renamed_filepath)
    new_name = Path(renamed_filepath).name
    print(old_name+' -> '+new_name+'\n')
print("----------")
