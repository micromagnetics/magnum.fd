#!/usr/bin/python
from magnum import *
from magnum.config import cfg

import unittest

from my_testcase import MyTestCase
from helpers import *

class StrayFieldTest(MyTestCase):

  def doTest(self, M_file, H_file, epsilon):
    # load ref
    M     = readOMF(M_file)
    H_ref = readOMF(H_file)
    H     = VectorField(H_ref.mesh)

    # setup
    stray = StrayFieldCalculator(M.mesh)
    H.fill((1.0, 2.0, 3.0))
    
    # calculate
    for t in range(1):
      stray.calculate(M, H)

    # compare
    self.assertVectorFieldEqual(H_ref, H, epsilon)

  #@unittest.skipIf(cfg.skip_long_tests, "skipping StrayFieldTest.calculate_2d (long test)")
  #def test_calculate_2d(self):
  #  self.doTest("ref/M1.omf", "ref/H1_stray.omf", 1e0);

  #@unittest.skipIf(cfg.skip_long_tests, "skipping StrayFieldTest.calculate_3d (long test)")
  #def test_calculate_3d(self):
  #  self.doTest("ref/M3.omf", "ref/H3_stray.ohf", 5e1)

  def test_rotated_magnetization_produces_same_rotated_strayfield(self):

    def compute(M, rotations=1):
      for _ in range(rotations): M = right_rotate_vector_field(M)
      H = VectorField(M.mesh)
      stray = StrayFieldCalculator(M.mesh)
      stray.calculate(M, H)
      for _ in range(rotations): H = left_rotate_vector_field(H)
      return H

    #mesh = RectangularMesh((32,16,8), (1e-9,1e-9,1e-9), "z", 20)
    mesh = RectangularMesh((20, 20, 6), (5e-9, 5e-9, 5e-9), "xy", 20)
    M0 = VectorField(mesh); M0.randomize(); M0.scale(8e5)
    H0 = compute(M0, 0)
    H1 = compute(M0, 1)
    H2 = compute(M0, 2)

    self.assertVectorFieldEqual(H0, H1, 1e0)
    self.assertVectorFieldEqual(H0, H2, 1e0)

# start tests
import os
if __name__ == '__main__':
  os.chdir("..")
  unittest.main()
