def horizontal_distance(player: tuple, obstacle: tuple) -> int:
    player_right = player[0] + player[2]
    obstacle_left = obstacle[0]
    return obstacle_left - player_right


if __name__ == "__main__":
    player = (100, 500, 40, 40)
    obstacle = (200, 480, 40, 60)
    print(f"Horizontal distance: {horizontal_distance(player, obstacle)} px")
    print(f"Obstacle height: {obstacle[3]} px")
