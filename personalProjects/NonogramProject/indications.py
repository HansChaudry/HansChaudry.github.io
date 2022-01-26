from Nonogram import *

def put_row_nums(row_list):

	pygame.init()

	font = pygame.font.SysFont('ptmono.ttf', 40)

	for x in range(len(row_list)):
		nums = str(row_list[x])
		nums = nums.replace(', ', ' ')

		# create a text surface object,
		# on which text is drawn on it.
		text = font.render(nums[1:-1], True, white, gray)

		# create a rectangular object for the
		# text surface object
		textRect = text.get_rect()

		# set the center of the rectangular object.
		textRect.center = (VARS['grid_Origin'][0] // 2, (VARS['grid_Origin'][1] + 25) + 50 * x)
		#place object(text) on the board
		VARS['board'].blit(text, textRect)

def put_col_nums(col_list):

	pygame.init()

	font = pygame.font.SysFont('ptmono.ttf', 40)

	for x in range(len(col_list)):
		nums = str(col_list[x])
		nums = nums.replace(', ', ' ')

		# create a text surface object,
		# on which text is drawn on it.
		text = font.render(nums[1:-1], True, white, gray)
		text = pygame.transform.rotate(text, 270)

		# create a rectangular object for the
		# text surface object
		textRect = text.get_rect()

		# set the center of the rectangular object.
		textRect.center = ((VARS['grid_Origin'][0] + 25) + 50 * x, VARS['grid_Origin'][1]/2)
		#place object(text) on the board
		VARS['board'].blit(text, textRect)