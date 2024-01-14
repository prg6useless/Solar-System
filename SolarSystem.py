from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import random

start_time = time.time()

year = 0
day = 0
x_dist = []
y_dist = []
size = []

for _ in range(500):
    x_dist.append(random.uniform(-30, 30))
    y_dist.append(random.uniform(-15, 15))
    size.append(random.uniform(0, 3))


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)


def Star():
    glEnable(GL_POINT_SMOOTH)
    for i in range(500):
        glPointSize(size[i])

        glBegin(GL_POINTS)
        glColor3d(1, 1, 1)
        glVertex3d(x_dist[i], y_dist[i], 0)
        glEnd()


def Orbit(radius, x, y, z):
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    angle = 0
    while angle < (2 * math.pi):
        x1 = x + math.cos(angle) * radius
        y1 = y
        z1 = z + math.sin(angle) * radius
        glVertex3f(x1, y1, z1)
        angle = angle + 0.01
    glEnd()


def Mercury(t):
    glPopMatrix()
    glPushMatrix()
    year_periodM = 0.24 * 8
    yearM = t / year_periodM
    dayM = 88 * yearM
    glRotatef(yearM * 360.0, 0, 1.0, 0.0)
    Orbit(1.2, 0, -0.25, 0.0)
    glTranslatef(1.2, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayM * 360, 0.0, 0.5, 0.0)
    glRotatef(90, 1.0, 3.0, 0.0)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidSphere(0.05, 10, 8)
    glPopMatrix()
    glPopMatrix()


def Venus(t):
    glPopMatrix()
    glPushMatrix()
    year_periodV = 0.62 * 8
    yearV = t / year_periodV
    dayV = 225 * yearV
    glRotatef(yearV * 360.0, 0, 1, 0)
    Orbit(1.5, 0, -0.25, 0.0)
    glTranslatef(1.5, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayV * 360, 0.0, 1.0, 0.0)
    glRotatef(90, 3.0, 2.0, 0.0)
    glColor3f(1, 0.5, 0)
    glutSolidSphere(0.1, 10, 8)
    glPopMatrix()
    glPopMatrix()


def Earth_System(t):
    year_period = 1 * 8
    year = t / year_period
    day = 365 * year
    moon_syn = (365 / 29.5) * year
    glRotatef(year * 360.0, 0, 1, 0)
    Orbit(2.1, 0, -0.25, 0.0)
    glTranslatef(2.1, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(day * 360.0, 0.0, 1.0, 0.0)
    glRotatef(90 - 23.4, 1.0, 1.0, 0.0)
    glColor3f(0.1, 0.4, 1)
    glutSolidSphere(0.15, 10, 8)
    glPopMatrix()
    glPushMatrix()
    glRotatef(moon_syn * 360.0, 0.0, 1.0, 0.0)
    glTranslatef(0.5, 0.0, 0.0)
    glRotatef(90, 1.0, 1.0, 0.0)
    glColor4f(0.4, 0.5, 0.6, 1)
    glutSolidSphere(0.05, 10, 8)
    glPopMatrix()
    glPopMatrix()


def Mars(t):
    glPopMatrix()
    glPushMatrix()
    year_periodMa = 1.88 * 8
    yearMa = t / year_periodMa
    dayMa = 687 * yearMa
    glRotatef(yearMa * 360.0, 0, 1, 0)
    Orbit(2.7, 0, -0.25, 0.0)
    glTranslatef(2.7, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayMa * 360, 0.0, 1.0, 0.0)
    glRotatef(75, 3.0, 2.0, 1.0)
    glColor3f(1, 0.3, 0)
    glutSolidSphere(0.12, 10, 8)
    glPopMatrix()
    glPopMatrix()


def Jupiter(t):
    glPopMatrix()
    glPushMatrix()
    year_periodJ = 11.86 * 8
    yearJ = t / year_periodJ
    dayJ = 4332 * yearJ
    glRotatef(yearJ * 360.0, 0, 1, 0)
    Orbit(3.6, 0, -0.25, 0.0)
    glTranslatef(3.6, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayJ * 360, 0.0, 1.0, 0.0)
    glRotatef(75, 3.0, 2.0, 0.0)
    glutSolidSphere(0.4, 20, 16)
    glPopMatrix()
    glPopMatrix()


def Saturn(t):
    glPopMatrix()
    glPushMatrix()
    year_periodS = 29.46 * 8
    yearS = t / year_periodS
    glRotatef(yearS * 360.0, 0, 1, 0)
    Orbit(4.5, 0, -0.25, 0.0)
    glTranslatef(4.5, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(170, 1.0, 2.0, 4.0)
    glColor3f(1, 0.8, 0.4)
    gluDisk(gluNewQuadric(), 0.4, 0.5, 60, 4)
    glutSolidSphere(0.3, 20, 16)
    glPopMatrix()
    glPopMatrix()


def Uranus(t):
    glPopMatrix()
    glPushMatrix()
    year_periodU = 84.02 * 8
    yearU = t / year_periodU
    dayU = 687 * yearU
    glRotatef(yearU * 360.0, 0, 1, 0)
    Orbit(5.4, 0, -0.25, 0.0)
    glTranslatef(5.4, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayU * 360, 0.0, 1.0, 0.0)
    glRotatef(50, 1, 2.0, 1)
    glColor3f(0.4, 1, 0.8)
    glutSolidSphere(0.2, 10, 8)
    glPopMatrix()
    glPopMatrix()


def Neptune(t):
    glPopMatrix()
    glPushMatrix()
    year_periodN = 164.79 * 8
    yearN = t / year_periodN
    dayN = 687 * yearN
    glRotatef(yearN * 360.0, 0, 1, 0)
    Orbit(6, 0, -0.25, 0.0)
    glTranslatef(6, -0.25, 0.0)
    glPushMatrix()
    glPushMatrix()
    glRotatef(dayN * 360, 0.0, 1.0, 0.0)
    glRotatef(70, 1, 2.0, 1)
    glColor3f(0.1, 0.9, 1)
    glutSolidSphere(0.2, 20, 40)
    glPopMatrix()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    t = time.time() - start_time
    Star()
    glPushMatrix()
    glColor4f(1.0, 1.0, 0, 1)
    glutSolidSphere(1, 28, 16)
    Earth_System(t)
    Mercury(t)
    Venus(t)
    Mars(t)
    Jupiter(t)
    Saturn(t)
    Uranus(t)
    Neptune(t)
    glPopMatrix()
    glutSwapBuffers()


def Reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, w / h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 2.0, 5.0, 0.0, -3.5, 0.0, 0.0, 2.0, 0.0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1500, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Solar System")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(Reshape)
    glutMainLoop()


main()
