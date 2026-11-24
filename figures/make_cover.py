"""Draw the honeycomb lattice and the two graphene bands from chapter 10."""

from cmath import exp
from math import cos, pi, sin, sqrt
from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.pdfgen.canvas import Canvas


WIDTH, HEIGHT = 600, 454
PAPER = HexColor("#112a41")
ICE = HexColor("#a4d8dc")
COPPER = HexColor("#f0bd83")


def blend(first, second, fraction):
    channels = zip(first.rgb(), second.rgb())
    return Color(*(a + fraction * (b - a) for a, b in channels))


def honeycomb(canvas):
    spacing = 56
    angle = -pi / 15
    a1 = (spacing * cos(angle), spacing * sin(angle))
    a2 = (spacing * cos(angle + pi / 3), spacing * sin(angle + pi / 3))

    def position(i, j):
        return 73 + i * a1[0] + j * a2[0], 199 + i * a1[1] + j * a2[1]

    def visibility(x, y):
        # Fade the real-space lattice before it meets the reciprocal-space plot.
        radius = ((x - 70) / 220) ** 2 + ((y - 214) / 290) ** 2
        return max(0, 1 - radius) ** 1.5

    bonds = []
    atoms = []
    for i in range(-11, 9):
        for j in range(-7, 9):
            ax, ay = position(i, j)
            bx, by = position(i + 1 / 3, j + 1 / 3)
            atoms.extend([(ax, ay, ICE), (bx, by, COPPER)])
            for di, dj in [(0, 0), (-1, 0), (0, -1)]:
                x, y = position(i + di + 1 / 3, j + dj + 1 / 3)
                bonds.append((ax, ay, x, y))
    for x1, y1, x2, y2 in bonds:
        strength = visibility((x1 + x2) / 2, (y1 + y2) / 2)
        if strength > 0.01:
            canvas.setStrokeColor(blend(PAPER, ICE, 0.6 * strength))
            canvas.setLineWidth(0.7)
            canvas.line(x1, y1, x2, y2)
    for x, y, color in atoms:
        strength = visibility(x, y)
        if strength > 0.01:
            canvas.setFillColor(blend(PAPER, color, 0.9 * strength))
            canvas.circle(x, y, 1.3 + 0.9 * strength, stroke=0, fill=1)


def energy_bands(canvas):
    # a1=(1,0), a2=(1/2,sqrt(3)/2), K=(4*pi/3,0), hopping t=1.
    rings, sectors = 19, 72
    center_x, center_y = 385, 220

    def sample(ring, sector, sign):
        theta = 2 * pi * sector / sectors
        qx, qy = ring * cos(theta) / rings, ring * sin(theta) / rings
        kx = 4 * pi / 3 + qx
        energy = sign * abs(1 + exp(-1j * kx) + exp(-1j * (kx + sqrt(3) * qy) / 2))
        screen = (center_x + 177 * qx, center_y + 43 * qy + 148 * energy)
        return screen, -qy + 0.29 * energy

    facets = []
    for sign, color in [(-1, ICE), (1, COPPER)]:
        for ring in range(rings):
            for sector in range(sectors):
                corners = [sample(r, s, sign) for r, s in
                           [(ring, sector), (ring + 1, sector),
                            (ring + 1, sector + 1), (ring, sector + 1)]]
                points, depths = zip(*corners)
                light = 0.21 + 0.065 * cos(2 * pi * sector / sectors + 0.8)
                facets.append((sum(depths) / 4, points, ring, sector, color, light))

    # Paint the far side first so grid lines on the back are hidden by the front.
    for _, points, ring, sector, color, light in sorted(facets, key=lambda item: item[0]):
        contour = canvas.beginPath()
        contour.moveTo(*points[0])
        for p in points[1:]:
            contour.lineTo(*p)
        contour.close()
        face = blend(PAPER, color, light)
        canvas.setFillColor(face)
        canvas.setStrokeColor(face)
        canvas.setLineWidth(0.32)
        canvas.drawPath(contour, fill=1, stroke=1)
        canvas.setStrokeColor(blend(PAPER, color, 0.72))
        canvas.setLineWidth(0.52)
        if sector % 3 == 0:
            canvas.line(*points[0], *points[1])
        if ring % 2 == 0:
            canvas.line(*points[1], *points[2])
        if ring == rings - 1:
            canvas.setStrokeColor(color)
            canvas.setLineWidth(1.25)
            canvas.line(*points[1], *points[2])
    canvas.setFillColor(HexColor("#fff2d9"))
    canvas.circle(center_x, center_y, 2.0, fill=1, stroke=0)


def main():
    target = Path(__file__).with_name("cover.pdf")
    canvas = Canvas(str(target), pagesize=(WIDTH, HEIGHT), pageCompression=1, invariant=1)
    canvas.setTitle("Graphene lattice and band contact at K")
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, WIDTH, HEIGHT, stroke=0, fill=1)
    honeycomb(canvas)
    energy_bands(canvas)
    canvas.showPage()
    canvas.save()


if __name__ == "__main__":
    main()
