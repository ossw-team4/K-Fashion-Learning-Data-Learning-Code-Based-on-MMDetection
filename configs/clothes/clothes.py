import random

_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))
        
train_pipeline = [  
    dict(type='LoadImageFromFile'),
    dict(
        type='LoadAnnotations',
        with_bbox=True,
        with_mask=True,
        poly2mask=False),
    dict(
        type='Resize',
        img_scale=(1333, 800),
        keep_ratio=True
    ), 
    dict(
        type='RandomFlip', 
        flip_ratio=0.5), 
    dict(
        type='Normalize', 
        mean=[123.675, 116.28, 103.53], 
        std=[58.395, 57.12, 57.375], 
        to_rgb=True),
    dict(
        type='Pad', 
        size_divisor=32),
    dict(type='DefaultFormatBundle'), 
    dict(
        type='Collect', 
        keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks'])
]

dataset_type = 'CocoDataset'
dataset_root = 'data/clothes/'
datasets_meta = [
    ['task_3-1_01outer_01coat_01-2022_08_18_06_22_27-coco 1.0', ('coat',)], 
    ['task_3-1_01outer_01coat_02-2022_08_18_21_13_43-coco 1.0', ('coat',)],
    ['task_3-1_01outer_02jacket_01-2022_08_19_07_11_56-coco 1.0', ('jacket',)],
    ['task_3-1_01outer_02jacket_02-2022_08_19_11_36_54-coco 1.0', ('jacket',)],
    ['task_3-1_01outer_03jumper_01-2022_08_29_12_07_33-coco 1.0', ('jumper',)],
    ['task_3-1_01outer_03jumper_02-2022_08_19_17_24_18-coco 1.0', ('jumper',)],
    ['task_3-1_01outer_04cardigan_01-2022_08_18_12_07_25-coco 1.0', ('cardigan',)],
    ['task_3-1_01outer_04cardigan_02-2022_08_20_10_05_43-coco 1.0', ('cardigan',)],
    ['task_3-1_02top_01blouse_01-2022_08_30_04_44_09-coco 1.0', ('blouse',)],
    ['task_3-1_02top_01blouse_02-2022_08_18_14_45_48-coco 1.0', ('blouse',)],
    ['task_3-1_02top_02t-shirt_01-2022_08_23_10_16_11-coco 1.0', ('t-shirt',)],
    ['task_3-1_02top_02t-shirt_02-2022_08_25_02_39_27-coco 1.0', ('t-shirt',)],
    ['task_3-1_02top_03sweater_01-2022_08_20_22_34_27-coco 1.0', ('sweater',)],
    ['task_3-1_02top_03sweater_02-2022_08_24_04_00_42-coco 1.0', ('sweater',)],
    ['task_3-1_02top_04shirt_01-2022_08_23_05_52_15-coco 1.0', ('shirt',)],
    ['task_3-1_02top_04shirt_02-2022_08_23_09_54_21-coco 1.0', ('shirt',)],
    ['task_3-1_03-1onepiece(dress)_01-2022_08_23_01_00_12-coco 1.0', ('onepiece(dress)',)],
    ['task_3-1_03-1onepiece(dress)_02-2022_08_21_20_27_04-coco 1.0', ('onepiece(dress)',)],
    ['task_3-1_03-2onepiece(jumpsuite)_01-2022_08_26_03_35_03-coco 1.0', ('jumpsuite',)],
    ['task_3-1_04bottom_01pants_01-2022_08_22_23_43_09-coco 1.0', ('pants',)],
    ['task_3-1_04bottom_01pants_02-2022_08_26_03_20_52-coco 1.0', ('pants',)],
    ['task_3-1_04bottom_02skirt_01-2022_08_23_00_22_56-coco 1.0', ('skirt',)],
    ['task_3-1_04bottom_02skirt_02-2022_08_28_08_22_14-coco 1.0', ('skirt',)],
    ['task_onepiece(dress)_1-2022_08_30_05_16_12-coco 1.0', ('onepiece(dress)',)],
    ['task_onepiece(dress)_2-2022_08_27_10_50_59-coco 1.0', ('onepiece(dress)',)],
]

train_datasets = []

for dataset in datasets_meta:
    img_prefix = dataset_root + dataset[0] + '/images'
    ann_file = dataset_root + dataset[0] + '/annotations/instances_default.json'
    classes = dataset[1]

    train_datasets.append(dict(
    type=dataset_type,
    pipeline=train_pipeline,
    img_prefix=img_prefix,
    classes=classes,
    ann_file=ann_file))

data = dict(
    train=train_datasets,
    val=train_datasets,
    test=train_datasets)

load_from = ''
