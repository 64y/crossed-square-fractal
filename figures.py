import numpy as np
import parse


class SVGElement:
	"""SVGElement is a SVG format codec for child classes."""

	@staticmethod
	def svg_encode(element):
		"""
		Child class call this method to encode elemten into SVG code.

		Parameter:
			element: Element to be encoded.

		Return:
			svg_code (str): SVG code of element.

		Example:
			Line is encoded into SVG code.

			>>> line = Line("#FF0000FF", Point(0, 0), Point(1, 1))
			>>> line_svg_code = Line.svg_encode(line)
			>>> line_svg_code
			<line x1="0.0" y1="0.0" x2="1.0" y2="1.0" stroke="#FF0000FF" />

		"""
		pass

	@staticmethod
	def svg_decode(svg_code):
		"""
		Child class call this method to decode SVG code into class's instance element.

		Parameter:
			svg_code (str): Element represented by its SVG code.

		Return:
			element (str): Decoded element.

		Example:
			Line is decoded from SVG code.

			>>> line_svg_code = '<line x1="0.0" y1="0.0" x2="1.0" y2="1.0" stroke="#FF0000FF" />'
			>>> line = Line.svg_decode(line_svg_code)
			>>> line
			Line [0.0 0.0], [1.0, 1.0] / #FF0000FF
		"""
		pass


class Point:
	"""The Point object describes by its coordinates x and y.

	Note:
		Attribute is a casted to float parameter.

	Parameters:
		x (number): x coordinate;
		y (number): y coordinate.

	Attributes:
		x (float): x coordinate;
		y (float): y coordinate.
	"""
	def __init__(it, x, y):
		it.x = float(x)
		it.y = float(y)

	def __add__(a, b):
		"""Overriding operator **+** plus

		Parameters:
			a (Point): The left operand of operation;
			b (Point, np.array[Point..Point], Figure): The right operand of operation; It could be the instance of a Point, an np.array of Points or a Figure.

		Raises:
			ValueError: If parameter b does not the instance of Point or Figure.

		Return:
			c (Point, np.array[Point..Point], Figure): new Point - the result of addition operation.

		Examples:
			Point and Point addition:

			>>> point_a = Point(3, 4)
			>>> point_b = Point(4, 3)
			>>> point_c = point_a + point_b
			>>> point_c
			[7.0, 7.0]

			Point and np.array of Points addition:

			>>> point_a = Point(1, 2)
			>>> points_b = np.array([Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 0)], dtype=Point)
			>>> points_c = point_a + points_b
			>>> points_c
			[[4.0, 6.0], [6.0, 8.0], [8.0, 10.0], [10.0, 2.0]]

			Point and Line addition:

			>>> point_a = Point(3, -3)
			>>> line_b = Line("#FF0000FF", Point(2, 8), Point(7, 13))
			>>> line_c = point_a + line_b
			>>> line_c
			Line [5.0 5.0], [10.0, 10.0] / #FF0000FF

		"""
		if isinstance(b, Point):
			return Point(a.x+b.x, a.y+b.y)
		elif isinstance(b, np.ndarray) and isinstance(b[0], Point):
			c = np.zeros(b.shape[0], dtype=Point)
			for i, b_point in enumerate(b):
				c[i] = a + b_point
			return c
		elif isinstance(b, Figure) or (isinstance(b, np.ndarray) and isinstance(b[0], Figure)):
			return b + a
		else:
			raise ValueError('In Point __add__(a, b) Point, b is not a Point or array of Points!')

	def __sub__(a, b):
		"""
		Overriding operator **-** minus

		Parameters:
			a (Point): The left operand of operation - Point;
			b (Point): The right operand of operation - Point.

		Return:
			c (Point): The result of subtraction operation.

		Examples:
			Point and Point subtraction:

			>>> point_a = Point(7, 3)
			>>> point_b = Point(6, 2)
			>>> point_c = point_a - point_b
			>>> point_c
			[1.0, 1.0]

		"""
		return Point(a.x-b.x, a.y-b.y)

	def __mul__(a, b):
		"""
		Overriding operator ***** multiply between Point and float

		Parameters:
			a (Point): The left operand of operation - Point;
			b (float): The right operand of operation - float.

		Return:
			c (Point): The result of multiplication operation.

		Examples:
			Point and float multiplication:

			>>> point_a = Point(2, 2)
			>>> float_b = 5.0
			>>> point_c = point_a * float_b
			>>> point_c
			[10.0, 10.0]

		"""
		return Point(a.x*b, a.y*b)

	def __rmul__(a, b):
		"""
		Overriding operator ***** multiply between float and Point

		Note:
			Variables a and b are swaping automatically.

		Parameters:
			a (Point): The right operand of operation - Point;
			b (float): The left operand of operation - float.

		Return:
			c (Point): The result of multiplication operation.

		Examples:
			float and Point multiplication:

			>>> float_a = 2.0
			>>> point_b = Point(3, 4)
			>>> point_c = float_a * point_b
			>>> point_c
			[6.0, 8.0]

		"""
		return a * b

	def __truediv__(a, b):
		"""
		Overriding operator **/** division between Point and float

		Parameters:
			a (Point): The left operand of operation - Point;
			b (float): The right operand of operation - float.

		Return:
			c (Point): The result of division operation.

		Examples:
			Point and float division:

			>>> point_a = Point(6, 3)
			>>> float_b = 3.0
			>>> point_c = point_a / float_b
			>>> point_c
			[2.0, 1.0]

		"""
		return Point(a.x/b, a.y/b)

	def __eq__(it, point):
		"""Overriding operator **==** equality."""
		return it.x == point.x and it.y == point.y

	def __hash__(it):
		"""
		Overriding method **__hash__**.

		Note:
			We want to be able to create set of Points.

		Return:
			hash (int): The hash value of `it` Point.

		"""
		return hash((it.x, it.y))

	def __str__(it):
		"""Overriding method **__str__**."""
		return f'[{it.x}, {it.y}]'


