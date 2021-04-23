from tkinter import *

class Tijolos:
	def __init__(self, canvas, eixos=5, quant=8, alt=30, pad=10):
		self.canvas = canvas

		self.tijolos = []

		larg = int(self.canvas['width']) // quant

		#L(quant) = Larg_TOTAL // quant - quant * pad

		cores = ['green', 'orange', 'white', 'lightgray', 'yellow', 'purple']

		# Cria uma lista, de acordo com o indicado
		for pos_y in range(1, eixos+1):
			aux = []
			
			if pos_y <= len(cores): cor = cores[pos_y]
			else: cor = cores[pos_y % len(cores)]
			
			for pos_x in range(quant):
				p_i = (larg*pos_x, alt*pos_y)
				p_f = (p_i[0]+larg, p_i[1]+alt)

				aux.append(
					self.Tijolo( ((p_i[0], p_i[1]), (p_f[0], p_f[1])), cor )
				)

			self.tijolos.append(aux)

	def Tijolo(self, coord, cor='red'): 

		id = self.canvas.create_rectangle(*coord, fill=cor, width=4)
		return id

	def DeletaTijolo(self, id):

		self.canvas.delete(id)

		coord = []
		for ind_y in range(len(self.tijolos)):
			if id in self.tijolos[ind_y]:
				coord = (ind_y, self.tijolos[ind_y].index(id))

		self.tijolos[coord[0]].pop(coord[1])
		self.tijolos[coord[0]].insert(coord[1], None)

if __name__ == '__main__':

	from tela import Tela
	from barra import Barra  
	from bola import Bola

	tela = Tela()
	Barra(tela.canvas)

	# Teste dos tijolos
	tij = Tijolos(tela.canvas)
	print(tij.tijolos)

	print(tij.tijolos[3][2])
	tij.DeletaTijolo(tij.tijolos[3][2])
	print(tij.tijolos)


	bola = Bola(tela.canvas, tela.inst)

	bola.Inicia()
	bola.Update()

	tela.inst.mainloop()