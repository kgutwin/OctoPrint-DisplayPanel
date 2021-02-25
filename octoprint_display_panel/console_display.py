
import os

CHRS = {
    ((0,0),(0,0)): ' ', ((0,0),(0,1)): '▗', ((0,0),(1,0)): '▖', ((0,0),(1,1)): '▄',
    ((0,1),(0,0)): '▝', ((0,1),(0,1)): '▐', ((0,1),(1,0)): '▞', ((0,1),(1,1)): '▟',
    ((1,0),(0,0)): '▘', ((1,0),(0,1)): '▚', ((1,0),(1,0)): '▌', ((1,0),(1,1)): '▙',
    ((1,1),(0,0)): '▀', ((1,1),(0,1)): '▜', ((1,1),(1,0)): '▛', ((1,1),(1,1)): '▉'
}

class SSD1306_I2C:
    def __init__(self, width, height, *args, **kwargs):
        self.width = width
        self.height = height
        self._image = None
        try:
            os.mkfifo('/tmp/micro-display')
        except OSError:
            pass

    def image(self, img):
        self._image = img

    def fill(self, v):
        pass
        
    def show(self):
        if not self._image:
            return
        px = self._image.getdata().pixel_access()
        l = []
        for i in range(0, self.height, 2):
            r = []
            for j in range(0, self.width, 2):
                c = ((px[j,i] and 1, px[j+1,i] and 1), (px[j,i+1] and 1, px[j+1,i+1] and 1))
                r.append(CHRS[c])
            r.append('┇')
            l.append(r)
        with open('/tmp/micro-display', 'w') as fp:
            print("\n".join("".join(r) for r in l), file=fp, flush=True)
        
