from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        # Diccionario para almacenar las variables y sus valores
        self.variables = {}

    def visitPrograma(self, ctx):
        # Recorre todas las sentencias y las evalúa
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables

    def visitAssign(self, ctx):
        # Maneja las asignaciones de variables
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        
        # Si la variable no existe, la inicializamos
        if var not in self.variables:
            self.variables[var] = 0  # Asignamos valor inicial a la variable
        self.variables[var] = value
        print(f"{var} = {value}")
        return value

    def visitForLoop(self, ctx):
        # Inicialización del bucle for
        var = ctx.inicializacion().ID().getText()
        self.variables[var] = self.visit(ctx.inicializacion().expresion())
        
        # Asegurarse de que 'x' esté inicializada antes de la ejecución del ciclo
        if 'x' not in self.variables:
            self.variables['x'] = 0  # Inicializar 'x' si no está definida
        
        # Evaluación del bucle
        while self.visit(ctx.condicion()):
            print(f"Ejecutando el ciclo for con {var} = {self.variables[var]}")
            self.visit(ctx.bloque())  # Ejecuta el bloque de instrucciones dentro del for
            
            # Actualización de la variable de control del bucle
            update_var = ctx.actualizacion().ID().getText()
            new_value = self.visit(ctx.actualizacion().expresion())
            self.variables[update_var] = new_value

            # Actualizar el valor de x dentro del ciclo
            if 'x' in self.variables:
                self.variables['x'] = self.variables.get('x', 0) + 2
        
        print("Finalizó la ejecución del bucle FOR")

    def visitCondicion(self, ctx):
        # Evalúa la condición del bucle for
        var = ctx.ID().getText()
        value = self.variables.get(var, 0)
        cmp_value = int(ctx.INT().getText())
        op = ctx.op.text
        
        if op == '>':
            return value > cmp_value
        elif op == '<':
            return value < cmp_value
        elif op == '==':
            return value == cmp_value
        elif op == '!=':
            return value != cmp_value
        return False

    def visitAddSub(self, ctx):
        # Evalúa operaciones de suma y resta
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left + right if ctx.op.text == '+' else left - right

    def visitMulDiv(self, ctx):
        # Evalúa operaciones de multiplicación y división
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left * right if ctx.op.text == '*' else left / right

    def visitInt(self, ctx):
        # Devuelve el valor de un número entero
        return int(ctx.getText())

    def visitVariable(self, ctx):
        # Obtiene el valor de una variable almacenada en el diccionario
        var = ctx.getText()
        if var not in self.variables:
            print(f"Variable '{var}' no está inicializada. Se asume 0.")
        return self.variables.get(var, 0)