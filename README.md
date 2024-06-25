# transcription-experimentation

downloads song as youtube_id.wav
runs spleeter and downloads separated audio as output/youtube_id/vocals.wav output/youtube_id/accomp....wav and  or demucs for source separation (uncomment the one you want)

runs basic-pitch on top
# installation 
create a virtual environemnt if it doens't already exist. 

```
source "venv_name"/bin/activate
pip install -r requiremetn.txt
```

# running
```
python3 dl_sep_run.py "youtube_link"
```
