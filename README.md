# K-Fashion-MMDetection

본 프로젝트는 경기대학교 2022-2 오픈소스SW실습 수업의 최종 과제로써 MMDetection의 Mask RCNN을 이용하여 학습을 수행합니다.

## How To

1. 프로젝트를 복제한다.

   ```shell
   git clone https://github.com/ossw-team4/K-Fashion-MMDetection.git
   cd K-Fashion-MMDetection
   ```

1. Anaconda 설치 후 최상위 디렉토리의 `openmmlab.yaml`을 import 한다.

   ```shell
   conda env create -f openmmlab.yaml
   conda activate openmmlab
   ```

   > 가상환경 Import 중 `Encountered error while trying to install package. mmdv-full` 오류가 발생한다면?
   >
   > `conda activate openmmlab`으로 가상환경을 활성화 시킨 후 아래의 두 명령어를 실행한다.
   >
   > `pip install -U openmim`
   >
   > `mim install mmcv-full`

1. 환경 구성이 정상적으로 되었는지 확인한다.

   ```shell
   mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .

   python demo/image_demo.py demo/demo.jpg yolov3_mobilenetv2_320_300e_coco.py yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth --device cpu --out-file result.jpg
   ```

   환경 구성에 성공했다면 `result.jpg`가 명령어를 실행한 경로에 생성된다.

1. 제공된 Dataset을 `K-Fashion-MMDetection/data/clothes`에 위치시킨다.

1. `K-Fashion-MMDetection/scripts`의 `unzip.py`를 실행한다.

   ```shell
   python scripts/unzip.py
   ```

   `K-Fashion-MMDetection/data/clothes`에서 압축해제된 폴더들을 확인한다.

1. `K-Fashion-MMDetection/scripts`의 `modify_annotations.py`를 실행하여 annotation의 오류를 수정한다.

   ```shell
   python modify_annotations.py
   ```

1. 학습을 시작한다.

   ```shell
   python tools/train.py configs/clothes/clothes.py
   ```
