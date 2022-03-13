import dearpygui.dearpygui as dpg

from windows import ControlWindow, ImageWindow, TemplateWindow

dpg.create_context()


image_window = ImageWindow(label='Image', width=300, height=300,
                           pos=(300, 0),
                           tag='image_window')

template_window = TemplateWindow(label='Template', width=300, height=300,
                                 pos=(600, 0),
                                 tag='template_window')

control_window = ControlWindow(label='Control', width=300, height=400,
                               pos=(0, 0),
                               tag='control_window',
                               image_window=image_window,
                               template_window=template_window)


dpg.create_viewport(title='Face Detector', width=1080, height=1080)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
