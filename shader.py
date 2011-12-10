import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from ctypes import *

import sys


class Shader(object):
	def __init__(self, vertex_file, fragment_file):
		vertex_shader = self.compileShader(GL_VERTEX_SHADER, vertex_file)
		fragment_shader = self.compileShader(GL_FRAGMENT_SHADER, fragment_file)
		self.program = self.compileProgram(vertex_shader, fragment_shader)
		
	def compileShader(self, shader_type, shader_file):
		try:
			f = open(shader_file, 'r')
		except IOError:
			print "Could not open shader source file:", shader_file
			sys.exit(1)

		shader_src = f.read()
	
		shader = glCreateShader(shader_type)
		glShaderSource(shader, shader_src)
		glCompileShader(shader)
		self.printShaderLog(shader, shader_file)
		return shader
		
	def compileProgram(self, vertex_shader, fragment_shader):
		program = glCreateProgram()
		glAttachShader(program, vertex_shader)
		glAttachShader(program, fragment_shader)
		glLinkProgram(program)
		self.printProgramLog(program)
		return program
		
	def printShaderLog(self, shader, shader_file):
		text = glGetShaderInfoLog(shader)
		if text:
			print "Error compiling:", shader_file
			print text
			sys.exit(1)
			
	def printProgramLog(self, program):
		text = glGetProgramInfoLog(program)
		if text:
			print "Error linking shader program."
			print text
			sys.exit(1)
		
	def bind(self):
		glUseProgram(self.program)
		
	def release(self):
		glUseProgram(0)
