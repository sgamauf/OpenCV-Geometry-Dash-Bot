import os
import sys
from pathlib import Path

import cv2

from gd_bot.geometry import horizontal_distance


# Get the image from path
def load_image(image_path: Path):
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    return image


if __name__ == "__main__":
    # Configure OpenCV's Qt preview for this Linux desktop.
    # Set these after importing cv2, which supplies its own font directory.
    if sys.platform.startswith("linux"):
        if os.environ.get("WAYLAND_DISPLAY") and os.environ.get("DISPLAY"):
            os.environ["QT_QPA_PLATFORM"] = "xcb"
        font_directory = Path("/usr/share/fonts/noto")
        if font_directory.is_dir():
            os.environ["QT_QPA_FONTDIR"] = str(font_directory)

    image = load_image(Path("../../samples/gameplay.png"))
    height, width = image.shape[:2] # .shape returns height and width as its first two elements
    print(f"Loaded image: {width} * {height}")

    preview = image.copy() # Get image copy to draw on

    # player rectangle
    player = (439, 451, 65, 64) # (x,y,width,height)
    playerX, playerY, playerWidth, playerHeight = player

    cv2.rectangle(
        preview,
        (playerX, playerY),
        (playerX + playerWidth, playerY + playerHeight),
        (0, 0, 255),
        2,
    )

    # block rectangle
    obstacle = (539, 450, 67, 65) # (x,y,width,height)
    x, y, width, height = obstacle

    cv2.rectangle(
        preview,
        (x, y),
        (x + width, y + height),
        (0, 255, 0),
        2,
    )

    distance = horizontal_distance(player, obstacle)
    playerRight = playerX + playerWidth
    line_y = min(playerY, y) - 15

    cv2.line(
        preview,
        (playerRight, line_y),
        (x, line_y),
        (0, 255, 255),
        2,
    )

    cv2.putText(
        preview,
        f"{distance} px",
        (playerRight, line_y - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.4,
        color=(0, 255, 255),
        thickness=1,
    )
    print(f"Manual block box: {obstacle[2]}x{obstacle[3]} px")
    print(f"Distance to selected obstacle: {distance} px")

    cv2.imshow("Test screenshot", preview)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
