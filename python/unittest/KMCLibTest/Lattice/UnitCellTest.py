""" Module for testing the UnitCell class. """


# Copyright (c)  2012  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import unittest
import numpy


from KMCLib.Exceptions.Error import Error

# Import from the module we test.
from KMCLib.Lattice.UnitCell import UnitCell


# Implement the test.
class UnitCellTest(unittest.TestCase):
    """ Class for testing the UnitCell class. """

    def testConstruction(self):
        """ Test the construction of the unitcell """

        vector_a = [2.3, 0.0, 0.0]
        vector_b = [2.4, 3.0, 0.0]
        vector_c = [0.0, 0.0, 11.8]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.5]]

        cell_vectors = [vector_a,
                        vector_b,
                        vector_c]

        cell = UnitCell(cell_vectors=cell_vectors,
                        basis_points=basis_points)

        # Check the vectors stored on the class.
        ref_vectors = numpy.array(cell_vectors)
        check_vectors = cell._UnitCell__cell_vectors
        self.assertAlmostEqual( numpy.linalg.norm(ref_vectors - check_vectors), 0.0, 10)

        # Check the basis points stored on the class.
        ref_basis = numpy.array(basis_points)
        check_basis = cell._UnitCell__basis_points
        self.assertAlmostEqual( numpy.linalg.norm(ref_basis - check_basis), 0.0, 10)

    def testConstructionFailVectors(self):
        """ Make sure construction fails if there is a problem with the unitcell vectors. """
        vector_a = [2.3, 0.0, 0.0]
        vector_b = [2.4, 3.0, 0.0, 1.3] # <- wrong shape
        vector_c = [0.0, 0.0, 11.8]
        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.5]]
        cell_vectors = [vector_a,
                        vector_b,
                        vector_c]
        self.assertRaises(Error, lambda: UnitCell(cell_vectors=cell_vectors, basis_points=basis_points))

    def testConstructionFailBasis(self):
        """ Make sure construction fails if there is a problem with the basis points. s"""
        vector_a = [2.3, 0.0, 0.0]
        vector_b = [2.4, 3.0, 0.0]
        vector_c = [0.0, 0.0, 11.8]
        basis_points = [[0.0, 0.0],       # <- wrong shape
                        [0.5, 0.5, 0.5]]
        cell_vectors = [vector_a,
                        vector_b,
                        vector_c]
        self.assertRaises(Error, lambda: UnitCell(cell_vectors=cell_vectors, basis_points=basis_points))


if __name__ == '__main__':
    unittest.main()

