from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def main():
    model.train(data='Dataset/SplitData/data.yaml', epochs=5)


if __name__ == '__main__':
    main()