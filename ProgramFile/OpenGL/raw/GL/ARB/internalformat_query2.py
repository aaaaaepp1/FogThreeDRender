'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_internalformat_query2'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_internalformat_query2',error_checker=_errors._error_checker)
GL_AUTO_GENERATE_MIPMAP=_C('GL_AUTO_GENERATE_MIPMAP',0x8295)
GL_CAVEAT_SUPPORT=_C('GL_CAVEAT_SUPPORT',0x82B8)
GL_CLEAR_BUFFER=_C('GL_CLEAR_BUFFER',0x82B4)
GL_COLOR_COMPONENTS=_C('GL_COLOR_COMPONENTS',0x8283)
GL_COLOR_ENCODING=_C('GL_COLOR_ENCODING',0x8296)
GL_COLOR_RENDERABLE=_C('GL_COLOR_RENDERABLE',0x8286)
GL_COMPUTE_TEXTURE=_C('GL_COMPUTE_TEXTURE',0x82A0)
GL_DEPTH_COMPONENTS=_C('GL_DEPTH_COMPONENTS',0x8284)
GL_DEPTH_RENDERABLE=_C('GL_DEPTH_RENDERABLE',0x8287)
GL_FILTER=_C('GL_FILTER',0x829A)
GL_FRAGMENT_TEXTURE=_C('GL_FRAGMENT_TEXTURE',0x829F)
GL_FRAMEBUFFER_BLEND=_C('GL_FRAMEBUFFER_BLEND',0x828B)
GL_FRAMEBUFFER_RENDERABLE=_C('GL_FRAMEBUFFER_RENDERABLE',0x8289)
GL_FRAMEBUFFER_RENDERABLE_LAYERED=_C('GL_FRAMEBUFFER_RENDERABLE_LAYERED',0x828A)
GL_FULL_SUPPORT=_C('GL_FULL_SUPPORT',0x82B7)
GL_GEOMETRY_TEXTURE=_C('GL_GEOMETRY_TEXTURE',0x829E)
GL_GET_TEXTURE_IMAGE_FORMAT=_C('GL_GET_TEXTURE_IMAGE_FORMAT',0x8291)
GL_GET_TEXTURE_IMAGE_TYPE=_C('GL_GET_TEXTURE_IMAGE_TYPE',0x8292)
GL_IMAGE_CLASS_10_10_10_2=_C('GL_IMAGE_CLASS_10_10_10_2',0x82C3)
GL_IMAGE_CLASS_11_11_10=_C('GL_IMAGE_CLASS_11_11_10',0x82C2)
GL_IMAGE_CLASS_1_X_16=_C('GL_IMAGE_CLASS_1_X_16',0x82BE)
GL_IMAGE_CLASS_1_X_32=_C('GL_IMAGE_CLASS_1_X_32',0x82BB)
GL_IMAGE_CLASS_1_X_8=_C('GL_IMAGE_CLASS_1_X_8',0x82C1)
GL_IMAGE_CLASS_2_X_16=_C('GL_IMAGE_CLASS_2_X_16',0x82BD)
GL_IMAGE_CLASS_2_X_32=_C('GL_IMAGE_CLASS_2_X_32',0x82BA)
GL_IMAGE_CLASS_2_X_8=_C('GL_IMAGE_CLASS_2_X_8',0x82C0)
GL_IMAGE_CLASS_4_X_16=_C('GL_IMAGE_CLASS_4_X_16',0x82BC)
GL_IMAGE_CLASS_4_X_32=_C('GL_IMAGE_CLASS_4_X_32',0x82B9)
GL_IMAGE_CLASS_4_X_8=_C('GL_IMAGE_CLASS_4_X_8',0x82BF)
GL_IMAGE_COMPATIBILITY_CLASS=_C('GL_IMAGE_COMPATIBILITY_CLASS',0x82A8)
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE=_C('GL_IMAGE_FORMAT_COMPATIBILITY_TYPE',0x90C7)
GL_IMAGE_PIXEL_FORMAT=_C('GL_IMAGE_PIXEL_FORMAT',0x82A9)
GL_IMAGE_PIXEL_TYPE=_C('GL_IMAGE_PIXEL_TYPE',0x82AA)
GL_IMAGE_TEXEL_SIZE=_C('GL_IMAGE_TEXEL_SIZE',0x82A7)
GL_INTERNALFORMAT_ALPHA_SIZE=_C('GL_INTERNALFORMAT_ALPHA_SIZE',0x8274)
GL_INTERNALFORMAT_ALPHA_TYPE=_C('GL_INTERNALFORMAT_ALPHA_TYPE',0x827B)
GL_INTERNALFORMAT_BLUE_SIZE=_C('GL_INTERNALFORMAT_BLUE_SIZE',0x8273)
GL_INTERNALFORMAT_BLUE_TYPE=_C('GL_INTERNALFORMAT_BLUE_TYPE',0x827A)
GL_INTERNALFORMAT_DEPTH_SIZE=_C('GL_INTERNALFORMAT_DEPTH_SIZE',0x8275)
GL_INTERNALFORMAT_DEPTH_TYPE=_C('GL_INTERNALFORMAT_DEPTH_TYPE',0x827C)
GL_INTERNALFORMAT_GREEN_SIZE=_C('GL_INTERNALFORMAT_GREEN_SIZE',0x8272)
GL_INTERNALFORMAT_GREEN_TYPE=_C('GL_INTERNALFORMAT_GREEN_TYPE',0x8279)
GL_INTERNALFORMAT_PREFERRED=_C('GL_INTERNALFORMAT_PREFERRED',0x8270)
GL_INTERNALFORMAT_RED_SIZE=_C('GL_INTERNALFORMAT_RED_SIZE',0x8271)
GL_INTERNALFORMAT_RED_TYPE=_C('GL_INTERNALFORMAT_RED_TYPE',0x8278)
GL_INTERNALFORMAT_SHARED_SIZE=_C('GL_INTERNALFORMAT_SHARED_SIZE',0x8277)
GL_INTERNALFORMAT_STENCIL_SIZE=_C('GL_INTERNALFORMAT_STENCIL_SIZE',0x8276)
GL_INTERNALFORMAT_STENCIL_TYPE=_C('GL_INTERNALFORMAT_STENCIL_TYPE',0x827D)
GL_INTERNALFORMAT_SUPPORTED=_C('GL_INTERNALFORMAT_SUPPORTED',0x826F)
GL_MANUAL_GENERATE_MIPMAP=_C('GL_MANUAL_GENERATE_MIPMAP',0x8294)
GL_MAX_COMBINED_DIMENSIONS=_C('GL_MAX_COMBINED_DIMENSIONS',0x8282)
GL_MAX_DEPTH=_C('GL_MAX_DEPTH',0x8280)
GL_MAX_HEIGHT=_C('GL_MAX_HEIGHT',0x827F)
GL_MAX_LAYERS=_C('GL_MAX_LAYERS',0x8281)
GL_MAX_WIDTH=_C('GL_MAX_WIDTH',0x827E)
GL_MIPMAP=_C('GL_MIPMAP',0x8293)
GL_NUM_SAMPLE_COUNTS=_C('GL_NUM_SAMPLE_COUNTS',0x9380)
GL_READ_PIXELS=_C('GL_READ_PIXELS',0x828C)
GL_READ_PIXELS_FORMAT=_C('GL_READ_PIXELS_FORMAT',0x828D)
GL_READ_PIXELS_TYPE=_C('GL_READ_PIXELS_TYPE',0x828E)
GL_RENDERBUFFER=_C('GL_RENDERBUFFER',0x8D41)
GL_SAMPLES=_C('GL_SAMPLES',0x80A9)
GL_SHADER_IMAGE_ATOMIC=_C('GL_SHADER_IMAGE_ATOMIC',0x82A6)
GL_SHADER_IMAGE_LOAD=_C('GL_SHADER_IMAGE_LOAD',0x82A4)
GL_SHADER_IMAGE_STORE=_C('GL_SHADER_IMAGE_STORE',0x82A5)
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST=_C('GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST',0x82AC)
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE=_C('GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE',0x82AE)
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST=_C('GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST',0x82AD)
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE=_C('GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE',0x82AF)
GL_SRGB_DECODE_ARB=_C('GL_SRGB_DECODE_ARB',0x8299)
GL_SRGB_READ=_C('GL_SRGB_READ',0x8297)
GL_SRGB_WRITE=_C('GL_SRGB_WRITE',0x8298)
GL_STENCIL_COMPONENTS=_C('GL_STENCIL_COMPONENTS',0x8285)
GL_STENCIL_RENDERABLE=_C('GL_STENCIL_RENDERABLE',0x8288)
GL_TESS_CONTROL_TEXTURE=_C('GL_TESS_CONTROL_TEXTURE',0x829C)
GL_TESS_EVALUATION_TEXTURE=_C('GL_TESS_EVALUATION_TEXTURE',0x829D)
GL_TEXTURE_1D=_C('GL_TEXTURE_1D',0x0DE0)
GL_TEXTURE_1D_ARRAY=_C('GL_TEXTURE_1D_ARRAY',0x8C18)
GL_TEXTURE_2D=_C('GL_TEXTURE_2D',0x0DE1)
GL_TEXTURE_2D_ARRAY=_C('GL_TEXTURE_2D_ARRAY',0x8C1A)
GL_TEXTURE_2D_MULTISAMPLE=_C('GL_TEXTURE_2D_MULTISAMPLE',0x9100)
GL_TEXTURE_2D_MULTISAMPLE_ARRAY=_C('GL_TEXTURE_2D_MULTISAMPLE_ARRAY',0x9102)
GL_TEXTURE_3D=_C('GL_TEXTURE_3D',0x806F)
GL_TEXTURE_BUFFER=_C('GL_TEXTURE_BUFFER',0x8C2A)
GL_TEXTURE_COMPRESSED=_C('GL_TEXTURE_COMPRESSED',0x86A1)
GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT=_C('GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT',0x82B2)
GL_TEXTURE_COMPRESSED_BLOCK_SIZE=_C('GL_TEXTURE_COMPRESSED_BLOCK_SIZE',0x82B3)
GL_TEXTURE_COMPRESSED_BLOCK_WIDTH=_C('GL_TEXTURE_COMPRESSED_BLOCK_WIDTH',0x82B1)
GL_TEXTURE_CUBE_MAP=_C('GL_TEXTURE_CUBE_MAP',0x8513)
GL_TEXTURE_CUBE_MAP_ARRAY=_C('GL_TEXTURE_CUBE_MAP_ARRAY',0x9009)
GL_TEXTURE_GATHER=_C('GL_TEXTURE_GATHER',0x82A2)
GL_TEXTURE_GATHER_SHADOW=_C('GL_TEXTURE_GATHER_SHADOW',0x82A3)
GL_TEXTURE_IMAGE_FORMAT=_C('GL_TEXTURE_IMAGE_FORMAT',0x828F)
GL_TEXTURE_IMAGE_TYPE=_C('GL_TEXTURE_IMAGE_TYPE',0x8290)
GL_TEXTURE_RECTANGLE=_C('GL_TEXTURE_RECTANGLE',0x84F5)
GL_TEXTURE_SHADOW=_C('GL_TEXTURE_SHADOW',0x82A1)
GL_TEXTURE_VIEW=_C('GL_TEXTURE_VIEW',0x82B5)
GL_VERTEX_TEXTURE=_C('GL_VERTEX_TEXTURE',0x829B)
GL_VIEW_CLASS_128_BITS=_C('GL_VIEW_CLASS_128_BITS',0x82C4)
GL_VIEW_CLASS_16_BITS=_C('GL_VIEW_CLASS_16_BITS',0x82CA)
GL_VIEW_CLASS_24_BITS=_C('GL_VIEW_CLASS_24_BITS',0x82C9)
GL_VIEW_CLASS_32_BITS=_C('GL_VIEW_CLASS_32_BITS',0x82C8)
GL_VIEW_CLASS_48_BITS=_C('GL_VIEW_CLASS_48_BITS',0x82C7)
GL_VIEW_CLASS_64_BITS=_C('GL_VIEW_CLASS_64_BITS',0x82C6)
GL_VIEW_CLASS_8_BITS=_C('GL_VIEW_CLASS_8_BITS',0x82CB)
GL_VIEW_CLASS_96_BITS=_C('GL_VIEW_CLASS_96_BITS',0x82C5)
GL_VIEW_CLASS_BPTC_FLOAT=_C('GL_VIEW_CLASS_BPTC_FLOAT',0x82D3)
GL_VIEW_CLASS_BPTC_UNORM=_C('GL_VIEW_CLASS_BPTC_UNORM',0x82D2)
GL_VIEW_CLASS_RGTC1_RED=_C('GL_VIEW_CLASS_RGTC1_RED',0x82D0)
GL_VIEW_CLASS_RGTC2_RG=_C('GL_VIEW_CLASS_RGTC2_RG',0x82D1)
GL_VIEW_CLASS_S3TC_DXT1_RGB=_C('GL_VIEW_CLASS_S3TC_DXT1_RGB',0x82CC)
GL_VIEW_CLASS_S3TC_DXT1_RGBA=_C('GL_VIEW_CLASS_S3TC_DXT1_RGBA',0x82CD)
GL_VIEW_CLASS_S3TC_DXT3_RGBA=_C('GL_VIEW_CLASS_S3TC_DXT3_RGBA',0x82CE)
GL_VIEW_CLASS_S3TC_DXT5_RGBA=_C('GL_VIEW_CLASS_S3TC_DXT5_RGBA',0x82CF)
GL_VIEW_COMPATIBILITY_CLASS=_C('GL_VIEW_COMPATIBILITY_CLASS',0x82B6)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLint64Array)
def glGetInternalformati64v(target,internalformat,pname,bufSize,params):pass
