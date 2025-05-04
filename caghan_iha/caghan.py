from ultralytics import YOLO

model = YOLO("caghan_model.pt")

results = model("test", save = True)
