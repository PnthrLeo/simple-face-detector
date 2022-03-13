import numpy as np


class FaceTemplate():
    def __init__(self):
        self.image_width = None
        self.image_height = None
        self.face_borders = [-1] * 4
        self.template_borders = [-1] * 4
        self.left_delta = None
        self.right_delta = None
        self.up_delta = None
        self.down_delta = None

    def set_face_borders(self, x1=None, y1=None, x2=None, y2=None):
        new_face_borders = np.array([x1, y1, x2, y2])
        old_face_borders = np.array(self.face_borders)
        new_face_borders = np.where(np.equal(new_face_borders, None),
                                    old_face_borders,
                                    new_face_borders).tolist()
        self.face_borders = new_face_borders
        if (None not in self.face_borders and
                None not in self.template_borders):
            self.__calculate_delta()

    def set_template_borders(self, x1=None, y1=None, x2=None, y2=None):
        new_template_borders = np.array([x1, y1, x2, y2])
        old_template_borders = np.array(self.template_borders)
        new_template_borders = np.where(np.equal(new_template_borders, None),
                                        old_template_borders,
                                        new_template_borders).tolist()
        self.template_borders = new_template_borders
        if (None not in self.template_borders and
                None not in self.face_borders):
            self.__calculate_delta()

    def set_image_size(self, image_width, image_height):
        self.image_width = image_width
        self.image_height = image_height

    def __calculate_delta(self):
        self.left_delta = self.face_borders[0] - self.template_borders[0]
        self.up_delta = self.face_borders[1] - self.template_borders[1]
        self.right_delta = self.face_borders[2] - self.template_borders[2]
        self.down_delta = self.face_borders[3] - self.template_borders[3]
