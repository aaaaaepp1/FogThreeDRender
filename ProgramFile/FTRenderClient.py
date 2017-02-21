#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib
import time
import socket
from contextlib import closing

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True
DEBUG = False
FULL_SCREEN = False

__author__ = 'Naoki Okamoto'
__version__ = '0.1.0'
__date__ = '2017/02/18'

#3Dオブジェクト（ポリゴンの集合）を表す単語に、objectとmodelが混在している

class Time(object):
	def __init__(self):
		self._marked = time.time()

		return

	def mark_time(self):
		self._marked = time.time()

		return

	def delta_time(self):
		result = time.time() - self._marked
		self.mark_time()
		return result

	def time(self):
		return time.time()

class ClientMessageControl(object):
	"""Control object for SendinMessage"""

	def __init__(self, super_host, port, buffer_size):
		"""constructor for this class"""
		if TRACE: print_doc(__name__, self)
		self._super_host_ip = super_host
		self._port = port
		self._buffer_size = buffer_size
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		return

	def start(self):
		"""this is the method to recieve the message"""
		if TRACE: print_doc(__name__, self)
		with closing(self._sock):
			self._sock.bind((self._super_host_ip, self._port))
			
			a_model = FTRenderModel(self)
			a_3Dmodel = FTRenderModelObj()
			a_3Dmodel.loadObjModel('models' + os.sep + 'monkey.obj')
			a_3Dmodel.rgb(1.0, 0.8, 0.8)
			a_model.add_3d_models(a_3Dmodel)
			# a_model.add_motion(None, [0.0, 2.0, 10.0], 5, 'ease_in_out_Cubic')
			# a_model.add_motion(None, [50.0, 0.0, 0.0], 1, 'ease_out_Cubic')
			# a_model.add_motion(None, [-100.0, 0.0, 0.0], 2, 'ease_out_Cubic')
			# a_model.add_motion(None, [50.0, 0.0, 0.0], 3, 'ease_out_Cubic')
			a_model.open()

			self._model = a_model

		return

	def wait_commands(self):
		while True:
			recieved_message = self._sock.recv(self._buffer_size)
			if self.manage_(recieved_message): break

		return

	def manage_(line):
		"""受信した文字列を解析する"""
		if TRACE: print_doc(__name__, self)
		if line == 'exit_0': 
			sys.exit(0)
		elif line == 'push':
			return True
		elif self._move:
			lines = line.split(',')
			start_position = None if lines[1] == False else [float(lines[2]),float(lines[3]),float(lines[4])]
			end_position = [float(lines[5]),float(lines[6]),float(lines[7])]
			self._model.add_motion(start_position, end_position, int(float(line[8])), line[9])
		elif self._model:
			pass
		elif line == 'move': self._move = True
		elif line == 'model': self._model = True

		return False

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

class FTRenderModel(object):
	def __init__(self, a_client_message_control):
		if TRACE: print_doc(__name__, self)

		self._projection = Projection()
		self._models = []
		self._axes_scale = 1.0
		self._handle_object = 0

		view_class= self.default_view_class()
		self._view = view_class(self)
		self._controller = self._view._controller
		self._client_message_control = a_client_message_control

		return

	def add_3d_models(self, *model_objects):
		if TRACE: print_doc(__name__, self)


		for each in model_objects:
			self._models.append(each)

		return

	def default_controll_class(self):
		if TRACE: print_doc(__name__, self)


		return FTRenderControl

	def default_view_class(self):
		if TRACE: print_doc(__name__, self)


		return FTRenderView

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
		glutMainLoop()

		return

	def add_motion(self, start_position, end_position, ease_time, ease_type):
		"""handle_objectにモーションを追加する処理"""
		if TRACE: print_doc(__name__, self)
		self._controller.add_motion(start_position, end_position, ease_time, ease_type)
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
		return

	def idle(self):
		"""フレームごとのModelのidle処理、これがglutIdleFuncに入る"""
		if TRACE: print_doc(__name__, self)

		if sum([len(each) for each in [models._easing_list for models in self._models]]) == 0:
			self._client_message_control.wait_commands()

		self._controller.idle()
		glutPostRedisplay()

		return

class FTRenderView(object):

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
		self._controller = FTRenderControl(self)
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
		glutIdleFunc(self._model.idle)

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

class FTRenderControl(object):

	def __init__(self, a_view):
		if TRACE: print_doc(__name__, self)

		self._model = a_view._model
		self._view = a_view
		self._time = Time()

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

	def add_motion(self, start_position, end_position, ease_time, ease_type):
		"""対象の3Dモデルにモーションを追加"""
		if TRACE: print_doc(__name__, self)

		model = None
		if self._model._handle_object < len(self._model._models):
			model = self._model._models[self._model._handle_object]

		model.add_motion(start_position, end_position, ease_time, ease_type)

		return

	def idle(self):
		"""フレームごとのcontrol処理"""
		if TRACE: print_doc(__name__, self)
		model = None
		if self._model._handle_object < len(self._model._models):
			model = self._model._models[self._model._handle_object]

		if model != None: model.idle()

		return

