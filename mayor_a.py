#importamos sys para que podamos acceder a los argumentos de la línea de comando
import sys

umbral = float(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].replace('.', '', 1).isdigit() else sys.exit("Uso: python mayor_a.py <umbral>")

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

print({mes: valor for mes, valor in ventas.items() if valor > umbral})
