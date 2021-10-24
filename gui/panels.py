class ActionMenu:
    def __init__(self, gui):
        pos, size = (0,gui.height*0.84), (gui.width,gui.height * 0.16)
        self.panel = gui.gui_sub_panel(pos,size)


class NotificationDisplay:
    def __init__(self, gui):
        pos, size = (gui.width*0.85,gui.height*0.04), (gui.width * 0.15,gui.height * 0.8)
        self.panel = gui.gui_sub_panel(pos,size)


class SubMenu:
    def __init__(self, gui):
        pos, size = (0,gui.height*0.04), (gui.width * 0.15,gui.height * 0.8)
        self.panel = gui.gui_sub_panel(pos,size)


class Toolbar:
    def __init__(self, gui):
        pos, size = (0,0), (gui.width,gui.height * 0.04)
        self.panel = gui.gui_sub_panel(pos,size)


class Viewport:
    def __init__(self, gui):
        self.width, self.height = (gui.width * 0.7,gui.height * 0.8)
        pos, size = (gui.width*0.15,gui.height*0.04), (self.width,self.height)
        self.panel = gui.gui_sub_panel(pos,size)

class AlertWindow:
    def __init__(self, gui, view):
        pos, size = (view.width * 0.1,view.height * 0.1),(view.width * 0.8, view.height * 0.65)
        self.panel = gui.gui_sub_panel(pos,size,view.panel)
        self.panel.hide()
