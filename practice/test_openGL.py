#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True
DEBUG = True
FULL_SCREEN = False

__author__ = 'Naoki Okamoto'
__version__ = '0.1.0'
__date__ = '2017/02/18'


class Projection(object):

	def __init__(self):
		"""OpenGLプロジェクションのコンストラクタ。"""
		if TRACE: print_doc(__name__, self)

		self._eye_point   = self._default_eye_point   = None
		self._sight_point = self._default_sight_point = None
		self._up_vector   = self._default_up_vector   = None
		self._fovy        = self._default_fovy        = None
		self._near        = self._default_near        = None
		self._far         = self._default_far         = None

		self.eye_point_([0.0 , 3.5 , 16])
		self.sight_point_([0.0 , 0.0 , 0.0])
		self.up_vector_([0.0 , 1.0 , 0.0])
		self.fovy_(50)

		return

	def eye_point(self):
		"""視点を応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._eye_point == None: self.eye_point_([0.0, 0.0, 10.0])
		return self._eye_point

	def eye_point_(self, a_point):
		"""視点を設定する。"""
		if TRACE: print_doc(__name__, self)

		self._eye_point = a_point
		if self._default_eye_point == None: self._default_eye_point = a_point

		return

	def sight_point(self):
		"""注視点を応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._sight_point == None: self.sight_point_([0.0, 0.0, 0.0])
		return self._sight_point

	def sight_point_(self, a_point):
		"""注視点を設定する。"""
		if TRACE: print_doc(__name__, self)

		self._sight_point = a_point
		if self._default_sight_point == None: self._default_sight_point = a_point

		return

	def up_vector(self):
		"""上方向ベクトルを応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._up_vector == None: self.up_vector_([0.0, 1.0, 0.0])
		return self._up_vector

	def up_vector_(self, a_point):
		"""上方向ベクトルを設定する。"""
		if TRACE: print_doc(__name__, self)

		self._up_vector = a_point
		if self._default_up_vector == None: self._default_up_vector = a_point

		return

	def fovy(self):
		"""視界角を応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._fovy == None: self.fovy_(30.0)
		return self._fovy

	def fovy_(self, a_float):
		"""視界角を設定する。"""
		if TRACE: print_doc(__name__, self)

		self._fovy = a_float
		if self._default_fovy == None: self._default_fovy = a_float

		return

	def near(self):
		"""近を応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._near == None: self.near_(0.01)
		return self._near

	def near_(self, a_float):
		"""近を設定する。"""
		if TRACE: print_doc(__name__, self)

		self._near = a_float
		if self._default_near == None: self._default_near = a_float

		return

	def far(self):
		"""遠を応答する。"""
		if TRACE: print_doc(__name__, self)

		if self._far == None: self.far_(100)
		return self._far

	def far_(self, a_float):
		"""遠を設定する。"""
		if TRACE: print_doc(__name__, self)

		self._far = a_float
		if self._default_far == None: self._default_far = a_float

		return

	def reset(self):
		"""プロジェクション情報をデフォルト(最初に設定されたパラメータ)に設定し直す。"""
		if TRACE: print_doc(__name__, self)

		if self._default_eye_point != None:
			self._eye_point = self._default_eye_point

		if self._default_fovy != None:
			self._fovy = self._default_fovy

		return


class Model(object):
	def __init__(self):
		if TRACE: print_doc(__name__, self)

		self._projection = Projection()
		self._models = []
		self._axes_scale = 1.0
		self._handle_object = 0

		return

	def add_3d_models(self, *model_objects):
		if TRACE: print_doc(__name__, self)


		for each in model_objects:
			self._models.append(each)

		return

	def default_controll_class(self):
		if TRACE: print_doc(__name__, self)


		return Control

	def default_view_class(self):
		if TRACE: print_doc(__name__, self)


		return View

	def default_window_title(self):
		if TRACE: print_doc(__name__, self)


		return "Fog 3D Render"

	def change_handle_object(self):
		"""制御するモデルを切り替える"""
		if TRACE: print_doc(__name__, self)

		if self._handle_object+1 >= len(self._models):
			self._handle_object = 0
		else:
			self._handle_object += 1

	def open(self):
		if TRACE: print_doc(__name__, self)

		view_class= self.default_view_class()
		self._view = view_class(self)
		glutMainLoop()

		return

	def rendering(self, a_handle_object):
		"""move_number番目のモデルだけ回転を施し、全ての3Dモデルをレンダリングする。"""
		if TRACE: print_doc(__name__, self)

		for (i, each) in enumerate(self._models):
			# glScale(each._model_scale, each._model_scale, each._model_scale)
			glTranslated(each._position_x, each._position_y, each._position_z)
			if(i != a_handle_object):
				each.rendering()
			# glScale(1/each._model_scale, 1/each._model_scale, 1/each._model_scale)
			glTranslated(-1*each._position_x, -1*each._position_y, -1*each._position_z)

		model = self._models[a_handle_object]
		glTranslated(model._position_x, model._position_y, model._position_z)
		model.rendering()
		glTranslated(-1*model._position_x, -1*model._position_y, -1*model._position_z)

		#self._marker._position_x = model._position_x
		#self._marker._position_z = model._position_z
		#glTranslated(self._marker._position_x, self._marker._position_y, self._marker._position_z)
		#self._marker.rendering()

		return


class View(object):

	window_position = [0, 0]

	@classmethod
	def get_window_position(a_class):
		if TRACE: print_doc(__name__, self)


		current_position = a_class.window_position
		a_class.window_position = map((lambda value: value + 30), a_class.window_position)

		return current_position


	def __init__(self, a_model):
		if TRACE: print_doc(__name__, self)

		self._model = a_model
		self._controller = Control(self)
		self._angle_x = 0.0
		self._angle_y = 0.0
		self._angle_z = 0.0
		self._width = 400
		self._height = 400

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		
		if FULL_SCREEN:
			glutGameModeString("width>=1280 height>=1080 bpp=32 hertz>=60")
			glutEnterGameMode()
		else:
			glutInitWindowPosition(100, 100)
			glutInitWindowSize(self._width, self._height);
			glutCreateWindow("FogThreeDRender")

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self._controller.keyboard)
		glutMouseFunc(self._controller.mouse)
		glutMotionFunc(self._controller.motion)
		glutWMCloseFunc(self._controller.close)

		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		glEnable(GL_NORMALIZE)

		return

	def display(self):
		if TRACE: print_doc(__name__, self)


		projection = self._model._projection
		eye_point = projection.eye_point()
		sight_point = projection.sight_point()
		up_vector = projection.up_vector()
		fovy = projection.fovy()
		near = projection.near()
		far = projection.far()

		aspect = float(self._width) / float(self._height)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(fovy, aspect, near, far)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(eye_point[0], eye_point[1], eye_point[2],
				  sight_point[0], sight_point[1], sight_point[2],
				  up_vector[0], up_vector[1], up_vector[2])

		glClearColor(1.0, 1.0, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glEnable(GL_LIGHTING)
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
		glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, 0.0)
		glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1.0)
		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 1.0, 0.0])
		glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0.0, 0.0, -1.0])
		glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 90.0)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)

		glRotated(self._angle_x, 1.0, 0.0, 0.0)
		glRotated(self._angle_y, 0.0, 1.0, 0.0)
		glRotated(self._angle_z, 0.0, 0.0, 1.0)
		#self.display_axes()

		self._model.rendering(self._model._handle_object)

		glutSwapBuffers()

		return

	def display_axes(self):
		"""世界座標系を描画する。"""
		if TRACE: print_doc(__name__, self)

		axes_scale = self._model._axes_scale
		scaled_by_n = (lambda vertex: map((lambda value: value * axes_scale), vertex))
		glBegin(GL_LINES)
		glColor([ 1.0, 0.0, 0.0, 1.0 ])
		glVertex(scaled_by_n([-1.0, 0.0, 0.0 ]))
		glVertex(scaled_by_n([ 1.0, 0.0, 0.0 ]))
		glColor([ 0.0, 1.0, 0.0, 1.0 ])
		glVertex(scaled_by_n([ 0.0,-1.0, 0.0 ]))
		glVertex(scaled_by_n([ 0.0, 1.0, 0.0 ]))
		glColor([ 0.0, 0.0, 1.0, 1.0 ])
		glVertex(scaled_by_n([ 0.0, 0.0,-1.0 ]))
		glVertex(scaled_by_n([ 0.0, 0.0, 1.0 ]))
		glEnd()

		return

	def reshape(self, width, height):
		if TRACE: print_doc(__name__, self)

		self._width = width
		self._height = height

		glViewport(0, 0, width, height)

		return


class Control(object):

	def __init__(self, a_view):
		if TRACE: print_doc(__name__, self)

		self._model = a_view._model
		self._view = a_view

		return

	def close(self):
		if TRACE: print_doc(__name__, self)

		sys.exit(0)

		return

	def keyboard(self, key, x, y):
		"""3Dモデルの制御を行う"""
		if TRACE: print_doc(__name__, self)
		if DEBUG: print "key: {}, x: {}, y: {}".format(key, x, y)

		model = None
		if self._model._handle_object < len(self._model._models):
			model = self._model._models[self._model._handle_object]


		if key == "qQ\33" or key == 'q':
			self.close()
		elif key == 'x' and model != None:
			model._position_x += 0.1
		elif key == 'y' and model != None:
			model._position_y += 0.1
		elif key == 'z' and model != None:
			model._position_z += 0.1

		elif key == 'X' and model != None:
			model._position_x -= 0.1
		elif key == 'Y' and model != None:
			model._position_y -= 0.1
		elif key == 'Z' and model != None:
			model._position_z -= 0.1

		self._view.display()

		return

	def motion(self, x, y):
		if TRACE: print_doc(__name__, self)


		return

	def mouse(self, button, state, x, y):
		if TRACE: print_doc(__name__, self)


		return

	def move(x, y, z):

		model._position_x += x
		model._position_y += y
		model._position_z += z

		return

class OpenGL3DModel(object):

	def __init__(self):
		if TRACE: print_doc(__name__, self)


		self._display_object = []
		self._display_list = None
		self._view = None
		self._axes_scale = 1.0
		self._position_x = 0.0
		self._position_y = 0.0
		self._position_z = 0.0
		self._model_scale = 1.0
		self._init_position_x = 0.0
		self._init_position_y = 0.0
		self._init_position_z = 0.0

		return

	def display_list(self):
		if TRACE: print_doc(__name__, self)


		if self._display_list == None:
			self._display_list = glGenLists(1)
			glNewList(self._display_list, GL_COMPILE)
			glColor4d(1.0, 1.0, 1.0, 1.0)
			for index, each in enumerate(self._display_object):
				each.rendering()
			glEndList()

		return self._display_list

	def rendering(self):
		if TRACE: print_doc(__name__, self)

		glCallList(self.display_list())
		return

	def name(self, n):
		if TRACE: print_doc(__name__, self)


		self._name = n

		return



class OpenGLObject(object):

	def __init__(self):
		if TRACE: print_doc(__name__, self)


		self._rgb = [1.0, 1.0, 1.0]
		self._name = ''

		return

	def rendering(self):
		if TRACE: print_doc(__name__, self)


		glColor4d(self._rgb[0], self._rgb[1], self._rgb[2], 1.0)

		return

	def rgb(self, red, green, blue):
		if TRACE: print_doc(__name__, self)


		self._rgb = [red, green, blue]

		return


class OpenGLPolygon(OpenGLObject):

	def __init__(self, vertexes):
		if TRACE: print_doc(__name__, self)


		super(OpenGLPolygon, self).__init__()
		self._vertexes = vertexes

		x = 0.0
		y = 0.0
		z = 0.0
		length = len(vertexes)
		for i in range(0, length):
			j = (i + 1) % length
			k = (i + 2) % length
			ux, uy, uz = map((lambda each1, each2: each1 - each2), vertexes[j], vertexes[i])
			vx, vy, vz = map((lambda each1, each2: each1 - each2), vertexes[k], vertexes[j])
			x = x + (uy * vz - uz * vy)
			y = y + (uz * vx - ux * vz)
			z = z + (ux * vy - uy * vx)
		normal_vector = [x, y, z]
		distance = sum(map((lambda each: each * each), normal_vector)) ** 0.5
		self._normal_unit_vector = map((lambda vector: vector / distance), normal_vector)

		return

	def resize(self, size):
		if TRACE: print_doc(__name__, self)


		tmp_list = []
		for each1 in self._vertexes:
			tmp = []
			for each2 in each1:
				tmp.append(each2*size)
			tmp_list.append(tmp)

		self._vertexes = []
		for each in tmp_list:
			self._vertexes.append(each)

		return

	def rendering(self):
		if TRACE: print_doc(__name__, self)


		super(OpenGLPolygon, self).rendering()
		glBegin(GL_POLYGON)
		glNormal3fv(self._normal_unit_vector)
		for vertex in self._vertexes:
			glVertex3fv(vertex)
		glEnd()

		return

class ModelObj(OpenGL3DModel):

	def __init__(self):
		if TRACE: print_doc(__name__, self)


		super(ModelObj, self).__init__()
		self._model_scale = 1.0

		return

	def rgb(self, red, green, blue):
		if TRACE: print_doc(__name__, self)


		for each in self._display_object:
			each.rgb(red, green, blue)

		return

	def loadObjModel(self, path):
		if TRACE: print_doc(__name__, self)

		filename = os.path.join(os.getcwd(), path)
		
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			print 'error to file path'
			sys.exit(1)

		with open(filename, "rU") as a_file:
			collection_of_vertexes = []
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_moments = a_string.split(' ')
				if len(a_moments) == 0: continue
				index_to_vertex = (lambda index: collection_of_vertexes[index-1])
				if a_moments[0] == 'mtllib':
					super(ModelObj, self).name(a_moments[1])
				elif a_moments[0] == 'v':
					a_vertex = map(float, a_moments[1:4])
					collection_of_vertexes.append(a_vertex)
				elif a_moments[0] == 'vn':
					pass
				elif a_moments[0] == 'f':
					number_of_indexes = 4
					each_moments = [each.split('/')[0] for each in a_moments[1:number_of_indexes+1]]
					indexes = map(int, each_moments)
					vertexes = map(index_to_vertex, indexes)
					a_polygon = OpenGLPolygon(vertexes)
					self._display_object.append(a_polygon)
		return

def main():
	"""
	
	"""
	a_model = Model()
	a_3Dmodel = ModelObj()
	a_3Dmodel.loadObjModel('monkey.obj')
	a_3Dmodel.rgb(1.0, 0.0, 0.0)
	a_model.add_3d_models(a_3Dmodel)
	a_model.open()

	return

def print_doc(namespace, object):
	"""
	
	"""
	
	import inspect
	# method_name = inspect.currentframe().f_back.f_code.co_name
	method_name = inspect.stack(1)[1][0].f_code.co_name
	document_string = getattr(object, method_name).__doc__
	print('{0} [{1}] {2}'.format(namespace, method_name, document_string))

if __name__ == '__main__':
	sys.exit(main())