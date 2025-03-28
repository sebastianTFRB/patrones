from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

# Solicitar al usuario que ingrese el código para el análisis
input_stream = InputStream(input('? '))

# Crear el lexer
lexer = MiGramaticaLexer(input_stream)

# Crear el flujo de tokens
tokens = CommonTokenStream(lexer)

# Crear el parser
parser = MiGramaticaParser(tokens)

# Generar el árbol de sintaxis
tree = parser.programa()

# Crear el visitante
visitor = EvalVisitor()

# Ejecutar el visitante sobre el árbol de sintaxis
resultado = visitor.visit(tree)

# Imprimir las variables al final
print("Variables al final:", resultado)