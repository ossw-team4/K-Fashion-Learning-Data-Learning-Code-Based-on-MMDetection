# K-Fashion 데이터 학습 및 환경 구축

> 경기대학교 2022-2 오픈소스SW실습 4조 최종 과제

## 발표 자료와의 차이점

본 프로젝트의 결과는 발표 자료의 내용과는 매우 상이합니다. 가장 큰 차이점은 `실습 환경`과 `Dataset 처리 방법`입니다.

1. 변경된 실습 환경에 대해

   > 발표 자료에서의 실습 환경은 Anaconda3 가상 환경과 CPU-based Train을 진행했습니다. 그러나 최종 결과물은 Docker를 이용한 GPU-based Train을 기준으로 개발되었습니다.

2. 변경된 Dataset 처리 방법에 대해

   > 발표 자료에서는 Dataset의 종류별로 구분되어 있는 25개의 Annotation을 구성 파일에서 엮어주는 방식으로 학습을 진행했습니다.
   >
   > 하지만 최종 결과물에서는 [Merge_COCO_FILES](https://github.com/mohamadmansourX/Merge_COCO_FILES)를 이용하여 25개의 Annotation을 하나로 병합하였습니다. 그리고 해당 Annotation을 Train Dataset(`train.json`)과 Validation Dataset(`val.json`)으로 나누어 이용하였습니다.

## Dataset 처리

제공된 Dataset을 다음과 같은 구조로 정리했습니다.

```plain
clothes/
├─ images/
├─ train.json
├─ val.json
```

제공된 Dataset의 모든 이미지는 `clothes/images`에 위치합니다.

각 Dataset에 들어있던 `instances_default.json`을 [Merge_COCO_FILES](https://github.com/mohamadmansourX/Merge_COCO_FILES)를 이용하여 하나의 Annotation으로 병합하고, [cocosplit](https://github.com/akarazniewicz/cocosplit)을 이용하여 `train.json`과 `val.json`으로 나누었습니다. 그 결과 Train 집합과 Validation 집합은 8(4760):2(1191)의 비율로 나어졌습니다.

`train.json`과 `val.json`의 `categories`는 다음의 표와 같이 설정하였습니다.

| id  | name            |
| --- | --------------- |
| 0   | coat            |
| 1   | jacket          |
| 2   | jumper          |
| 3   | cardigan        |
| 4   | blouse          |
| 5   | t-shirt         |
| 6   | sweater         |
| 7   | shirt           |
| 8   | onepiece(dress) |
| 9   | jumpsuite       |
| 10  | pants           |
| 11  | skirt           |

## Pre-conditions

- Windows(WSL2)의 경우

  1. [NVIDIA 드라이버](https://www.nvidia.co.kr/Download/index.aspx?lang=kr)가 필요합니다.
  2. [WSL2용 CUDA ToolKit](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)이 필요합니다.
  3. [Docker Desktop](https://www.docker.com/products/docker-desktop/)이 필요합니다.

- Linux(focused on Ubuntu)의 경우
  1. Linux용 NVIDIA 독점 드라이버가 필요합니다.
  2. [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)가 필요합니다.

## Instruction

MMDetection을 이용한 K-Fashion 데이터의 Train 및 Validation 절차에 대해 설명합니다.

### Train

1. 프로젝트를 복제합니다.

   ```shell
   git clone https://github.com/ossw-team4/K-Fashion-MMDetection.git
   cd K-Fashion-MMDetection
   ```

2. Docker 이미지를 빌드 합니다.

   > 주의!
   >
   > 사용 중인 그래픽카드에 따라 Dockerfile의 수정이 필요할 수 있습니다. 본 프로젝트의 Dockerfile은 NVIDIA RTX 30 Series에서 작동하도록 설정되어 있습니다. 이외의 그래픽 카드는 다음 단계에 따라 Dockerfile의 환경 변수를 수정해야 할 수 있습니다.
   >
   > 1. [CUDA GPUs](https://developer.nvidia.com/cuda-gpus)를 참고하여 사용 중인 그래픽 카드의 Compute Capability를 확인하고 `TORCH_CUDA_ARCH_LIST` 환경 변수를 수정하세요.
   >
   > 2. [pytorch dockerHub](https://hub.docker.com/r/pytorch/pytorch/tags)를 참고하여 `PYTORCH`, `CUDA`, `CUDNN` 환경 변수를 수정하세요.
   >
   > 3. 변경한 `CUDNN`과 `PYTORCH` 변수에 맞춰 mmcv의 주소를 다음과 같이 변경하세요.
   >
   >    `https://download.openmmlab.com/mmcv/dist/cu{CUDNN VER}/torch{PYTORCH VER}/index.html`

   ```shell
   docker build -t mmdetection docker/
   ```

3. mmdetection 컨테이너를 시작합니다.

   ```shell
   docker run --gpus all --shm-size=8g --name kfashion -it mmdetection
   ```

4. Train을 시작합니다. 결과물은 컨테이너의 `/mmdetection/work_dirs`에 저장됩니다.

   ```shell
   python tools/train.py configs/clothes/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_clothes.py
   ```

### Validation

1. Validation을 시작합니다. Detection 결과는 `work_dirs/results/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_clothes`에 저장됩니다.

   ```shell
   python tools/test.py configs/clothes/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_clothes.py work_dirs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_clothes/latest.pth --eval bbox segm --show-dir work_dirs/results/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_clothes
   ```

2. **컨테이너 터미널은 그대로 둔 채로 Host에서 새 터미널 창을 열고** 다음 명령어를 입력하여 결과물을 Host의 `~/learning_results`로 복사합니다.

   ```shell
   docker cp kfashion:/mmdetection/work_dirs ~/learning_results
   ```

3. Host의 `~/learning_results`에서 로그, 가중치, Detection 결과 등을 확인합니다.

## Reference

- [Merge_COCO_FILES](https://github.com/mohamadmansourX/Merge_COCO_FILES)
- [cocosplit](https://github.com/akarazniewicz/cocosplit)
- [2: Train with customized datasets](https://github.com/open-mmlab/mmdetection/blob/master/docs/en/2_new_data_model.md)
