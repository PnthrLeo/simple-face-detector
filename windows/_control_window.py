import dearpygui.dearpygui as dpg
from algo import TemplateDetector, ViolaJonesDetector

from windows.subcontrol import TemplateControlWindow


class ControlWindow:
    def __init__(self, label, width, height, pos, tag, image_window,
                 template_window):
        self.tag = tag
        self.width = width
        self.height = height
        self.image_window = image_window
        self.template_window = template_window
        self.template_control_window = None

        with dpg.window(label=label, width=width, pos=pos,
                        height=height, tag=tag):
            dpg.add_button(label='Image Selector',
                           callback=self.button_file_dialog_callback,
                           tag=f'{self.tag}_button_1')
            dpg.add_button(label='Template Selector',
                           callback=self.button_file_dialog_callback,
                           tag=f'{self.tag}_button_2')
            dpg.add_button(label='Predict via Template method',
                           callback=self.button_predict_template_callback,
                           tag=f'{self.tag}_button_3')
            dpg.add_button(label='Predict via Viola Jones method',
                           callback=self.button_predict_viola_callback,
                           tag=f'{self.tag}_button_4')
            dpg.add_checkbox(label='Template Settings Window',
                             callback=self.checkbox_1_callback,
                             tag=f'{self.tag}_checkbox_1')

    def button_file_dialog_callback(self, sender, *_unused):
        try:
            dpg.delete_item(f'{self.tag}_file_dialog')
        except SystemError:
            pass

        with dpg.file_dialog(directory_selector=False, show=True,
                             callback=self.file_dialog_callback,
                             tag=f'{self.tag}_file_dialog',
                             height=400):
            dpg.set_item_user_data(f'{self.tag}_file_dialog', sender)
            dpg.add_file_extension(
                'Source files (*.png *.jpg *.jpeg){.png,.jpg,.jpeg}',
                color=(150, 255, 150, 255)
            )

    def button_predict_template_callback(self, sender, app_data):
        detector = TemplateDetector(self.image_window, self.template_window)
        detector.predict()

    def button_predict_viola_callback(self, sender, app_data):
        detector = ViolaJonesDetector(self.image_window)
        detector.predict()

    def file_dialog_callback(self, _unused, app_data, user_data):
        if (len(app_data['selections']) == 0):
            return

        button_tag = user_data

        if button_tag == f'{self.tag}_button_1':
            self.image_window.show_image(app_data['file_path_name'])
        elif button_tag == f'{self.tag}_button_2':
            self.template_window.show_image(app_data['file_path_name'])

        dpg.delete_item(f'{self.tag}_file_dialog')

    def checkbox_1_callback(self, _unused, app_data):
        is_checkbox_set = app_data

        if is_checkbox_set:
            self.template_control_window = TemplateControlWindow(
                label='Template Control Window',
                width=self.width, height=250,
                pos=(0, self.height),
                tag=f'{self.tag}_template_control_window',
                template_window=self.template_window
            )
        else:
            self.template_control_window.delete()
