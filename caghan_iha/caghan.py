import cv2
from ultralytics import YOLO
import numpy as np
import time
def main():
  model = YOLO("caghan_model.pt")

  #cap = cv2.VideoCapture(0)
  cap = cv2.VideoCapture("test/dronefight.mp4")

  if not cap.isOpened():
      print(f"Hata: Video dosyası açılamadı")
      exit()

  prev_time = 0

  print("Video açılıyor...")

  while True:
      ret, frame = cap.read()

      if not ret:
          print("Video sonlandı veya kare okunamadı.")
          break

      current_time = time.time()
      if (current_time - prev_time) > 0:
          fps = 1 / (current_time - prev_time)
      else:
          fps = 0
      prev_time = current_time
      results = model(frame, verbose=False) 

      annotated_frame = results[0].plot()
      
      yukseklik, genislik = int(annotated_frame.shape[0]), int(annotated_frame.shape[1])
      center_x = int(genislik / 2)
      center_y = int(yukseklik / 2)
      rect_height = int(yukseklik * 0.8)  
      rect_width = int(genislik * 0.5)
      top_left_x = center_x - int(rect_width / 2)  
      top_left_y = center_y - int(rect_height / 2) 
      bottom_right_x = center_x + int(rect_width / 2)  
      bottom_right_y = center_y + int(rect_height / 2) 
      boxes = results[0].boxes.xyxy.cpu().numpy() 
      if len(boxes) > 0:  # 
          centers = (boxes[:, [0, 1]] + boxes[:, [2, 3]]) / 2  
          centers = centers.astype(int) 

          widths = boxes[:, 2] - boxes[:, 0] 
          heights = boxes[:, 3] - boxes[:, 1]  
          radii = (np.minimum(widths, heights) * 0.2).astype(int)  

          for center, radius in zip(centers, radii):
              cv2.line(annotated_frame,(center_x,center_y),(center[0],center[1]),(0,255,0),5)
              cv2.circle(annotated_frame, (center[0], center[1]), 5, (255, 0, 0), cv2.FILLED)    
      cv2.circle(annotated_frame, (center_x, center_y), 5, (0, 0, 255), cv2.FILLED)
      cv2.rectangle(annotated_frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
      
      cv2.putText(annotated_frame, "Av : Hedef Vurus Alani", (top_left_x + 10, bottom_right_y - 10), 
                  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
      
      cv2.putText(annotated_frame, "Ak : Kamera Gorus Alani", (20, yukseklik - 20), 
                  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
      cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (genislik - 200, yukseklik - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

      cv2.imshow("CAGHAN 2025", annotated_frame)

      if cv2.waitKey(25) & 0xFF == ord('q'):
          print("'q' tuşuna basıldı, çıkılıyor...")
          break

  print("Video bitti...")
  cap.release()

  cv2.destroyAllWindows()

  print("Yazılım kapanıyor...")


if  __name__ == "__main__":
    main()


""" import cv2
import time
from yolo_detector import YoloDetector
from tracker import Tracker

MODEL_PATH = "caghan_model.pt"
VIDEO_PATH = "test/twodrone.mp4"


def main():
  detector = YoloDetector(model_path=MODEL_PATH, confidence=0.2)
  tracker = Tracker()

  cap = cv2.VideoCapture(VIDEO_PATH)

  if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

  while True:
    ret, frame = cap.read()
    if not ret:
      break

    start_time = time.perf_counter()
    detections = detector.detect(frame)
    tracking_ids, boxes = tracker.track(detections, frame)

    for tracking_id, bounding_box in zip(tracking_ids, boxes):
      cv2.rectangle(frame, (int(bounding_box[0]), int(bounding_box[1])), (int(
          bounding_box[2]), int(bounding_box[3])), (0, 0, 255), 2)
      cv2.putText(frame, f"{str(tracking_id)}", (int(bounding_box[0]), int(
          bounding_box[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    end_time = time.perf_counter()
    fps = 1 / (end_time - start_time)
    print(f"Current fps: {fps}")

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
      break

  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
  main() """


