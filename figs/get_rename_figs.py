import os
import re
import subprocess as sp
import shutil


SERVER = 'mmuetz@login.archer.ac.uk'
LOC = '/nerc/n02/n02/mmuetz/um10.9_runs/archive/u-au197/share/data/history/P1M/figs/./'

FILENAMES = [
    'atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-0_evr-0.5278288722038269.png', 
    'atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-1_evr-0.1835406869649887.png', 
    'atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-2_evr-0.1671045869588852.png', 
    'atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-3_evr-0.04120809957385063.png', 
]


def get_all():
    filenames = [os.path.join(LOC, fn) for fn in FILENAMES]

    cmd_filenames = ' :'.join(filenames)
    cmd = f'rsync -Rza {SERVER}:{cmd_filenames} raw/'
    sp.call(cmd, shell=True)


def rename_all():
    for fn in FILENAMES:
        new_fn = re.sub('atmos.None.shear_profile_classification_analysis.', '', fn)
        new_fn = re.sub('_evr.*\.png', '', new_fn) + '.png'
        shutil.copyfile(os.path.join('raw', fn), new_fn)


def main():
    if not os.path.exists('raw'):
        os.makedirs('raw')

    get_all()
    rename_all()


if __name__ == '__main__':
    main()
