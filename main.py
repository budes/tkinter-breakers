from sys import path

path.append('codigos')

from tela import Tela

from barra import Barra
from bola import Bola
from tijolos import Tijolos

tela = barra = tijolos = bola = None

def Inicia(inst_existe=False):
	global tela, barra, tijolos, bola

	if not inst_existe:
		tela = Tela(full=True)
		barra = Barra(tela.canvas)
		
	tijolos = Tijolos(tela.canvas)

	bola = Bola(tela.canvas, tela.inst, deleta_colisao)

	def movimenta_bola(): bola.Inicia(); bola.Update()

	tela.but_init['command'] = movimenta_bola

# --------------------------

def Reinicia():
	global bola, tijolos

	bola.DeletaBola()

	for eixos in tijolos.tijolos:
		for id in eixos:
			tijolos.DeletaTijolo(id)

	Inicia(True)

# --------------------------

def deleta_colisao(colis):
	# Detectando colisao, ele deleta

	if colis == 'fundo':
		Reinicia()

	elif colis != barra.barra_id:
		tijolos.DeletaTijolo(colis)

# ==================================

Inicia()

bola.Update()

tela.inst.mainloop()