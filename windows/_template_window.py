import dearpygui.dearpygui as dpg
from algo import FaceTemplate

from windows import ImageWindow


class TemplateWindow(ImageWindow):
    def __init__(self, label, width, height, pos, tag):
        self.face_template = None
        super().__init__(label, width, height, pos, tag)

    def show_image(self, image_path):
        width, height, _, data = dpg.load_image(image_path)
        self.face_template = FaceTemplate()
        self.face_template.set_image_size(width, height)
        super().show_image(image_path)