class Figure:
	"""
	Figure is parent class for Line, Triangle, ... Each figure is representing by its color and points.

	Note:
		We use Point in a range from Point(0.0, 0.0) to Point(1.0, 1.0).

	Parameters:
		color (str): Color format is #{red:02X}{green:02X}{blue:02X}{alpha:02X}, for example: '#FF0000FF' - red;
		*points (Point, Point, ...): non-key worded, variable-length argument list of Points.

	Attributes:
		color (str): The color of figure.
		points (np.array of Points): The numpy array of figure points.

	Example:
		Creating line:

		>>> line = Line('#00FF00FF', Point(0, 0), Point(1.0, 1.0))

		Creating Triangle:

		>>> triangle = IsoscelesRightTriangle('#0000FFFF', Point(0, 0.5), Point(0, 0), Point(0.5, 0))
	"""
	def __init__(it, color, *points):
		points = points[0] if len(points) == 1 else points
		it.color = color
		it.points = np.array(points, dtype=Point)

	def __add__(a, b):
		"""Overriding operator **+** plus

		Parameters:
			a (Figure): The left operand of operation;
			b (Point, Figure): The right operand of operation; It could be the instance of a Point or a Figure.

		Return:
			c (Figure: Line, Triangle): new Figure - the result of addition operation of lines points, but save the color of the left operand.

		Examples:
			Line and Line addition:

			>>> line_a = Line('#FF0000FF', Point(1, 1), Point(5, 5))
			>>> line_b = Line('#0000FFFF', Point(4, 4), Point(-4, -4))
			>>> line_c = line_a + line_b
			>>> line_c
			Line [5.0 5.0], [1.0, 1.0] / #FF0000FF
		"""
		color = a.color
		points = a.points + (b if isinstance(b, Point) else b.points)
		return a.__class__(color, points)

	def __mul__(a, b):
		"""
		Overriding operator ***** multiply between Figure and float.

		Parameters:
			a (Figure): The left operand of operation - Figure;
			b (int, float): The right operand of operation - numeric.

		Return:
			c (Figure): The result of multiplication operation.

		Examples:
			Line and float multiplication:

			>>> line_a = Line('#FF0000FF', Point(4, 4), Point(8, 8))
			>>> float_b = 0.25
			>>> line_c = line_a * float_b
			>>> line_c
			Line [1.0 1.0], [2.0, 2.0] / #FF0000FF

		"""
		assert(isinstance(b, (int, float)))
		return a.__class__(a.color, a.points*float(b))

	def __eq__(it, figure):
		"""Overriding operator **==**."""
		return set(it.points) == set(figure.points)

	def __hash__(it):
		"""Overriding method **__hash__**."""
		return hash([it.color] + [p for p in it.points])

	def __str__(it):
		"""Overriding method **__str__**."""
		return f'{type(it).__name__} {", ".join([str(p) for p in it.points])} / {it.color}'


class Line(Figure, SVGElement):
	"""
	Line is a basic Figure, it is a child of Figure - inherit attributes (color, points) and opperations (+, *), and SVGElement - inherit SVG codec methods.

	Parameters:
		color (str): Line's color;
		*points (Point, Point, ...): Line's points.

	Attributes:
		color (str): The color of line.
		points (np.array of Points): The numpy array of line points.

	Raises:
		ValueError: If there are more or less then two Points in *points.

	"""
	def __init__(it, color, *points):
		super(Line, it).__init__(color, *points)
		if len(it.points) != 2:
			raise ValueError('Line must have two Points exactly!')

	@staticmethod
	def svg_encode(line):
		return f'<line x1="{line.points[0].x}" y1="{line.points[0].y}" x2="{line.points[1].x}" y2="{line.points[1].y}" stroke="{line.color}" />'

	@staticmethod
	def svg_decode(svg_code):
		p = parse.parse('<line x1="{point_0_x:f}" y1="{point_0_y:f}" x2="{point_1_x:f}" y2="{point_1_y:f}" stroke="{color}" />', svg_code)
		return Line(p['color'], Point(p['point_0_x'], p['point_0_y']), Point(p['point_1_x'], p['point_1_y']))


