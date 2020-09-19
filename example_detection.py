import darknet
import cv2
import numpy as np

def retbox(detections,i) :
	label = detections[i][0].decode('utf-8')
	score = detections[i][1]
	# classes = labels_arr.index(label)

	x1 = int(round((detections[i][2][0]) - (detections[i][2][2]/2.0))) # top left x1 
	y1 = int(round((detections[i][2][1]) - (detections[i][2][3]/2.0))) # top left xy 
	x2 = int(round((detections[i][2][0]) + (detections[i][2][2]/2.0))) # bottom right x2 
	y2 = int(round((detections[i][2][1]) + (detections[i][2][3]/2.0))) # bottom right y2 
                
	box = np.array([x1,y1,x2,y2])

	return label, score, box

if __name__ == "__main__" :
	COLORS = []
	class_num = 80 #coco classes
	for i in range(class_num) :
		COLORS.append((np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)))

	net = darknet.load_net(bytes('yolov4.cfg',encoding='utf-8'), 
						   bytes('yolov4.weights',encoding='utf-8'),0)

	meta = darknet.load_meta(bytes('coco.data',encoding='utf-8'))

	cap = cv2.VideoCapture('classroom.mp4') #input videofile or 0(webcam)
	# cap.set(3,1920)	#using webcam option
	# cap.set(4,1280)
	# cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
	threshold = 0.9

	while True:
		ret, frame = cap.read()
		rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		detections = darknet.detect_image(net,meta, rgb_frame , thresh=.15)
	    
		for i in range(len(detections)) :
			label , score , box = retbox(detections,i)
			left,top,right,bottom=box
			#-----Draw Bounding box-----
			cv2.putText(frame, label, (left,top), cv2.FONT_HERSHEY_SIMPLEX, 2, COLORS[i], 3)
			cv2.rectangle(frame, (left,top), (right,bottom), COLORS[i], 3)
			#---------------------------
		cv2.imshow('frame',frame)
		k = cv2.waitKey(1)
		if k == 27 :
			break

	cv2.destroyAllWindows()
	cap.release()