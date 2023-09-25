import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_rectangle(ax, x, y, width, height, fill_ratio):
    # Draw outer rectangle
    outer_rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(outer_rect)

    # Calculate height of inner rectangle based on fill_ratio
    inner_height = height * fill_ratio

    # Draw inner rectangle
    inner_rect = patches.Rectangle((x, y), width, inner_height, linewidth=1, edgecolor='black', facecolor='blue')
    ax.add_patch(inner_rect)
