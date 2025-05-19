import cv2
import torch
import os

# Lista de imagens que vai processar
imagens = ["imagem_patio1.jpg", "imagem_patio2.jpg"]

# Carrega o modelo YOLOv5 pré-treinado
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.4  

# Processa cada imagem
for imagem_path in imagens:
    if not os.path.exists(imagem_path):
        print(f"Imagem não encontrada: {imagem_path}")
        continue

    # Carrega imagem
    img = cv2.imread(imagem_path)

    # Faz a inferência
    results = model(img)
    detections = results.pandas().xyxy[0]

    # Processa detecções
    for _, det in detections.iterrows():
        class_name = det['name']
        x1, y1, x2, y2 = map(int, [det['xmin'], det['ymin'], det['xmax'], det['ymax']])

        if class_name == 'motorcycle':
            # Simula lógica de zona (exemplo simples baseado em posição)
            zona = 'A1' if x1 < img.shape[1] // 2 else 'B2'

            # Desenha retângulo e texto
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Moto - {zona}"
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

    # Exibe a imagem
    cv2.imshow(f'Detecção: {imagem_path}', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
