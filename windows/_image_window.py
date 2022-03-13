import warnings

import cv2 as cv
import dearpygui.dearpygui as dpg


class ImageWindow:
    def __init__(self, label, width, height, pos, tag):
        self.tag = tag
        self.width = width
        self.height = height
        self.image = None

        with dpg.window(label=label, width=width, height=height,
                        pos=pos, tag=tag):
            dpg.add_text(default_value='Path: None',
                         tag=f'{self.tag}_text_1')

    def show_image(self, image_path):
        try:
            dpg.delete_item(f'{self.tag}_text_1')
            dpg.delete_item(f'{self.tag}_texture_id')
            dpg.delete_item(f'{self.tag}_drawlist')
            self.image = None
        except SystemError:
            pass

        width, height, _, data = dpg.load_image(image_path)

        if width > self.width or height > self.height:
            warnings.warn('Image size more than size of the window',
                          RuntimeWarning)

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data,
                                   tag=f'{self.tag}_texture_id')

        with dpg.drawlist(width=width, height=height, parent=self.tag,
                          tag=f'{self.tag}_drawlist'):
            dpg.draw_image(f'{self.tag}_texture_id', (0, 0), (width, height),
                           uv_min=(0, 0), uv_max=(1, 1))

        dpg.add_text(default_value=f'Path: {image_path}',
                     tag=f'{self.tag}_text_1',
                     parent=self.tag)

        self.image = cv.imread(image_path)

    def draw_box(self, p1, p2, color, tag, thickness):
        try:
            dpg.delete_item(f'{self.tag}_box_{tag}')
        except SystemError:
            pass

        dpg.draw_rectangle(p1, p2, color=color,
                           tag=f'{self.tag}_box_{tag}',
                           parent=f'{self.tag}_drawlist',
                           thickness=thickness)
