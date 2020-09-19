# yolo-example
yolo example for tistory

alexyab 사이트에서 확인해보았더니, `darknet.py`의 코드 내용이 좀 변경되었더군요
그전에 좀 더러웠던 코드를 정리한 느낌이라 별 차이는 없을거라 생각 되지만 제가 작성한 글을 그대로
사용하기 위해서는 전에 있던 `darknet.py`가 필요할거 같아서 같이 올려드립니다.
해당 코드는 yolov4의 pre-train가중치를 이용하여 coco data set이 훈련된 모델로 테스트 되었습니다.

## Required Pakages
+ Opencv
+ Numpy

## 확인 사항
+ `libdarknet.so` 파일은 반드시 본인의 컴퓨터에서 빌드한 파일을 사용하시길 바랍니다.    
(예시로 올려드리지만 제 컴퓨터에서 빌드된 파일이라 안될겁니다.)
+ `exmaple_detection.py` 파일은 블로그에서 피자인식하는 알고리즘을 뺀 예제 파일입니다.    
(classroom 동영상으로 테스트하여 잘 작동됩니다.)
+ pre-train가중치를 다운받아서 한번 테스트 해보시는 것을 추천드립니다.    
[yolov4.weight](https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view), [yolov4-tiny.weight](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights)
+ `cuda : out of memory` 같은 오류가 발생할 경우 cfg파일의 batch size나 input network size를 줄여보시기 바랍니다.
