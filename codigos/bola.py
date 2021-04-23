from tkinter import *


class Bola:
	def __init__(self, canvas, inst, func_colis=None, cor='red', xy_i=(300, 300), diam=40, passo=15):
		'''
		canvas → Onde vai ser desenhado
		inst → Instância, para fazer uns códigos de movimento
		func_colis → Se a colisão for detectada, qual função executar
		cor → Cor da bola
		xy_i → Posição do ponto inicial (Esquerda inferior ←↓)
		diam → Diametro do circulo
		passo → O passo (em pixels), da bola
		'''

		self.inst = inst
		self.canvas = canvas

		self.func = func_colis
		
		self.bola = self.canvas.create_oval(
			xy_i, (xy_i[0]+diam, xy_i[1]-diam),
			fill=cor)

		self.passo = passo
		self.mod_x = self.mod_y = 0

	def Inicia(self): self.mod_x = self.mod_y = 1

	def Movimento(self):
		self.canvas.move(self.bola,
			self.mod_x * self.passo, self.mod_y * self.passo
		)

	def ChecaColisao(self):

		colis_bola = self.canvas.bbox(self.bola)

		if colis_bola[0] <= 0 or colis_bola[2] > int(self.canvas['width']):
			self.mod_x *= -1 
		if colis_bola[1] <= 0:
			self.mod_y *= -1 

		if colis_bola[3] > int(self.canvas['height']):
			return 'fundo'

		ids_proximos = self.canvas.find_overlapping(*colis_bola)
		if len(ids_proximos) > 1:
			self.mod_y *= -1

			return ids_proximos[0] # Retorna o id de onde colidiu

		return None

	def Update(self):
		if self.mod_x != 0: # Indiquei só um, mas pode indicar o outro
			
			colis = self.ChecaColisao()

			if colis != None and self.func != None:
				self.func(colis)

			self.Movimento()

			if colis != 'fundo':
				self.inst.after(30, self.Update)

	def DeletaBola(self): self.canvas.delete(self.bola)

if __name__ == '__main__':
	from tela import Tela
	from barra import Barra  

	tela = Tela((640, 468), full=False)
	Barra(tela.canvas)

	# Teste da bola
	bola = Bola(tela.canvas, tela.inst)
	bola.Inicia()
	bola.Update()

	tela.inst.mainloop()