import os
import shutil
root = 'small_birds_dataset'

shutil.make_archive('birds_dataset', 'zip', os.path.join('.', root))