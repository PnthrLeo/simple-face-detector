import cv2 as cv


class TemplateDetector:
    def __init__(self, image_window, template_window):
        self.image_window = image_window
        self.template_window = template_window

    def predict(self, method=cv.TM_SQDIFF):
        image = self.image_window.image
        template = self.template_window.image

        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

        template_template_borders = self.template_window.face_template.template_borders  # noqa: E501

        ttb_x1, ttb_y1, ttb_x2, ttb_y2 = template_template_borders

        template = template[ttb_y1:ttb_y2, ttb_x1:ttb_x2]

        res = cv.matchTemplate(image, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        self.show_result(top_left, template.shape)

    def show_result(self, template_top_left, template_shape):
        ld = self.template_window.face_template.left_delta
        rd = self.template_window.face_template.right_delta
        ud = self.template_window.face_template.up_delta
        dd = self.template_window.face_template.down_delta

        x1_template = template_top_left[0]
        y1_template = template_top_left[1]
        x2_template = template_top_left[0] + template_shape[1]
        y2_template = template_top_left[1] + template_shape[0]

        x1_face = template_top_left[0] + ld
        y1_face = template_top_left[1] + ud
        x2_face = template_top_left[0] + template_shape[1] + rd
        y2_face = template_top_left[1] + template_shape[0] + dd

        self.image_window.draw_box(p1=[x1_template, y1_template],
                                   p2=[x2_template, y2_template],
                                   color=(0, 255, 0, 255),
                                   tag='predicted_template',
                                   thickness=5)

        self.image_window.draw_box(p1=[x1_face, y1_face],
                                   p2=[x2_face, y2_face],
                                   color=(255, 0, 0, 255),
                                   tag='predicted_face',
                                   thickness=5)


class ViolaJonesDetector:
    def __init__(self, image_window):
        self.image_window = image_window

    def predict(self, method=cv.TM_SQDIFF):
        image = self.image_window.image

        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        face_cascade = cv.CascadeClassifier(
            cv.data.haarcascades + 'haarcascade_frontalface_default.xml',
        )
        eye_cascade = cv.CascadeClassifier(
            cv.data.haarcascades + 'haarcascade_eye.xml',
        )

        detected_faces = face_cascade.detectMultiScale(image)

        for f_idx, f_values in enumerate(detected_faces):
            x, y, w, h = f_values
            face_image = image[y: y + h, x: x + w]
            detected_eyes = eye_cascade.detectMultiScale(face_image)

            self.show_result(x, y, w, h,
                             color=(255, 0, 0, 255),
                             tag=f'predicted_face_{f_idx}')
            for e_idx, e_values in enumerate(detected_eyes):
                ex, ey, ew, eh = e_values
                self.show_result(ex+x, ey+y, ew, eh,
                                 color=(0, 255, 0, 255),
                                 tag=f'predicted_eye__{f_idx}_{e_idx}')

    def show_result(self, x, y, w, h, color, tag):
        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h
        self.image_window.draw_box(p1=[x1, y1], p2=[x2, y2],
                                   color=color,
                                   tag=tag,
                                   thickness=5)
