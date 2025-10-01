import cv2
import os
from ultralytics import YOLO

# Lista de imagens que vai processar
imagens = ["imagem_patio1.jpg", "imagem_patio2.jpg"]

# Carrega o modelo YOLOv8 
model = YOLO("yolov8n.pt")

# Processa cada imagem
for imagem_path in imagens:
    if not os.path.exists(imagem_path):
        print(f"❌ Imagem não encontrada: {imagem_path}")
        continue

    # Carrega a imagem
    img = cv2.imread(imagem_path)

    # Faz a inferência
    results = model(img)

    # Itera sobre os resultados
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])        
            conf = float(box.conf[0])       
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # coordenadas da bounding box

            # Nome da classe (ex: "person", "car", "motorcycle"...)
            class_name = model.names[cls_id]

            if class_name == "motorcycle":
                # Simula lógica de zona (exemplo: esquerda = A1, direita = B2)
                zona = 'A1' if x1 < img.shape[1] // 2 else 'B2'

                # Desenha retângulo e label
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"Moto - {zona} ({conf:.2f})"
                cv2.putText(img, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Mostra a imagem processada
    cv2.imshow(f"Detecção: {os.path.basename(imagem_path)}", img)
    cv2.waitKey(0)  # espera até apertar uma tecla
    cv2.destroyAllWindows()