class IsoscelesRightTriangle(Figure, SVGElement):
	"""
	IsoscelesRightTriangle is a basic Figure, it is a child of Figure - inherit attributes (color, points) and opperations (+, *), and SVGElement - inherit SVG codec methods.

	Parameters:
		color (str): Triangle's color;
		*points (Point, Point, ...): Triangle's points.

	Attributes:
		color (str): The color of triangle;
		points (np.array of Points): The numpy array of triangle points. Points are ordered as follow: `it.points[0] - first hypotenuse point, it.points[1] - second hypotenuse point, it.points[2] - right-angle point;
		d (Point): Middle point of hypotenuse;
		m (Point): Middle point between `it.points[2]` and `d`.

	Raises:
		ValueError: If there are more or less then three Points in *points. Or if triangle does not fit appropriate conditions.

	"""
	def __init__(it, color, *points):
		super(IsoscelesRightTriangle, it).__init__(color, *points)
		if len(it.points) != 3:
			raise ValueError('Triangle must have three Points exactly!')
		p0, p1, p2 = np.array([it.points[0].x, it.points[0].y], dtype=np.float32), np.array([it.points[1].x, it.points[1].y], dtype=np.float32), np.array([it.points[2].x, it.points[2].y], dtype=np.float32)
		p0p1_length = np.sqrt(np.sum(np.power(p0-p1, 2.0)))
		p1p2_length = np.sqrt(np.sum(np.power(p1-p2, 2.0)))
		p2p0_length = np.sqrt(np.sum(np.power(p2-p0, 2.0)))
		if p0p1_length > p1p2_length and p0p1_length > p2p0_length:
			pass
		elif p1p2_length > p0p1_length and p1p2_length > p2p0_length:
			it.points[[0, 1, 2]] = it.points[[1, 2, 0]]
		elif p2p0_length > p0p1_length and p2p0_length > p1p2_length:
			it.points[[0, 1, 2]] = it.points[[2, 0, 1]]
		else:
			raise ValueError('It does not smell like appropriate triangle!')
		it.d = it.points[0] - (it.points[0]-it.points[1])/2.0
		it.m = it.points[2] - (it.points[2]-it.d)/2.0

	def __hash__(it):
		"""Overriding method `__hash__` of IsoscelesRightTriangle."""
		return hash(it.m)

	def split(it):
		"""
		Method split `it` isosceles right triangle into two isosceles right triangles.

		Return:
			nd.array (Triangle): Two triangles based on the first one

		Example:
			Spliting triangle:

			>>> triangle = IsoscelesRightTriangle('#0000FFFF', Point(0, 1), Point(0, 0), Point(1, 0))
			>>> triangles = triangle.split()
			>>> '\\n'.join([t.__str__() for t in triangles])
			IsoscelesRightTriangle [1.0, 0.0], [0.0, 0.0], [0.5, 0.5] / #0000FFFF
			IsoscelesRightTriangle [0.0, 1.0], [0.0, 0.0], [0.5, 0.5] / #0000FFFF

		"""
		return np.array(
			[
				IsoscelesRightTriangle(it.color, it.points[0], it.points[2], it.d),
				IsoscelesRightTriangle(it.color, it.points[1], it.points[2], it.d)
			],
			dtype=IsoscelesRightTriangle
		)

	@staticmethod
	def svg_encode(triangle):
		return f'<polygon points="{triangle.points[0].x},{triangle.points[0].y} {triangle.points[1].x},{triangle.points[1].y} {triangle.points[2].x},{triangle.points[2].y}" fill="{triangle.color}" fill-opacity="{float(int(triangle.color[-2:], 16))/255.0}" stroke="#000000FF" />'

	@staticmethod
	def svg_decode(svg_code):
		p = parse.parse('<polygon points="{point_0_x:f},{point_0_y:f} {point_1_x:f},{point_1_y:f} {point_2_x:f},{point_2_y:f}" fill="{color}" fill-opacity="{color_opacity}" stroke="#000000FF" />', svg_code)
		return IsoscelesRightTriangle(p['color'], Point(p['point_0_x'], p['point_0_y']), Point(p['point_1_x'], p['point_1_y']), Point(p['point_2_x'], p['point_2_y']))
