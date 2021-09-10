import collections
import copy
import imageio
import math
import numpy as np
import os
from reportlab.graphics import renderPM
import shutil
from svglib.svglib import svg2rlg
import time

from figures import SVGElement, Point, Figure, Line, IsoscelesRightTriangle


class CrossedSquare(SVGElement):
	"""
	CrossedSquare is a basic class for crossed square. Inheritors are presenting different ways to describe `Crossed Square`
	of iteration `n` by its figures.

	Note:
		If we inscribe a `Crossed Square` in the middle of the sides of another `Crossed Square`, and the second one is without
		overloapings with other `Crossed Squares`. On each iteration we will multiply the number of `Crossed Squares` by four and receive a
		`Crossed Square Fractal` of iteration plus one. The simple `Crossed Square` is a `Crossed Square Fractal` with iteration one.

	Parameters:
		n (int): Iteration number. Default value is 1;
		image_size (int): Image size. Default value is 2048;
		image_border (int): Image border. Default value is 32;
		log (bool): Option of making a `Crossed Square` changing Log. If `log` is False and `log_stash` is empty it is not possible to create *.gif picture. Default value is False.

	Attributes:
		n (int): Iteration number.
		image_size (int): Attribute is used to create image, by multiplying `.figures` Points by `image_size`;
		image_border (int): Attribute is used to create image, and determine the free space from top, bot, left and right;
		log (bool): Option of making a history of changes in `figures`;
		figures (nparray (Figure)): Array of Figures;
		log_stash(list of CrossedSquares): Contains copy of `it` at each stage of adding new elements into the `figures`, if `log` is True. If `log` is False and `log_stash` is empty it is not possible to create *.gif picture.

	"""
	def __init__(it, n=1, image_size=2048, image_border=32, log=False):
		it.n = n
		it.image_size = image_size
		it.image_border = image_border
		it.log = log
		it.figures = np.zeros(0, dtype=Figure)
		it.log_stash = []
		it._generate_figures()

	def _generate_figures(it):
		"""Generate Figures for `n`'th iteration of `Crossed Square`."""
		pass

	def _add_figures(it, figures):
		"""Method use np.append to add `figures` into current `it.figures` and call method `it._log."""
		it.figures = np.append(it.figures, figures)
		it._log()

	def _log(it):
		"""Method add current state of `it` into the `it.log_stash` if `it.log` is True."""
		if not it.log:
			return
		it.log_stash.append(copy.copy(it))

	def write_gif(it, file_name):
		"""Creating *.gif animation of the way `Crossed Square` has been created and write it into the `file_name`.gif file."""
		if not it.log_stash:
			return
		time.ctime()
		tmp_path = f'/tmp/{file_name}_{hash(file_name)}_{time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}'
		os.makedirs(tmp_path)
		with imageio.get_writer(file_name, duration=[0.5]*(len(it.log_stash)-1)+[5], mode='I') as fout_gif:
			for i, cs in enumerate(it.log_stash):
				tmp_file_name = f'{tmp_path}/{it.__class__.__name__}_{i:05d}'
				with open(tmp_file_name + '.svg', 'w') as fout:
					fout.write(it.__class__.svg_encode(cs))
				drawing = svg2rlg(tmp_file_name + '.svg')
				renderPM.drawToFile(drawing, tmp_file_name + '.png', fmt='PNG')
				image = imageio.imread(tmp_file_name + '.png')
				fout_gif.append_data(image)
		shutil.rmtree(tmp_path)

	def write_svg(it, file_name):
		"""Creating *.svg image of `Crossed Square` and write it into the `file_name`.svg file."""
		with open(file_name, 'w') as fout_svg:
			fout_svg.write(it.__class__.svg_encode(it))

	@staticmethod
	def svg_encode(crossed_square):
		svg_code = ''
		svg_code += f'<svg xmlns="http://www.w3.org/2000/svg" width="{crossed_square.image_size+2*crossed_square.image_border}" height="{crossed_square.image_size+2*crossed_square.image_border}" viewBox="{-crossed_square.image_border} {-crossed_square.image_border} {crossed_square.image_size+2*crossed_square.image_border} {crossed_square.image_size+2*crossed_square.image_border}" n="{crossed_square.n}" stroke-linecap="round" stroke-linejoin="round" stroke-width="4">\n'
		svg_code += f'\t<rect x="{-crossed_square.image_border}" y="{-crossed_square.image_border}" width="{crossed_square.image_size+2*crossed_square.image_border}" height="{crossed_square.image_size+2*crossed_square.image_border}" fill="#FFFFFFFF" opacity="1"/>\n'
		for figure in crossed_square.figures:
			figure_scaled = figure * crossed_square.image_size
			svg_code += f'\t{figure.__class__.svg_encode(figure_scaled)}\n'
		svg_code += '</svg>'
		return svg_code

	@staticmethod
	def svg_decode(svg_code):
		"""TODO: Implement svg_decode method for CrossedSquare class."""
		pass


