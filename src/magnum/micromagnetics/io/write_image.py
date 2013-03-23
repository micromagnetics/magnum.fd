# Copyright 2012, 2013 by the Micromagnum authors.
#
# This file is part of MicroMagnum.
# 
# MicroMagnum is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# MicroMagnum is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MicroMagnum.  If not, see <http://www.gnu.org/licenses/>.

from .io_tools import try_io_operation

try:
  import numpy, Image
except ImportError:
  def writeImage(filename, field, map_fn = id, color_fn = "black-white", color_range = (None, None)):
    raise NotImplementedError("writeImage: need 'numpy' and 'Image' libraries to work")
else:

  def map_field_to_array(field, map_fn, scale_from_range = (None, None)):
    nn = field.mesh.num_nodes
    arr = numpy.zeros((nn[0], nn[1]))
  
    # map field to numpy array
    for x, y, z in field.mesh.iterateCellIndices():
      if z != 0: break
      arr[x,y] = map_fn(field.get(x,y,z))
  
    # scale from range
    s0 = scale_from_range[0] or numpy.min(arr)
    s1 = scale_from_range[1] or numpy.max(arr)
    arr -= s0
    if s0 != s1: arr /= (s1-s0)
    arr.clip(0.0, 1.0, arr)
    return arr
  
  def map_array_to_image(arr, color_fn):
    nx, ny = arr.shape
    img = Image.new("RGB", (nx, ny))
    for y in range(ny):
      for x in range(nx):
        col = color_fn(arr[x,y])
        r, g, b = int(256*col[0]), int(256*col[1]), int(256*col[2])
        img.putpixel((x,y), (r,g,b))
    return img
  
  def exportImage(field, map_fn, color_fn, scale_from_range = (None, None)):
    arr = map_field_to_array(field, map_fn, scale_from_range)
    img = map_array_to_image(arr, color_fn)
    return img
  
  def writeImage(filename, field, map_fn = id, color_fn = "black-white", color_range = (None, None)):
    from math import atan2, sqrt

    map_fns = {
      'x': lambda val: val[0],
      'y': lambda val: val[1],
      'z': lambda val: val[2],
      'xy-angle': lambda val: atan2(val[1], val[0]),
      'xz-angle': lambda val: atan2(val[2], val[0]),
      'yz-angle': lambda val: atan2(val[2], val[1]),
      'mag': lambda val: sqrt(val[0]**2 + val[1]**2 + val[2]**2),
    }
    
    color_fns = {
      'black-white': lambda i: (i,i,i),
      'white-black': lambda i: (1.0-i,1.0-i,1.0-i),
    }
  
    if isinstance(color_fn, str): color_fn = color_fns[color_fn]
    if isinstance(map_fn, str): map_fn = map_fns[map_fn]
  
    img = exportImage(field, map_fn, color_fn, color_range)
    try_io_operation(lambda: img.save(filename))