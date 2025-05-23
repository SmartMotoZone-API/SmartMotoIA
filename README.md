# SmartMotoIA

Kaio Cumpian Silva - 99816
Gabriel Yuji Suzuki - RM556588
Lucas Felix Vassiliades - RM97677



# Problema
A Mottu enfrenta desafios no controle da localização das motos em pátios de múltiplas filiais. O monitoramento atual é manual, sujeito a erros, e afeta a eficiência operacional. O objetivo é automatizar o mapeamento, identificação e rastreamento das motos com uma solução baseada em Visão Computacional.

# Objetivo da Análise
Detectar e rastrear visualmente motos em uma imagem/vídeo representando o pátio da Mottu e mapear suas posições em zonas definidas (ex: A1, B2...).

# Tecnologias utilizadas 

Componente                    Função

OpenCV (cv2)                | Processamento de imagem e vídeo, detecção de movimento e objetos
Torch                       | carregar e rodar o modelo YOLOv5
YOLOv5/YOLOv8 (Ultralytics) | Detecção/classificação de motos
Python                      | Lógica de IA e integração geral
cv2.imshow                  | Visualização das detecções
Pillow                      | É uma biblioteca para abrir, editar, salvar ou converter imagens
os                          | Proporciona interatividade com o sistema operacional

# Instalar pacotes

Digite no terminal:

> pip install torch torchvision opencv-python pillow
> pip install pandas
> pip install requests
> pip install seaborn

# Como rodar o projeto

Digite no terminal:

> python detectar_motos.py
