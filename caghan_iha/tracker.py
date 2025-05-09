from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
  def __init__(self):
    self.object_tracker = DeepSort(
        max_age=20,
        n_init=2,
        nms_max_overlap=0.3, # İHA'lar küçük ve yakın olabileceğinden bu değeri ayarlamak gerekebilir (örn: 0.5)
        max_cosine_distance=0.7, # Görünüm benzerliği eşiği, modelinize göre ayarlayın
        nn_budget=None,
        override_track_class=None,
        embedder="mobilenet", # Veya daha iyi bir embedder (örn: "osnet_x0_25")
        half=True,
        bgr=True,
        embedder_model_name=None,
        embedder_wts=None,
        polygon=False,
        today=None
    )

  def track(self, detections, frame):
    # DeepSORT'a gönderilecek formatı hazırlayalım
    # yolo_detector'dan gelen format: (([x1, y1, w, h]), conf, class_name)
    # DeepSORT beklenen format (genellikle): (bbox_xywh, confidence, class_id)
    # Şimdilik class_name'i göz ardı edip bbox ve conf gönderelim.
    # Gerekirse class_name'i bir ID'ye mapleyip gönderebilirsiniz.

    formatted_detections = []
    for detection in detections:
        bbox_xywh, conf, _ = detection # class_name'i şimdilik almıyoruz
        formatted_detections.append((bbox_xywh, conf)) # Sadece bbox ve confidence

    # Eğer DeepSORT sürümünüz class_id gerektiriyorsa:
    # formatted_detections = []
    # for detection in detections:
    #     bbox_xywh, conf, class_name = detection
    #     # class_name'e göre sabit bir class_id atayabiliriz (örn: 0)
    #     # Veya modelinizden gelen class_id'yi kullanabilirsiniz (yolo_detector'da class_number'ı döndürmeniz gerekir)
    #     class_id = 0 # Örnek sabit ID
    #     formatted_detections.append((bbox_xywh, conf, class_id))


    # update_tracks'e formatlanmış tespitleri ve frame'i verin
    tracks = self.object_tracker.update_tracks(formatted_detections, frame=frame) # formatted_detections kullanıldı

    tracking_ids = []
    boxes = []
    for track in tracks:
      if not track.is_confirmed():
        continue
      tracking_ids.append(track.track_id)
      ltrb = track.to_ltrb() # ltrb formatı [sol, üst, sağ, alt]
      boxes.append(ltrb)

    return tracking_ids, boxes