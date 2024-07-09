import os
import shutil

def clear_pycache(root_dir='.'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == '__pycache__':
                pycache_path = os.path.join(dirpath, dirname)
                print(f'Removendo {pycache_path}')
                shutil.rmtree(pycache_path)

if __name__ == "__main__":
    clear_pycache()
