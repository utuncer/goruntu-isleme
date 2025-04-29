# OpenCV Kütüphanesi Kullanımı

https://www.geeksforgeeks.org/opencv-python-tutorial/

https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

Python Yorumlayıcısı oluştur:

```bash
  python -m venv .venv
```

Sanal Ortamı Aktifleştirin

```bash
(Windows) .\.venv\Scripts\activate
```

```bash
(macOS/Linux) source .venv/bin/activate
```

İndir:

```bash
  pip install opencv-python
```

```bash
  pip install cv2
```

## Görsellerin Mantığı

```bash
resim = cv2.imread("gorsel")
print(resim.shape) # (471, 840, 3)
```

- 471 değeri yükseklik, 840 değeri genişlik ve 3 değeri ise renk kanalı sayısıdır.
- Eğer renk kanalı 0 ise görsel siyah-beyaz'dır.

```bash
print(resim.size) # 471*840*3 = 1186920
```

- Yükseklik, genişlik ve renk kanalı sayısı değerlerinin çarpımıyla gorselin boyutu bulunur.
