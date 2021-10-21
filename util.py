import pygame_gui
import pygame as pg

def new_label(container, manager, pos, size, txt):
    label = pygame_gui.elements.UITextBox(container=container,
                                          relative_rect=pg.Rect(pos, size),
                                          manager=manager,
                                          html_text=txt
                                          )
    return label

def new_header(container, manager, pos, size, txt):
    header = pygame_gui.elements.UIButton(container=container,
                                          relative_rect=pg.Rect(pos, size),
                                          manager=manager,
                                          text=txt,
                                          )

    return header


def find_key_parent(d, key):
    for k, v in d.items():
        if isinstance(v,dict):
            for k1, v1 in v.items():
                if k1 == key:
                    return k

