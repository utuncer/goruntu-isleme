### Kullanılan Algoritmalar

- TID (Tracking Interaction Detection)
- PID (Proportional Integral Derivative)
- Dubins Path
- YOLO (You Only Look Once)
- DeepSORT
- Kalman Filtresi
- RRT (Rapidly - Exploring Random Tree)
- PN (Proportional Navigation)

### Sanal Ortam (Wİndows)

Üçüncü parti modülleri sisteminize yüklemeyi sağlayan sistem olan PIP'ı kurmadıysanız kurun

```bash
python -m pip install -U pip
```

```bash
pip install virtualenv
```

Sanal ortamın oluşturulacağı yere gir

```bash
virtualenv venv
```

Sanal Ortama Kütüphane Ekleme

```bash
venv\Scripts\activate
```
### Sanal Ortam (Linux)

Üçüncü parti modülleri sisteminize yüklemeyi sağlayan sistem olan PIP'ı kurmadıysanız kurun

```bash
sudo apt update
sudo apt install python3-pip -y
python3 -m pip install --upgrade pip
```

```bash
pip3 install virtualenv
```

Sanal ortamın oluşturulacağı yere gir

```bash
virtualenv venv
```

Sanal Ortama Kütüphane Ekleme

```bash
source venv/bin/activate
```
Gerekli Kütüphaneler

```bash
pip install numpy
```

```bash
pip install ultralytics
```
OpenCV'de imshow gibi komutlar için GUI kütühaneleri gereklidir
```bash
pip install opencv-python
```
```bash
sudo apt update
```
```bash
sudo apt install -y libgtk2.0-dev libgl1-mesa-glx
```
