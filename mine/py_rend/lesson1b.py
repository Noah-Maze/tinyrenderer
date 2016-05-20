import sys
import svgwrite
from collections import namedtuple
from decimal import Decimal

W = 1280
H = 600

# Vertex type
Vertex = namedtuple('Vertex', ['x', 'y', 'z'])

class Drawer(object):
    def __init__(self, filename):
        self.drawing = svgwrite.Drawing(filename, profile='tiny')
    def line(self, start, stop):
        self.drawing.add(self.drawing.line(start,stop, stroke=svgwrite.rgb(10, 10, 16, '%')))
    def line3(self, start3, stop3):
        # Trunc Z for now because laziness
        start = (start3[0],start3[1])
        stop = (stop3[0],stop3[1])
        self.line(start, stop)
    def text(self, start, text):
        self.drawing.add(self.drawing.text(text, insert=start, fill='red'))
    def save(self):
        self.drawing.save()

# Load the model
with open(sys.argv[1]) as ob:
    # List of Vertex
    vertexes = []
    # List of Vertex Pairs by smallest index first
    lines = set()
    for line in ob:
        if line.startswith('v '):
            v = Vertex(*[float(n) for n in line[2:].split(' ')])
            vertexes.append(v)
        # Skipping texture data (vt)
        # Skipping normals (vn)
        if line.startswith('f '):
            # Break it into items
            items = line[2:].split(' ')
            # Break off vertex indexes (the rest relates to vt, vn)
            vert_inds = [a.partition('/')[0] for a in line[2:].split(' ')]
            # Add pairs to set
            pairs=[]
            for i in range(0,len(vert_inds)):
                start = int(vert_inds[i])-1
                stop = int(vert_inds[(i+1)%len(vert_inds)])-1
                if start > stop:
                    pairs.append((start, stop))
                else:
                    pairs.append((stop,start))
            # Update linelist with new pairs
            lines.update(set(pairs))

# Scale vertexes because obj scaling isn't standardized at all, wtf
fv = max(vertexes, key=lambda v: v[0]**2+v[1]**2)
sc = -min([H,W])/(2*int(fv[0]**2+fv[1]**2)**0.5)
oc = min([H,W])/2
vertexes = [ (int(v[0]*sc)+oc,int(v[1]*sc)+oc,int(v[2]*sc)+oc) for v in vertexes]

# Open a new file
objTest = Drawer(sys.argv[2])
# Add a line between every vertext pair
for line in lines:
    objTest.line3(vertexes[line[0]],vertexes[line[1]])
# Save it
objTest.save()
