from ctypes import Structure, c_long, windll, byref


class RECT(Structure):
    _fields_ = [
        ('left', c_long),
        ('top', c_long),
        ('right', c_long),
        ('bottom', c_long),
    ]

    def width(self):  return self.right - self.left

    def height(self): return self.bottom - self.top


def window_on_top(window):
    set_window_pos = windll.user32.SetWindowPos
    get_window_rect = windll.user32.GetWindowRect
    rc = RECT()
    get_window_rect(window, byref(rc))
    set_window_pos(window, -1, rc.left, rc.top, 0, 0, 0x0001)
