import seleccion
import pandas as pd
data = []
target = []
valores = [12,3,4,5]
Pturno = []
Psemana = []
Pproxpol = []
delito = []
hreporte = []
mes = []
dianum = []
diasem = []
turno = []
factorv = []
sexov = []
lat = []
lon = []
unidad = []
csv = "Dataset1.csv"
def lecturaCsv(csv):
	Datos = pd.read_csv(csv)
	data = Datos[Datos.columns[0:-1]].as_matrix() 
	target = Datos[Datos.columns[-1]].as_matrix()
	return target


def registroDelitos(entrada):
	for g in range(len(entrada['features'])):
		delito.append(entrada['features'][g]['properties']['TIPODELITO'])
		mes.append(entrada['features'][g]['properties']['MES'])
		hreporte.append(entrada['features'][g]['properties']['HREPORTE'])
		diasem.append(entrada['features'][g]['properties']['DIASEM'])
		dianum.append(entrada['features'][g]['properties']['DIANUM'])
		factorv.append(entrada['features'][g]['properties']['FACTOR_V'])
		sexov.append(entrada['features'][g]['properties']['SEXOV'])
		lat.append(entrada['features'][g]['geometry']['coordinates'][0])
		lon.append(entrada['features'][g]['geometry']['coordinates'][1])
		unidad.append(entrada['features'][g]['properties']['UNIDAD'])
		turno.append(entrada['features'][g]['properties']['TURNO'])
	robo = {'R. PERSONA': delito.count('R. PERSONA')}
	totales = [
	delito[4], hreporte[4], mes[4], diasem[4], 
	dianum[4], factorv[4], lat[4], lon[4], unidad[4], turno[4]]
	return totales
	
def prediccionDia(lista):
	pass
print(type(data))
# Pturno 	= pparametro(turno_totales)
# Psemana = pparametro(semana_totales)