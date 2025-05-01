# OpenCV Kütüphanesi Kullanımı

https://www.geeksforgeeks.org/opencv-python-tutorial/

https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

https://abdulsamet-ileri.medium.com/g%C3%B6r%C3%BCnt%C3%BC-filtrelerini-uygulama-ve-kenarlar%C4%B1-alg%C4%B1lama-21d42f194db4

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

## OpevCV Koordinat Mantığı

![Koordinat Görüntüsü](https://community.stereolabs.com/uploads/default/original/1X/b5e996d4114fdf303c56f0f396106b20a49cbd7c.png)
