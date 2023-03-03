import random
from build_data import bird_code_to_name
import os
import glob
import shutil

dset = 'dataset'
audio = 'audio'
root = 'small_birds_dataset'
tst = 'test'

def stradd(a, b):
    return os.path.join(a, b)

def mkd(str):
    if not os.path.exists(str):
        os.mkdir(str)
if os.path.exists(root):
    shutil.rmtree(root)
for k in bird_code_to_name:
    v = bird_code_to_name[k]
    "test/*/*.wav"
    os.chdir(dset)
    os.chdir(audio)
    os.chdir(v.replace(' ',''))
    names = glob.glob("*.wav")
    sources = [stradd(os.path.join(dset, audio, v.replace(' ', '')), s) for s in names]
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    mkd(root)
    os.chdir(root)
    mkd(tst)
    os.chdir(tst)
    mkd(k)
    os.chdir('..')
    os.chdir('..')
    for (n, s) in zip(names, sources):
        if random.randrange(0, 15) == 0: # copy approximate 1 in 15 files
            print(s + " copied to " + os.path.join(root, tst, k, n))
            shutil.copy(s, os.path.join(root, tst, k, n))