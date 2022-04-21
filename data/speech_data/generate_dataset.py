#
import os
import shutil
import csv
from pathlib import Path
root_path = '/research/everything2text-speech_encoder_only/LibriSpeech'

dest_root_path = '/research/everything2text-speech_encoder_only/data/speech/'

header = ['audio_id','speaker_id','text']
# transcription = {}
csv_file = open(dest_root_path+'/dataset/audio_test.csv','w')
writer = csv.writer(csv_file)
writer.writerow(header)
for root, dir, files in os.walk(root_path):
    # print(root, dir, files)
    # break
    for name in files:
        if name.endswith((".flac")):
            # print('Audio: ')
            # print(root+'/'+name)
            # shutil.copyfile(root+'/'+name, dest_root_path+'/audio/'+name)
            pass
            # break
        elif name.endswith((".trans.txt")):
            f = open(root+'/'+name,'r').readlines()
            for line in f:
                split = line.split(' ')
                id = split[0]
                speaker_id = id.split('-')[0]
                # ADD FOOLSTOP AT END
                # text = ' '.join(split[1:-1]+[split[-1].replace('\n',' .')])

                # REPLACE \n AT END OF THE TXT FILE BY EMPTY CHAR
                text = ' '.join(split[1:-1]+[split[-1].replace('\n','')])

                writer.writerow([id,speaker_id, text])
            # pass


# csv_f = open(dest_root_path+'/dataset/audio_test.csv','r')
# reader = csv.reader(csv_f)
# for row in reader:
#     print(row)
