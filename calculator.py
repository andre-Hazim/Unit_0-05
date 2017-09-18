# created by andre hazim
#created on Sept 2017
#created for ICS3U
#program can do basic math
import ui

def calculation_one_touch_up_inside (sender):
    #5+2^3
    view['answer1_label1'].text = str('Area = ')+str(5*3) + str('cm**2')
    view['answer2_label'].text = str('Perimeter = ')+str(3*2+5*2)+str('cm')

view = ui.load_view()
view.present('sheet')
