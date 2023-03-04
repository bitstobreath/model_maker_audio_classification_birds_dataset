# model_maker_audio_classification_birds_dataset
Bird Maker Audio Classification Birds Dataset Patch

# Why?
* One of my classes requested I use Google colab to experiment with audio machine learning

# Build Environment
* Linux Debian Based or Ubuntu on WSL

# Libraries
```bash
sudo apt install libportaudio ffmpeg -y
```

# Updates/Upgrades
```bash
pip install --upgrade pip
```

# Problem Solver
* Try installing pyenv for different version of Python if getting dependency conflicts with Python
* Try using miniforge conda environment if you cannot run the colab .ipynb file.

# Note on Speed
* you can reduce the number of files downloaded by changing line ~#183 to ~#186 in xenocanto_modified.py
```python
# get 1 out of 1 tracks in url_list[1]
# change the (0,1) to (0, n) for 1 in 10 or 1 in 4 urls approximately
# random is used to hopefully avoid sampling order biases i.e. getting the first 100 sounds or every 2nd sound
url_list[1] = [url for i, url in enumerate(url_list[1]) if random.randrange(0,1) == 0]
```
* you can reduce the number of files copied by changing line ~#46 in prepare_data.py
* bash or shell scripts/commands would likely be faster, especially for the zip/unzip commands
* or on windows, context tools like winrar/7zip or builtin unzip tools

# Initial Ideas

* [Modified Library](https://github.com/ntivirikin/xeno-canto-py)
* Library contains wav files that are not RIFF, and not 1600hz mono audio files.
* main.py will download(build_data.py), process(prepare_data.py), store_results(my_zip)

# Recommended Changes

* [Better Library](https://github.com/realzza/xenopy)