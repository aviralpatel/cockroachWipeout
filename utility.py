import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_rectangle(ax, fill_ratio, x=0, y=0, width=1, height=1):
    # Draw outer rectangle
    outer_rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(outer_rect)

    # Calculate height of inner rectangle based on fill_ratio
    inner_width = width * fill_ratio

    # Draw inner rectangle
    inner_rect = patches.Rectangle((x, y), inner_width, height, linewidth=1, edgecolor='black', facecolor='lightpink')
    ax.add_patch(inner_rect)

    return inner_rect