class Easing(object):
	def __init__(self, a_object):
		self._time = Time()
		self._object = a_object
		self._end = False
		self._started = False
		return

	def is_end(self):
		return self._end

	def idle(self):
		"""イージング処理を行う"""
		if TRACE: print_doc(__name__, self)

		if self._started:
			progression = (self._time.time() - self._start_time) / self._ease_time
			easing_progression = 0.0
			if self._ease_type == 'ease_in_Quadratic':
				easing_progression = (lambda t, b, c: c*t*t + b)(progression, 0.0, 1.0)
			elif self._ease_type == 'ease_out_Quadratic':
				easing_progression = (lambda t, b, c: -c*t*(t-2.0) + b)(progression, 0.0, 1.0)
			elif self._ease_type == 'ease_in_out_Quadratic':
				easing_progression = (lambda t, b, c: c/2.0*t*t + b if t<1 else -c/2.0 * ((t-1)*((t-1)-2) - 1) + b)(progression*2.0, 0.0, 1.0)
			elif self._ease_type == 'ease_in_Cubic':
				easing_progression = (lambda t, b, c: c*t*t*t + b)(progression, 0.0, 1.0)
			elif self._ease_type == 'ease_out_Cubic':
				easing_progression = (lambda t, b, c: c*((t-1)*(t-1)*(t-1) + 1) + b)(progression, 0.0, 1.0)
			elif self._ease_type == 'ease_in_out_Cubic':
				easing_progression = (lambda t, b, c: c/2.0*t*t*t + b if t < 1 else c/2.0 * ((t-2)*(t-2)*(t-2) + 2) + b)(progression*2, 0.0, 1.0)
			else:
				easing_progression = (lambda t: t)(progression)


			
			list_plus = (lambda list1, list2: [i + j for i, j in zip(list1, list2)])
			list_diff = (lambda list1, list2: [i - j for i, j in zip(list1, list2)])
			
			a_current_delta = (lambda list_, i: [each * i for each in list_])(self._delta, easing_progression)
			self._object._position_x += a_current_delta[0] - self._last_delta[0]
			self._object._position_y += a_current_delta[1] - self._last_delta[1]
			self._object._position_z += a_current_delta[2] - self._last_delta[2]
			self._last_delta = a_current_delta

			if progression >= 1.0:
				self._end = True
				self._started = False
				return

		return

	def start(self, start_position, end_position, ease_time, ease_type):
		self._start_position = [self._object._position_x, self._object._position_y, self._object._position_z] if start_position == None else start_position
		if start_position != None: 
			self._object._position_x = start_position[0]
			self._object._position_y = start_position[1]
			self._object._position_z = start_position[2]
		self._last_position = self._start_position
		self._end_position = end_position
		self._ease_time = ease_time
		self._ease_type = ease_type
		self._delta = (lambda list1, list2: [i + j for i, j in zip(list1, list2)])(self._end_position, self._start_position)
		self._time.mark_time()
		self._last_delta = [0.0, 0.0, 0.0]
		self._start_time = self._time._marked
		self._started = True

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

		self._easing_list = []

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

	def default_easing_class(self):
		return Easing

	def idle(self):
		"""各モデルの制御を行う"""
		if TRACE: print_doc(__name__, self)

		for (i, each) in enumerate(self._easing_list): 
			each.idle()
			if each.is_end(): del self._easing_list[i]  
		return

	def add_motion(self, start_position, end_position, ease_time, ease_type):

		easing = Easing(self)
		easing.start(start_position, end_position, ease_time, ease_type)
		self._easing_list.append(easing)
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

class FTRenderModelObj(OpenGL3DModel):

	def __init__(self):
		if TRACE: print_doc(__name__, self)


		super(FTRenderModelObj, self).__init__()
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
					super(FTRenderModelObj, self).name(a_moments[1])
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
	# a_model = FTRenderModel()
	# a_3Dmodel = FTRenderModelObj()
	# a_3Dmodel.loadObjModel('models' + os.sep + 'monkey.obj')
	# a_3Dmodel.rgb(1.0, 0.8, 0.8)
	# a_model.add_3d_models(a_3Dmodel)
	# a_model.add_motion(None, [0.0, 2.0, 10.0], 5, 'ease_in_out_Cubic')
	# a_model.add_motion(None, [50.0, 0.0, 0.0], 1, 'ease_out_Cubic')
	# a_model.add_motion(None, [-100.0, 0.0, 0.0], 2, 'ease_out_Cubic')
	# a_model.add_motion(None, [50.0, 0.0, 0.0], 3, 'ease_out_Cubic')
	# a_model.open()

	client = ClientMessageControl("192.168.10.110", 4000, 4048)
	client.start()

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