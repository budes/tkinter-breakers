from tkinter import *

class Barra:
	def __init__(self, canvas, altura_i=60, alt=20, larg=75):
		'''
		canvas → O próprio canvas onde vai ser desenhado.
		altura_i → Altura inicial do desenho.
		alt → A altura própria do desenho (grossura).
		larg → A largura da barra.
		'''

		self.canvas = canvas

		larg_tot = int(self.canvas['width'])
		alt_tot = int(self.canvas['height'])

		self.pos_x = larg_tot//2 # posição inicial da barra (centro)

		self.barra_id = self.canvas.create_rectangle(
			(self.pos_x-larg, alt_tot-altura_i),
			(self.pos_x+larg, alt_tot-altura_i-alt),
			fill='white'
		)
		self.larg, self.alt = larg, alt

		self.canvas.bind('<Motion>', self.Move)
		self.canvas.focus_force()


	def Move(self, pos):
		if pos.x != self.pos_x and (pos.x > self.larg and pos.x < int(self.canvas['width'])-self.larg):
			self.canvas.move(self.barra_id, pos.x-self.pos_x, 0)
			self.pos_x = pos.x



if __name__ == '__main__':
	from tela import Tela

	tela = Tela((640, 468), full=False)

	# Teste da barra
	Barra(tela.canvas)

	tela.inst.mainloop()