from pathlib import Path

import cv2


def load_image(image_path: Path):
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    return image


if __name__ == "__main__":
    image = load_image(Path("../../samples/gameplay.png"))
    height, width = image.shape[:2]
    print(f"Loaded image: {width} * {height}")
    cv2.imshow("Geometry Dash screenshot", image)
    cv2.waitKey(0)
