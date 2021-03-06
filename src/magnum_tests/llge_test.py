#!/usr/bin/python

# Copyright 2012-2014 by the MicroMagnum Team
# Copyright 2014 by the magnum.fd Team
#
# This file is part of magnum.fd.
# magnum.fd is based heavily on MicroMagnum.
# (https://github.com/MicroMagnum/MicroMagnum)
#
# magnum.fd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# magnum.fd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with magnum.fd. If not, see <http://www.gnu.org/licenses/>.

import unittest

from magnum import RectangularMesh, Field, VectorField
import magnum.magneto as magneto


class LLGETest(unittest.TestCase):

    def test_llge(self):
        mesh = RectangularMesh((10, 10, 10), (1e-9, 1e-9, 1e-9))
        f1, f2 = Field(mesh), Field(mesh)
        M, H, dM = VectorField(mesh), VectorField(mesh), VectorField(mesh)

        # dM = f1*MxH + f2*Mx(MxH)
        f1.fill(10)
        f2.fill(20)
        M.fill((5, 10, 15))
        H.fill((20, 25, 30))
        magneto.llge(f1, f2, M, H, dM)

        for idx in range(dM.size()):
            self.assertEqual(dM.get(idx), (-60750.0, -13500.0, 29250.0))

if __name__ == '__main__':
    unittest.main()
