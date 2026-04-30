import streamlit as st
import calculadora as calc

st.image("https://cdn-blog.superprof.com/blog_br/wp-content/uploads/2016/11/como-calcular-rapidamente.jpg.webp", width=1000)
st.title("CALCULADORA 🧮")

numero1 = st.number_input("Digite o primeiro número: ",step=0.1,value=None)
numero2 = st.number_input("Digite o segundo número: ",step=0.1,value=None)
operacao = st.selectbox("Selecione a operação",["+","-","*","/"])

if st.button("Calcular"):
    resultado = calc.calcular(numero1, numero2, operacao)
    st.success(f"Resultado: {resultado}")
    if resultado == 67:
        st.image("https://previews.123rf.com/images/kostiuchenko/kostiuchenko1701/kostiuchenko170100206/69868667-67-sixty-seven-numeral-imitation-glass-and-a-blazing-fire-isolated-on-white-background.jpg")