class CrossedSquare0(CrossedSquare):
	"""
	The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare0` as follows:
		a) add all vertical lines into `figures`;
		b) add all horizontal lines into `figures`;
		c) add all diagonal lines into `figures`.
	"""

	def __init__(it, n=0, image_size=2048, image_border=16, log=False):
		super(CrossedSquare0, it).__init__(n, image_size, image_border, log)

	def _generate_figures(it):
		num = pow(2, it.n-1)
		num_horizontal, num_vertical = num+1, num+1
		num_diagonal_first, num_diagonal_second = num-1, num-1
		step_basic = 1.0 / float(num)

		# horizontal
		line = Line('#FF0000FF', Point(0.0, 0.0), Point(1.0, 0.0))
		step = Line('', Point(0.0, step_basic), Point(0.0, step_basic))
		for i in range(num_horizontal):
			it._add_figures(line)
			line = line + step
		# vertical
		line = Line('#00FF00FF', Point(0.0, 0.0), Point(0.0, 1.0))
		step = Line('', Point(step_basic, 0.0), Point(step_basic, 0.0))
		for i in range(num_vertical):
			it._add_figures(line)
			line = line + step
		# first diagonal
		line = Line('#0000FFFF', Point(0.0, 0.0), Point(1.0, 1.0))
		step_left = Line('', Point(0.0, step_basic), Point(-step_basic, 0.0))
		line_left = line + step_left
		step_right = Line('', Point(step_basic, 0.0), Point(0.0, -step_basic))
		line_right = line + step_right
		it._add_figures(line)
		for i in range(num_diagonal_first):
			it._add_figures([line_left, line_right])
			line_left = line_left + step_left
			line_right = line_right + step_right
		# second diagonal
		line = Line('#FFFF00FF', Point(1.0, 0.0), Point(0.0, 1.0))
		step_left = Line('', Point(-step_basic, 0.0), Point(0.0, -step_basic))
		line_left = line + step_left
		step_right = Line('', Point(0.0, step_basic), Point(step_basic, 0.0))
		line_right = line + step_right
		it._add_figures(line)
		for i in range(num_diagonal_first):
			it._add_figures([line_left, line_right])
			line_left = line_left + step_left
			line_right = line_right + step_right


class CrossedSquare1(CrossedSquare):
	"""
	The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare1` as follows:
		a) creating a the smalest possible `Crossed Square` for iteration `n`;
		b) form a matrix of appropriate dimention of that `Crossed Square` and add lines of each `Crossed Square` into `figures`.
	"""
	def __init__(it, n=0, image_size=2048, image_border=16, log=False):
		super(CrossedSquare1, it).__init__(n, image_size, image_border, log)

	def _generate_figures(it):
		num = pow(2, it.n-1)
		step = 1.0 / float(num)
		template_lines = np.array(
			[
				Line('#FF0000FF', Point(0.0, 0.0), Point(1.0, 0.0)),
				Line('#00FF0FFF', Point(0.0, 0.0), Point(0.5, 0.5)),
				Line('#0000FFFF', Point(0.5, 0.5), Point(1.0, 0.0)),
				Line('#0FF000FF', Point(0.0, 0.0), Point(0.0, 1.0)),
				Line('#000FF0FF', Point(1.0, 0.0), Point(1.0, 1.0)),
				Line('#F0000FFF', Point(0.0, 1.0), Point(0.5, 0.5)),
				Line('#FFFF00FF', Point(0.5, 0.5), Point(1.0, 1.0)),
				Line('#00FFFFFF', Point(0.0, 1.0), Point(1.0, 1.0))
			],
			dtype=Line
		) * step
		for y in np.arange(0.0, 1.0, step):
			for x in np.arange(0.0, 1.0, step):
				lines = template_lines + Point(x, y)
				it._add_figures(lines)


