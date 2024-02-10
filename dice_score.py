import nibabel as nib
import os
import numpy as np


def test_nifti_dice_score(seg_path, seg_file, truth_path, truth_file):
    seg_file_path = os.path.join(seg_path, seg_file)
    truth_file_path = os.path.join(truth_path, truth_file)
    seg_nib = nib.load(seg_file_path)
    seg_data = np.array(seg_nib.dataobj)
    truth_nib = nib.load(truth_file_path)
    truth_data = np.array(truth_nib.dataobj)
    dice_score = calculate_nifti_dice_score(seg_data, truth_data)
    print(f'{seg_file} vs {truth_file}: {dice_score}')
    return dice_score


def calculate_nifti_dice_score(segmentation, truth):
    area_sum = np.sum(segmentation) + np.sum(truth)
    if area_sum > 0:
        return (np.sum(segmentation[truth > 0]) * 2.0) / area_sum
    else:
        return 0


def compare_directories(seg_path, truth_path):
    seg_files = os.listdir(seg_path)
    seg_files.sort()
    truth_files = os.listdir(truth_path)
    truth_files.sort()

    with open('./dice_scores.csv', 'w') as f:
        f.write('Medpseg Predict, Ground Truth, Dice Score\n')

        for seg_file, truth_file in zip(seg_files, truth_files):
            dice_score = test_nifti_dice_score(seg_path, seg_file, truth_path, truth_file)

            f.write(f'{seg_file}, {truth_file}, {dice_score}\n')


if __name__ == '__main__':
    compare_directories(
        seg_path='seg/',
        truth_path='truth/',
    )
