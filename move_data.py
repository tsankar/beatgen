import os
import shutil

ROOT = '/media/tharun/OS/Program Files (x86)/Image-Line/FL Studio 12/Data/Patches/Packs (Old)'
DATA = 'data/'

for folder in os.listdir(ROOT):
    if folder.startswith('Vengeance'):
        for pack in os.listdir(os.path.join(ROOT, folder)):
            dest = ''
            # Kicks were moved manually due to inconsistent directory structures
            # if pack.find('Bassdrums') != -1 or pack.find('Kicks') != -1:
            #     dest = 'Kicks'
            if pack.find('Claps') != -1 and folder != 'Vengeance Electroshock Vol.2':
                dest = 'Claps'
            elif pack.find('Snares') != -1 and folder != 'Vengeance Electroshock Vol.2':
                dest = 'Snares'
            elif pack.find('Cymbals') != -1:
                for cym in os.listdir(os.path.join(ROOT, folder, pack)):
                    if cym.find('Closed Hihat') != -1:
                        dest = 'Closed_hats'
                    elif cym.find('Open Hihat') != -1:
                        dest = 'Open_hats'
                    if dest:
                        for wav in os.listdir(os.path.join(ROOT, folder, pack, cym)):
                            shutil.copy2(os.path.join(ROOT, folder, pack, cym, wav), os.path.join(DATA, dest))

                continue

            if dest:
                for wav in os.listdir(os.path.join(ROOT, folder, pack)):
                    shutil.copy2(os.path.join(ROOT, folder, pack, wav), os.path.join(DATA, dest))
