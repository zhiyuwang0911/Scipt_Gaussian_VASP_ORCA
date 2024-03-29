from ase.io import read
from ase import Atoms
from ase.build import surface, bulk
from ase.io import write

geom = read('geometry.in')

slab = surface(geom, (0, 0, 1), 1)
slab.center(vacuum=10, axis=2)
slab *= (5, 5, 1)
write('slab.in', slab)

