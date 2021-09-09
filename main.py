from crossedsquare import CrossedSquare, CrossedSquare0, CrossedSquare1, CrossedSquare2, CrossedSquare3, CrossedSquare4, CrossedSquare5


def crossed_square_run_all(n=4, image_size=2048, image_border=32):
	folder = 'data'
	crossed_squares = [CrossedSquare0, CrossedSquare1, CrossedSquare2, CrossedSquare3, CrossedSquare4, CrossedSquare5]
	for crossed_square in crossed_squares:
		cs = crossed_square(n, image_size, image_border, True)
		cs.write_svg(f'{folder}/{type(cs).__name__}_{n}.svg')
		cs.write_gif(f'{folder}/a_{type(cs).__name__}_{n}.gif')


def crossed_square_5_triangle_counts(n_max=8):
	for n in range(1, n_max+1, 1):
		cs = CrossedSquare5(n)
		print(n, cs.counts)


if __name__ == '__main__':
	crossed_square_run_all(n=3, image_size=256)
	

