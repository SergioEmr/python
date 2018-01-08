turno_totales = [1,2,3,4]
semana_totales = [1,2,3,4,5,6,7]
mes_totales = [1,2,3,4,5,6,7,8,9,10,11,12]
proxpol_totales = [1,2,3,4,5,6,7,8,9,10,11]
# @param{List} valor
# reuturn{List} probabilidad de ocurrencia
def probabilidades(lista):
	y = 0
	test = lista
	probabilidad = []
	for x in lista:
		y += x
	for x in range(len(lista)):
		probabilidad.append(lista[x]/y)
	return test