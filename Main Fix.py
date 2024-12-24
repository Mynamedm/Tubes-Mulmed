import cv2
import mediapipe as mp
import numpy as np
import random

# Inisialisasi MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2, refine_landmarks=True)

# Fungsi untuk menggambar glitter pada wajah
def apply_glitter_effect(image, mask, num_particles=100):
    y, x = np.where(mask > 0)
    if len(y) > 0:
        for _ in range(num_particles):
            idx = random.randint(2, len(y) -1)  # Pilih titik acak
            point_x, point_y = x[idx], y[idx]
            color = (
                random.randint(73, 255),  # Biru
                random.randint(98, 255),  # Hijau
                random.randint(140, 255),  # Merah
            )   # Format warna RGB
            cv2.circle(image, (point_x, point_y), 1, color, -1)

# Buka webcam
cap = cv2.VideoCapture(0)  # Ganti ke 1 untuk webcam eksternal
if not cap.isOpened():
    print("Kamera tidak dapat dibuka. Pastikan sudah terhubung.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame untuk efek mirror
    frame = cv2.flip(frame, 1)
    image_height, image_width, _ = frame.shape

    # Konversi warna ke RGB untuk MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi wajah dengan Face Mesh
    results = face_mesh.process(rgb_frame)

    # Mask untuk area wajah
    mask = np.zeros((image_height, image_width), dtype=np.uint8)

    # Jika wajah terdeteksi
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Landmark wajah
            landmarks = [(int(l.x * image_width), int(l.y * image_height)) for l in face_landmarks.landmark]

            # Buat polygon untuk seluruh wajah
            face_outline = [landmarks[i] for i in range(0, 468)]
            cv2.fillPoly(mask, [np.array(face_outline, dtype=np.int32)], 255)

            # Hapus area mata
            left_eye = [landmarks[i] for i in range(129, 154)] + [landmarks[i] for i in range(154, 132)]
            right_eye = [landmarks[i] for i in range(364, 382)] + [landmarks[i] for i in range(382, 359)]
            cv2.fillPoly(mask, [np.array(left_eye, dtype=np.int32)], 0)
            cv2.fillPoly(mask, [np.array(right_eye, dtype=np.int32)], 0)

        # Terapkan efek glitter
        apply_glitter_effect(frame, mask)

    # Tampilkan hasil
    cv2.imshow('Glitter Face Filter', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Tekan ESC untuk keluar
        break

# Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()