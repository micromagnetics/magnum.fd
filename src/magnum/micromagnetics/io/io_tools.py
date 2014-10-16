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

import time

from magnum.config import cfg
from magnum.logger import logger

def try_io_operation(io_fn):
    if cfg.options.on_io_error in [1, 2]:
        max_tries = 100
    else:
        max_tries = 0
    wait_time = 6

    tries = 0
    done = False
    while not done:
        try:
            io_fn()
            break
        except RuntimeError:  # e.g., generated by C++ code
            tries += 1
            if tries > max_tries:
                logger.error("I/O operation failed, giving up after %s tries.", max_tries)
                raise
            logger.warn("I/O operation failed, retrying in %s seconds. (Tries left: %s)", wait_time, max_tries - tries)
            time.sleep(wait_time)
        except:  # any other exception is an immediate error
            raise
