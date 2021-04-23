from tkinter import *

class Tela:
	def __init__(self, res=None, full=True):
		'''
		res → Resolução da tela
		full → Fullscreen
		'''

		# Instancia e configuração
		self.inst = Tk()

		if res == None: larg, alt = self.ObterResolucao()
		else: larg, alt = res
		
		self.inst.geometry(f'{larg}x{alt}')
		
		if full: self.inst.attributes("-fullscreen", True)

		# ================================

		self.canvas = Canvas(self.inst, height=alt-60, width=larg,
		bg='black', highlightthickness=0)
		
		self.canvas.pack()

		framebut = Frame(self.inst)

		self.but_init = Button(framebut, bg='green', width=72, height=10)
		self.but_init.pack(side=LEFT)
		
		but_sair = Button(framebut, bg='red', width=72, height=10,
			command=exit)
		but_sair.pack()

		framebut.pack()

	def ObterResolucao(self, inst=None):

		if inst == None:        
			altura = self.inst.winfo_screenheight()
			largura = self.inst.winfo_screenwidth()
		else:
			altura = inst.winfo_screenheight()
			largura = inst.winfo_screenwidth()


		return largura, altura



if __name__ == '__main__':
	tela = Tela(None)
	tela.inst.mainloop()