class CrossedSquare2(CrossedSquare):
	"""The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare2` as it described in `Note` in `CrossedSquare`."""

	def __init__(it, n=1, image_size=2048, image_border=16, log=False):
		super(CrossedSquare2, it).__init__(n, image_size, image_border, log)

	def _generate_template_lines(it):
		template_lines_0 = np.array(
			[
				Line('#FF0000FF', Point(0.0, 0.0), Point(1.0, 0.0)),
				Line('#00FF00FF', Point(0.0, 0.0), Point(1.0, 1.0)),
				Line('#FFFF00FF', Point(1.0, 0.0), Point(0.0, 1.0)),
				Line('#0000FFFF', Point(0.0, 0.0), Point(0.0, 1.0)),
				Line('#FF00FFFF', Point(1.0, 0.0), Point(1.0, 1.0)),
				Line('#00FFFFFF', Point(0.0, 1.0), Point(1.0, 1.0))
			],
			dtype=Line
		)
		template_lines_1 = np.array(
			[
				Line('#FF0000FF', Point(0.0, 0.5), Point(0.5, 0.0)),
				Line('#00FF00FF', Point(0.5, 0.0), Point(1.0, 0.5)),
				Line('#FFFF00FF', Point(0.5, 0.0), Point(0.5, 1.0)),
				Line('#0000FFFF', Point(0.0, 0.5), Point(1.0, 0.5)),
				Line('#FF00FFFF', Point(0.0, 0.5), Point(0.5, 1.0)),
				Line('#00FFFFFF', Point(0.5, 1.0), Point(1.0, 0.5))
			],
			dtype=Line
		)
		return template_lines_0, template_lines_1

	def _generate_figures(it):
		template_lines_0, template_lines_1 = it._generate_template_lines()
		it._add_figures(template_lines_0)
		for n in range(1, it.n, 1):
			num = pow(2, n-1)
			step = 1.0 / float(num)
			lines = template_lines_1 * step
			for y in np.arange(0.0, 1.0, step):
				for x in np.arange(0.0, 1.0, step):
					it._add_figures(lines + Point(x, y))


class CrossedSquare3(CrossedSquare2):
	"""The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare3` as it described in `Note` in `CrossedSquare`.
	There each side of `Crossed Square` is splited into two lines and `Crossed Square` is represented by four arrows."""

	def __init__(it, n=1, image_size=2048, image_border=16, log=False):
		super(CrossedSquare3, it).__init__(n, image_size, image_border, log)

	def _generate_template_lines(it):
		template_lines_0 = np.array(
			[
				Line('#FF0000FF', Point(0.5, 0.0), Point(0.0, 0.0)),
				Line('#FF0000FF', Point(0.0, 0.5), Point(0.0, 0.0)),
				Line('#FF0000FF', Point(0.5, 0.5), Point(0.0, 0.0)),
				Line('#00FF00FF', Point(0.5, 0.0), Point(1.0, 0.0)),
				Line('#00FF00FF', Point(0.5, 0.5), Point(1.0, 0.0)),
				Line('#00FF00FF', Point(1.0, 0.5), Point(1.0, 0.0)),
				Line('#0000FFFF', Point(0.0, 0.5), Point(0.0, 1.0)),
				Line('#0000FFFF', Point(0.5, 0.5), Point(0.0, 1.0)),
				Line('#0000FFFF', Point(0.5, 1.0), Point(0.0, 1.0)),
				Line('#FFFF00FF', Point(0.5, 1.0), Point(1.0, 1.0)),
				Line('#FFFF00FF', Point(0.5, 0.5), Point(1.0, 1.0)),
				Line('#FFFF00FF', Point(1.0, 0.5), Point(1.0, 1.0))
			],
			dtype=Line
		)
		template_lines_1 = np.array(
			[
				Line('#FF0000FF', Point(0.25, 0.25), Point(0.5, 0.0)),
				Line('#FF0000FF', Point(0.5, 0.5), Point(0.5, 0.0)),
				Line('#FF0000FF', Point(0.75, 0.25), Point(0.5, 0.0)),
				Line('#00FF00FF', Point(0.75, 0.25), Point(1.0, 0.5)),
				Line('#00FF00FF', Point(0.5, 0.5), Point(1.0, 0.5)),
				Line('#00FF00FF', Point(0.75, 0.75), Point(1.0, 0.5)),
				Line('#0000FFFF', Point(0.25, 0.25), Point(0.0, 0.5)),
				Line('#0000FFFF', Point(0.5, 0.5), Point(0.0, 0.5)),
				Line('#0000FFFF', Point(0.25, 0.75), Point(0.0, 0.5)),
				Line('#FFFF00FF', Point(0.25, 0.75), Point(0.5, 1.0)),
				Line('#FFFF00FF', Point(0.5, 0.5), Point(0.5, 1.0)),
				Line('#FFFF00FF', Point(0.75, 0.75), Point(0.5, 1.0))
			],
			dtype=Line
		)
		return template_lines_0, template_lines_1


