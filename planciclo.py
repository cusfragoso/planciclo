import streamlit as st
import pandas as pd
st.cache.clear()
from io import BytesIO

class PlanDelCiclo:
    def __init__(self):
        self.plan = {}
        self.preguntas = [
            "¿Cuál es tu próximo porqué?",
            "¿Cuántos inscritos tuyos directos lograste este ciclo?",
            "¿Cuántos inscritos aparte de los tuyos, se inscribieron en tu equipo?",
            "¿Cuál es tu meta en puntos para este ciclo?",
            "¿Cuántos matches hiciste en el ciclo anterior?",
            "¿Cuántos matches piensas hacer en el nuevo ciclo?",
            "¿Cuánto necesitas ganar este ciclo?",
            "¿Cuánto ganaste en el ciclo anterior?",
            "¿Cuál es tu meta de posición?",
            "¿Cuántos zafiros nuevos planeas lograr?",
            "¿Qué habilidades necesitas mejorar?",
            "¿Qué media docena de cosas, si las cambiaras, mejorarían radicalmente tus resultados? (separa cada una con una coma)", #esto se agregó en V2
            "¿Cómo piensas mejorar esas habilidades?",
            "¿Cuántos inscritos planeas lograr este ciclo?",
            "¿Cuántos puntos planeas lograr este ciclo?",
            "¿Cuántos matches planeas lograr este ciclo?",
            "¿Cuál es tu meta para esta semana?",
            "¿Cuántas citas te comprometes a hacer cada semana?"
        ]

    def agregar_respuesta(self, pregunta, respuesta):
        self.plan[pregunta] = respuesta

    def generar_resumen(self):
        resumen = "\nResumen del Plan del Ciclo:\n"
        for pregunta, respuesta in self.plan.items():
            resumen += f"{pregunta}: {respuesta}\n"
        return resumen

    def generar_dataframe(self):
        return pd.DataFrame(list(self.plan.items()), columns=["Pregunta", "Respuesta"])

# Inicializar la instancia del plan
if 'plan_ciclo' not in st.session_state:
    st.session_state.plan_ciclo = PlanDelCiclo()

if 'indice' not in st.session_state:
    st.session_state.indice = 0

if 'nombre' not in st.session_state:
    st.session_state.nombre = ""

plan_ciclo = st.session_state.plan_ciclo
indice = st.session_state.indice
nombre = st.session_state.nombre

st.title("Plan del Ciclo")

# Preguntar el nombre al inicio
if nombre == "":
    nombre_input = st.text_input("Por favor, ingresa tu nombre:")
    if st.button("Continuar") and nombre_input.strip():
        st.session_state.nombre = nombre_input
        st.session_state.indice = 0  # Reiniciar el índice por si acaso
        st.rerun()

# Continuar con las preguntas del ciclo
elif indice < len(plan_ciclo.preguntas):
    pregunta_actual = plan_ciclo.preguntas[indice]

    # Barra de progreso
    total_preguntas = len(plan_ciclo.preguntas)
    progreso = indice / total_preguntas
    st.progress(progreso)

    # Pregunta con campo numérico o de texto
    if pregunta_actual in [
        "¿Cuántos inscritos tuyos directos lograste este ciclo?",
        "¿Cuántos inscritos aparte de los tuyos, se inscribieron en tu equipo?",
        "¿Cuántos matches hiciste en el ciclo anterior?",
        "¿Cuántos matches piensas hacer en el nuevo ciclo?",
        "¿Cuánto necesitas ganar este ciclo?",
        "¿Cuánto ganaste en el ciclo anterior?",
        "¿Cuántos zafiros nuevos planeas lograr?",
        "¿Cuántos inscritos planeas lograr este ciclo?",
        "¿Cuántos puntos planeas lograr este ciclo?",
        "¿Cuántos matches planeas lograr este ciclo?",
        "¿Cuántas citas te comprometes a hacer cada semana?",
	"¿De quién voy a ser runner y cada cuanto me voy a reportar con esa persona?",
    ]:
        respuesta = st.number_input(pregunta_actual, value=0)
    else:
        respuesta = st.text_input(pregunta_actual)

    # Avanzar con el botón "Responder"
    if st.button("Responder"):
        plan_ciclo.agregar_respuesta(pregunta_actual, respuesta)
        st.session_state.indice += 1
        st.rerun()

# Si no hay más preguntas, mostrar el resumen
if indice >= len(plan_ciclo.preguntas):
    st.write(f"¡Gracias, {nombre}! Has completado el plan del ciclo.")
    resumen = plan_ciclo.generar_resumen()
    st.text_area("Resumen", resumen)

    # Opción de descargar el reporte en Excel
    if st.button("Descargar Reporte en Excel"):
        df = plan_ciclo.generar_dataframe()
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Plan del Ciclo')
        st.download_button(label="Descargar el reporte en Excel", data=buffer, file_name=f"reporte_plan_ciclo_{nombre}.xlsx")

    # Mostrar globos al completar
    st.balloons()

