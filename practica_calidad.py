"Este es el nuevo cambio que se hizo para el deber de Calidad de Software"
import os
import json 
import requests

# Credenciales obtenidas desde variables de entorno
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir para cero")
    return a / b


def conectar_bd(usuario):
    query = "SELECT * FROM usuarios WHERE nombre = %s"
    return query


def calcular_tipo_a(monto, descuento, cliente):
    if monto > 100:
        if descuento > 0:
            if cliente == "VIP":
                return monto * 0.8
            return monto * 0.9
        return monto
    return monto * 1.1


def calcular_tipo_b(monto, descuento, cliente):
    if monto > 100:
        if descuento > 0:
            if cliente == "VIP":
                return monto * 0.7
            return monto * 0.85
        return monto
    return monto * 1.05


def procesar_pedido(tipo, monto, descuento, cliente):
    if tipo == "A":
        return calcular_tipo_a(monto, descuento, cliente)

    if tipo == "B":
        return calcular_tipo_b(monto, descuento, cliente)

    return 0


def leer_archivo(nombre):
    with open(nombre, "r") as archivo:
        contenido = archivo.read()
    return contenido


def agregar_item(item, lista=None):
    if lista is None:
        lista = []

    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        resultado = usuario / clave
    except ZeroDivisionError:
        resultado = None

    return resultado


def calcular_total(precios):
    total = 0

    for p in precios:
        total += p

    descuento_especial = 50
    return total - descuento_especial


def main():
    try:
        print(dividir(10, 2))
    except ValueError as e:
        print(e)

    print(procesar_pedido("A", 150, 1, "VIP"))
    print(agregar_item("manzana"))
    print(agregar_item("pera"))


if __name__ == "__main__":
    main()
