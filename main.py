#!/usr/bin/env python

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

def init():
	glutInit(len(sys.argv), sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
	glutInitWindowSize(800, 600);
	win_id = glutCreateWindow('Dynamic Skybox')
	glutDisplayFunc(draw)
	glutMotionFunc(mouse_drag)
	glutKeyboardFunc(keyboard)
	glutMouseFunc(mouse_press)
	glutMainLoop()
	
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity();
	
	glFlush();
	glutSwapBuffers();
	
def mouse_drag(x, y):
	print "mouse_drag"
	
def mouse_press(button, state, x, y):
	print "mouse press"
	
def keyboard(key, x, y):
	print "keyboard"
	
def main():
	print "Initializing OpenGL..."
	init()
	
if __name__ == "__main__":
	main()
