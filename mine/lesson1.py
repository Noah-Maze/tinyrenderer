import svgwrite

class Drawer(object):
    def __init__(self,filename):
        self.drawing = svgwrite.Drawing(filename, profile='tiny')
    def line(self,x,y):
        self.drawing.add(self.drawing.line(x,y, stroke=svgwrite.rgb(10, 10, 16, '%')))
    def text(self, x,y,text):
        self.drawing.add(self.drawing.text(text, insert=(x, y), fill='red'))
    def save(self):
        self.drawing.save()

lineTest = Drawer('lineTest.svg')
lineTest.line((0,0),(100,100))
lineTest.text(50,50,'Testing')
lineTest.save()
