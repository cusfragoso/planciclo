class PlanDelCiclo:
    def __init__(self):
        self.plan = {}

    def preguntar(self, pregunta):
        respuesta = input(pregunta + " ")
        return respuesta

    def recopilar_respuestas(self):
        preguntas = [
            "¿Cuál es tu próximo porqué?",
            "¿Cuántos inscritos tuyos y del equipo lograste en el ciclo anterior?",
            "¿Cuál es tu meta en puntos para este ciclo?",
            "¿Cuántos matches hiciste en el ciclo anterior?",
            "¿Cuántos matches piensas hacer en el nuevo ciclo?",
            "¿Cuánto necesitas ganar este ciclo?",
            "¿Cuánto ganaste en el ciclo anterior?",
            "¿Cuál es tu meta de posición?",
            "¿Cuántos zafiros nuevos planeas lograr?",
            "¿Qué habilidades necesitas mejorar?",
            "¿Cómo piensas mejorar esas habilidades?",
            "¿Cuántos inscritos planeas lograr este ciclo?",
            "¿Cuántos puntos planeas lograr este ciclo?",
            "¿Cuántos matches planeas lograr este ciclo?",
            "¿Cuál es tu meta para esta semana?",
            "¿Cuántas citas te comprometes a hacer cada semana?"
        ]

        for pregunta in preguntas:
            respuesta = self.preguntar(pregunta)
            if respuesta:
                self.plan[pregunta] = respuesta
            else:
                self.plan[pregunta] = "No respondido"

    def generar_resumen(self):
        print("\nResumen del Plan del Ciclo:")
        for pregunta, respuesta in self.plan.items():
            print(f"{pregunta}: {respuesta}")

if __name__ == "__main__":
    plan_ciclo = PlanDelCiclo()
    plan_ciclo.recopilar_respuestas()
    plan_ciclo.generar_resumen()

