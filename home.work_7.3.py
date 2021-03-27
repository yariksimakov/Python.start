import os
from shutil import copytree
print(os.path)
print(*os.walk('new_project'))
for el in os.walk('new_project'):
    print(el)

def copy_project():
    start_dir = 'new_project'
    finish_dir = 'templates'
    # for root, dirs, file in os.walk(start_dir):
    #     print(root, dirs, file)
    #     copytree(os.path.join(root), finish_dir)


if __name__ == '__main__':
    copy_project()
