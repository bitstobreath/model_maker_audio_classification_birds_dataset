import random
import sys
from time import sleep
from build_data import bird_code_to_name
import os
import glob
import logging
import shutil
import magic
from pydub import AudioSegment

logging.basicConfig(filename='run.log', encoding='UTF-8', level=logging.DEBUG)

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
for i, k in enumerate(bird_code_to_name):
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
    for j, (n, s) in enumerate(zip(names, sources)):
        if random.randrange(0, 1) == 0: # process approximate 1 in 1 files
            n_loc = os.path.abspath(os.path.join(root, tst, k, n))
            s_loc = os.path.abspath(s)
            datt = magic.from_file(s_loc)
            logging.info(s_loc + " - " + datt)
            if random.randrange(0, 4) == 0:
                n_loc = n_loc.replace('/test/', '/train/')
            os.makedirs(os.path.dirname(n_loc), exist_ok=True)
            logging.info(s_loc + " copying to " + n_loc)
            try:
                sound = None
                if "ID3" in datt:
                    sound = AudioSegment.from_mp3(s_loc)
                elif "RIFF" not in datt:
                    sound = AudioSegment.from_wav(s_loc)
                else:
                    raise Exception("WARNING: " + s_loc + " " + datt)
                sound.set_channels(1)
                sound = sound.set_frame_rate(16000)                
                sound = sound.set_channels(1)  
                sound.export(n_loc, format="wav")
                datt = magic.from_file(n_loc)
                logging.info(n_loc + " - " + datt)
                logging.info(s_loc + " copied to " + n_loc)
            except Exception as e:
                logging.error(s_loc + " NOT copied to " + n_loc, exc_info=e)
            sys.stdout.write('\r')
            # the exact output you're looking for
            n_len = len(names) * len(bird_code_to_name)
            i_iter = j + len(names) * i;
            sys.stdout.write("{:.2%}".format(i_iter/n_len))
            sys.stdout.flush()