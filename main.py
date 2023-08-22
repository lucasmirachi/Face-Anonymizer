import cv2
import mediapipe as mp
import os

def process_img(img, face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bounding_box = location_data.relative_bouding_box 

            x1, y1, w, h = bounding_box.xmin, bounding_box.ymin, bounding_box.width, bounding_box.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # To draw a green rectangle around the detected face
            cv2.rectangle(img, (x1, y1), (x1 + 2, y1 + h), (0, 255, 0), 10)

            # STEP 3: blur faces
            # To blur the detected face region
            img[y1:y1 + hm x1:x1 + w, :] = cv2.blur(img[y1:y1 + hm x1:x1 + w, :], (50, 50))
    
    return img




# STEP 1: read image

# STEP 2: detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence = 0.5) as face_detection:
   img = process_img(img, face_detection)


# STEP 4: save image