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

## solver for micromagnetics
from magnum.micromagnetics.create_solver import create_solver

## constants
from magnum.micromagnetics.constants import MU0, H_BAR, ELECTRON_CHARGE, MU_BOHR, GYROMAGNETIC_RATIO, BOLTZMANN_CONSTANT

## modules
from magnum.micromagnetics.landau_lifshitz_gilbert import LandauLifshitzGilbert
from magnum.micromagnetics.exchange_field import ExchangeField
from magnum.micromagnetics.stray_field import StrayField, StrayFieldCalculator
from magnum.micromagnetics.anisotropy_field import AnisotropyField
from magnum.micromagnetics.external_field import AlternatingExternalField, StaticExternalField, ExternalField
from magnum.micromagnetics.spin_torque import SpinTorque
from magnum.micromagnetics.macro_spin_torque import MacroSpinTorque
from magnum.micromagnetics.current import AlternatingCurrent, StaticCurrent
from magnum.micromagnetics.alternating_field import AlternatingField
from magnum.micromagnetics.static_field import StaticField

__all__ = [
    "create_solver",
    "MU0", "H_BAR", "ELECTRON_CHARGE", "MU_BOHR", "GYROMAGNETIC_RATIO", "BOLTZMANN_CONSTANT",

    "LandauLifshitzGilbert",
    "ExchangeField",
    "StrayField", "StrayFieldCalculator",
    "AnisotropyField",
    "AlternatingExternalField", "StaticExternalField", "ExternalField",
    "SpinTorque", "MacroSpinTorque",
    "AlternatingCurrent", "StaticCurrent",
    "AlternatingField",
    "StaticField"
]
