from ultralytics import YOLO

class YoloDetector:
  def __init__(self, model_path, confidence):
    self.model = YOLO(model_path)
    # YENİ MODELİN İHA İÇİN KULLANDIĞI SINIF ADINI BURAYA YAZIN
    # Örnek: Modeliniz İHA'ları "drone" olarak etiketliyorsa:
    self.classList = ["uav"]
    # VEYA Modeliniz birden fazla türü farklı etiketliyorsa:
    # self.classList = ["drone", "uav", "quadcopter"]
    # !! Kendi modelinize göre doğru sınıf adını/adlarını yazdığınızdan emin olun !!
    self.confidence = confidence

  def detect(self, image):
    results = self.model.predict(image, conf=self.confidence)
    result = results[0]
    detections = self.make_detections(result)
    return detections

  def make_detections(self, result):
    boxes = result.boxes
    detections = []
    for box in boxes:
      x1, y1, x2, y2 = box.xyxy[0]
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
      w, h = x2 - x1, y2 - y1
      class_number = int(box.cls[0])

      # Sadece belirlenen sınıfları işleme al
      if result.names[class_number] not in self.classList:
        continue

      conf = float(box.conf[0]) # Tipi float olarak alalım
      # DeepSORT'un beklediği format: (bbox_xywh, class_id, confidence)
      # class_id yerine doğrudan sınıf adını veya sabit bir değer de verebilirsiniz,
      # ancak DeepSORT genellikle class bilgisini doğrudan kullanmaz.
      # Önemli olan bbox ve confidence.
      detections.append((([x1, y1, w, h]), conf, result.names[class_number])) # DeepSORT girdisini güncelledik (class ismi eklendi, conf float yapıldı)

    return detections