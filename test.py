import numpy as np
import unittest

from figures import Point, Line


class TestPoint(unittest.TestCase):
	"""TestPoint is a class to test point's operations."""

	def test_point_add_point(it):
		"""testing: Point + Point"""
		a = Point(2.75, 3.25)
		b = Point(0.25, 2.75)
		c = Point(3.0, 6.0)
		r = a + b
		it.assertEqual(c, r)

	def test_point_add_points(it):
		"""testing: Point + [Point ... Point]"""
		a = Point(-0.25, -0.75)
		b = np.array([Point(1.25, 1.75), Point(4.25, 4.75), Point(8.25, 8.75), Point(0.25, 0.75), Point(2.25, 2.75)], dtype=Point)
		c = np.array([Point(1, 1), Point(4, 4), Point(8, 8), Point(0, 0), Point(2, 2)], dtype=Point)
		r = a + b
		np.testing.assert_array_equal(c, r)

	def test_points_add_point(it):
		"""testing: [Point ... Point] + Point"""
		a = np.array([Point(1.25, 1.75), Point(4.25, 4.75), Point(8.25, 8.75), Point(0.25, 0.75), Point(2.25, 2.75)], dtype=Point)
		b = Point(-0.25, -0.75)
		c = np.array([Point(1, 1), Point(4, 4), Point(8, 8), Point(0, 0), Point(2, 2)], dtype=Point)
		r = a + b
		np.testing.assert_array_equal(c, r)

	def test_points_add_points(it):
		"""testing: [Point ... Point] + [Point ... Point]"""
		a = np.array([Point(0, 1), Point(2, 3), Point(4, 5), Point(6, 7), Point(8, 9)], dtype=Point)
		b = np.array([Point(5, 4), Point(3, 2), Point(1, 0), Point(-1, -2), Point(-3, -4)], dtype=Point)
		c = np.array([Point(5, 5), Point(5, 5), Point(5, 5), Point(5, 5), Point(5, 5)], dtype=Point)
		r = a + b
		np.testing.assert_array_equal(c, r)

	def test_point_mul_numeric(it):
		"""testing: Point * number"""
		a = Point(2, 4)
		b = 5
		c = Point(10, 20)
		r = a * b
		it.assertEqual(c, r)

	def test_numeric_mul_point(it):
		"""testing: number * Point"""
		a = 3
		b = Point(5, 7)
		c = Point(15, 21)
		r = a * b
		it.assertEqual(c, r)

	def test_points_mul_numeric(it):
		"""testing: [Point ... Point] * number"""
		a = np.array([Point(1, 3), Point(5, 7), Point(9, 11)], dtype=Point)
		b = 2
		c = np.array([Point(2, 6), Point(10, 14), Point(18, 22)], dtype=Point)
		r = a * b
		np.testing.assert_array_equal(c, r)

	def test_numeric_mul_points(it):
		"""testing: number * [Point ... Point]"""
		a = 0.5
		b = np.array([Point(0, 2), Point(4, 6), Point(8, 10), Point(12, 14)], dtype=Point)
		c = np.array([Point(0, 1), Point(2, 3), Point(4, 5), Point(6, 7)], dtype=Point)
		r = a * b
		np.testing.assert_array_equal(c, r)


class TestFigure(unittest.TestCase):
	"""TestFigure is a class to test operations between Figures and Points."""

	def test_line_add_point(it):
		"""testing: Line + Point"""
		a = Line('red', Point(0, 0), Point(1, 1))
		b = Point(5, 5)
		c = Line('red', Point(5, 5), Point(6, 6))
		r = a + b
		it.assertEqual(c, r)

	def test_point_add_line(it):
		"""testing: Point + Line"""
		a = Point(-3, +3)
		b = Line('red', Point(8, 2), Point(13, 7))
		c = Line('red', Point(5, 5), Point(10, 10))
		r = a + b
		it.assertEqual(c, r)

	def test_lines_add_point(it):
		"""testing: [Line ... Line] + Point"""
		a = np.array(
			[
				Line('red', Point(8, 8), Point(3, 3)),
				Line('green', Point(13, 13), Point(18, 18)),
				Line('blue', Point(10, 5), Point(15, 20))
			],
			dtype=Line
		)
		b = Point(2, 2)
		c = np.array(
			[
				Line('red', Point(10, 10), Point(5, 5)),
				Line('green', Point(15, 15), Point(20, 20)),
				Line('blue', Point(12, 7), Point(17, 22))
			],
			dtype=Line
		)
		r = a + b
		np.testing.assert_array_equal(c, r)

	def test_point_add_lines(it):
		"""testing: Point + [Line ... Line]"""
		a = Point(3, 3)
		b = np.array(
			[
				Line('red', Point(5, 5), Point(7, 7)),
				Line('green', Point(1, 1), Point(3, 3)),
				Line('blue', Point(5, 7), Point(1, 3))
			],
			dtype=Line
		)
		c = np.array(
			[
				Line('red', Point(8, 8), Point(10, 10)),
				Line('green', Point(4, 4), Point(6, 6)),
				Line('blue', Point(8, 10), Point(4, 6))
			],
			dtype=Line
		)
		r = a + b
		np.testing.assert_array_equal(c, r)

	def test_line_add_line(it):
		"""testing: Line + Line"""
		a = Line('red', Point(0, 1), Point(2, 3))
		b = Line('green', Point(4, 5), Point(6, 7))
		c = Line('red', Point(4, 6), Point(8, 10))
		r = a + b
		it.assertEqual(c, r)


if __name__ == '__main__':
	unittest.main()
