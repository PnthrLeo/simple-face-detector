import dearpygui.dearpygui as dpg


class TemplateControlWindow():
    def __init__(self, label, width, height, pos, tag, template_window):
        self.tag = tag
        self.template_window = template_window

        face_template = self.template_window.face_template
        with dpg.window(label=label, width=width,
                        height=height, pos=pos,
                        tag=self.tag):
            dpg.add_input_int(label='Face x1', callback=self.__input_callback,
                              default_value=face_template.face_borders[0],
                              tag=f'{self.tag}_input_1')
            dpg.add_input_int(label='Face y1', callback=self.__input_callback,
                              default_value=face_template.face_borders[1],
                              tag=f'{self.tag}_input_2')
            dpg.add_input_int(label='Face x2', callback=self.__input_callback,
                              default_value=face_template.face_borders[2],
                              tag=f'{self.tag}_input_3')
            dpg.add_input_int(label='Face y2', callback=self.__input_callback,
                              default_value=face_template.face_borders[3],
                              tag=f'{self.tag}_input_4')
            dpg.add_input_int(label='Template x1',
                              callback=self.__input_callback,
                              default_value=face_template.template_borders[0],  # noqa: E501
                              tag=f'{self.tag}_input_5')
            dpg.add_input_int(label='Template y1',
                              callback=self.__input_callback,
                              default_value=face_template.template_borders[1],  # noqa: E501
                              tag=f'{self.tag}_input_6')
            dpg.add_input_int(label='Template x2',
                              callback=self.__input_callback,
                              default_value=face_template.template_borders[2],  # noqa: E501
                              tag=f'{self.tag}_input_7')
            dpg.add_input_int(label='Template y2',
                              callback=self.__input_callback,
                              default_value=face_template.template_borders[3],  # noqa: E501
                              tag=f'{self.tag}_input_8')

    def __input_callback(self, sender, app_data):
        face_template = self.template_window.face_template
        if sender == f'{self.tag}_input_1':
            face_template.set_face_borders(x1=app_data)
        elif sender == f'{self.tag}_input_2':
            face_template.set_face_borders(y1=app_data)
        elif sender == f'{self.tag}_input_3':
            face_template.set_face_borders(x2=app_data)
        elif sender == f'{self.tag}_input_4':
            face_template.set_face_borders(y2=app_data)
        elif sender == f'{self.tag}_input_5':
            face_template.set_template_borders(x1=app_data)
        elif sender == f'{self.tag}_input_6':
            face_template.set_template_borders(y1=app_data)
        elif sender == f'{self.tag}_input_7':
            face_template.set_template_borders(x2=app_data)
        elif sender == f'{self.tag}_input_8':
            face_template.set_template_borders(y2=app_data)

        if -1 not in face_template.face_borders:
            self.template_window.draw_box(
                face_template.face_borders[0:2],
                face_template.face_borders[2:4],
                color=(255, 0, 0, 255),
                tag='face',
                thickness=5
            )
        if -1 not in face_template.template_borders:
            self.template_window.draw_box(
                face_template.template_borders[0:2],
                face_template.template_borders[2:4],
                color=(0, 255, 0, 255),
                tag='template',
                thickness=5
            )

    def delete(self):
        dpg.delete_item(self.tag)