class CrossedSquare4(CrossedSquare):
	"""The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare4` as follow: `Crossed Square` is represented
	by four isosceles right triangles, and on each iteration each triangle is splited two times."""
	def __init__(it, n=1, image_size=2048, image_border=32, log=False):
		super(CrossedSquare4, it).__init__(n, image_size, image_border, log)

	def _generate_figures(it):
		triangles = np.array(
			[
				IsoscelesRightTriangle('#FF0000FF', Point(0.5, 0.5), Point(0.0, 0.0), Point(0.0, 1.0)),
				IsoscelesRightTriangle('#FF0000FF', Point(0.5, 0.5), Point(0.0, 1.0), Point(1.0, 1.0)),
				IsoscelesRightTriangle('#FF0000FF', Point(0.5, 0.5), Point(1.0, 1.0), Point(1.0, 0.0)),
				IsoscelesRightTriangle('#FF0000FF', Point(0.5, 0.5), Point(0.0, 0.0), Point(1.0, 0.0))
			],
			dtype=IsoscelesRightTriangle
		)
		it._add_figures(triangles)
		for n in range(1, it.n, 1):
			for times in range(2):
				triangles = np.zeros(0, dtype=IsoscelesRightTriangle)
				for t in it.figures:
					triangles = np.append(triangles, t.split())
				it.figures = np.zeros(0, dtype=IsoscelesRightTriangle)
				it._add_figures(triangles)


class CrossedSquare5(CrossedSquare):
	"""The `Crossed Square Fractal` of iteration `n` is build by `CrossedSquare5` as follow:
		1) `Crossed Square` is represented by four isosceles right triangles;
		2) On each iteration:
			2.1) Spliting triangles in `figures` first time;
			2.2) Puting another `Crossed Square` onto each current `Crossed Square` instead of fitting it, as it was described in `CrossedSquare` `Note`'s. This way each triangle is added into `figures`;
			2.3) Spliting the result triangles in `figures` the second time.

	Attributes:
		counts (dict(int: int)): Number of triangles in different layers.

	"""
	def __init__(it, n=1, image_size=2048, image_border=32, log=False):
		super(CrossedSquare5, it).__init__(n, image_size, image_border, log)
		it.counts = dict(
			sorted(
				collections.Counter(
					collections.Counter(
						list(map(lambda x: hash(x), it.figures))
					).values()
				).items()
			)
		)

	def _generate_figures(it):
		color = f'#FF0000{int(255.0/math.log2(float(it.n+1))):02X}' # The simple 255/it.n cause a huge transperency.
		template_triangles_0 = np.array(
			[
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.0, 0.0), Point(0.0, 1.0)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.0, 1.0), Point(1.0, 1.0)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(1.0, 1.0), Point(1.0, 0.0)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.0, 0.0), Point(1.0, 0.0))
			],
			dtype=IsoscelesRightTriangle
		)
		template_triangles_1 = np.array(
			[
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(1.0, 0.5), Point(0.5, 1.0)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.5, 1.0), Point(0.0, 0.5)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.0, 0.5), Point(0.5, 0.0)),
				IsoscelesRightTriangle(color, Point(0.5, 0.5), Point(0.5, 0.0), Point(1.0, 0.5))
			],
			dtype=IsoscelesRightTriangle
		)
		template_triangles_1 = np.concatenate([t.split() for t in template_triangles_1], axis=0)
		it._add_figures(template_triangles_0)
		for n in range(1, it.n, 1):
			num = pow(2, n-1)
			step = 1.0 / float(num)
			for times in range(2):
				triangles = np.zeros(0, dtype=IsoscelesRightTriangle)
				for t in it.figures:
					triangles = np.append(triangles, t.split())
				it.figures = np.zeros(0, dtype=IsoscelesRightTriangle)
				it._add_figures(triangles)
			triangles = template_triangles_1 * step
			for y in np.arange(0.0, 1.0, step):
				for x in np.arange(0.0, 1.0, step):
					it._add_figures(triangles + Point(x, y))
