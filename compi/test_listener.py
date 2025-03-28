from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

def test_listener():
    # Solicitar al usuario que ingrese el ciclo for completo en una línea
    codigo_for = input("Ingrese el ciclo 'for' completo (ej. for(i = 0; i < 3; i = i + 1) { x = x + 2; };): ")

    # Crear el flujo de entrada
    input_stream = InputStream(codigo_for)
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)

    # Generar el árbol de sintaxis
    tree = parser.programa()

    # Ejecutar el Listener
    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, tree)

# Ejecutar la función de prueba
test_listener()