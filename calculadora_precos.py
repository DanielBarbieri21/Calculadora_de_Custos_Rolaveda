import sys
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

# Função para obter o caminho do recurso (imagem) no executável
def resource_path(relative_path):
    """Obter o caminho absoluto do recurso, seja no modo dev ou executável"""
    try:
        base_path = sys._MEIPASS  # PyInstaller cria uma pasta temporária e armazena o caminho nele
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Função para calcular o valor de custo, preço de venda e lucro líquido
def calcular_precos():
    try:
        # Obter os valores dos inputs
        preco_custo = float(entry_preco_custo.get() or 0)
        ipi = float(entry_ipi.get() or 0) / 100
        st = float(entry_st.get() or 0) / 100
        difal = float(entry_difal.get() or 0) / 100
        comissao_patrocinio = float(entry_comissao_patrocinio.get() or 0) / 100
        frete = float(entry_frete.get() or 0)
        simples = float(entry_simples.get() or 0) / 100
        comissao_ml = float(entry_comissao_ml.get() or 0) / 100
        taxa_fixa_ml = float(entry_taxa_fixa_ml.get() or 0)
        margem_contribuicao = float(entry_margem_contribuicao.get() or 0) / 100

        # Calcular o valor de custo
        valor_custo = (preco_custo + (preco_custo * ipi) + (preco_custo * st) + (preco_custo * difal) + frete) * 1.1

        # Calcular o preço de venda
        preco_venda = (valor_custo + taxa_fixa_ml) / (1 - simples - comissao_ml - margem_contribuicao)

        # Calcular o lucro líquido
        lucro_liquido = (
            preco_venda 
            - valor_custo 
            - (simples * preco_venda) 
            - (comissao_ml * preco_venda) 
            - taxa_fixa_ml
        )

        # Calcular a margem de contribuição
        margem_contribuicao_resultado = (lucro_liquido / preco_venda) * 100 if preco_venda > 0 else 0

        # Exibir os resultados
        resultado_valor_custo['text'] = f"Valor de Custo: R${valor_custo:.2f}"
        resultado_preco_venda['text'] = f"Preço de Venda: R${preco_venda:.2f}"
        resultado_lucro_liquido['text'] = f"Lucro Líquido: R${lucro_liquido:.2f}"
        resultado_margem_contribuicao['text'] = f"Margem de Contribuição: {margem_contribuicao_resultado:.2f}%"

    except ZeroDivisionError:
        messagebox.showerror("Erro de Cálculo", "A margem de contribuição não pode ser 100%.")

    except ValueError:
        resultado_valor_custo['text'] = ""
        resultado_preco_venda['text'] = ""
        resultado_lucro_liquido['text'] = ""
        resultado_margem_contribuicao['text'] = ""

# Função para processar os inputs da interface e calcular os valores automaticamente
def processar(*args):
    try:
        calcular_precos()
    except ValueError:
        pass  # Ignorar entradas inválidas enquanto o usuário digita

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Preço e Lucro")

# Carregar a imagem de fundo
image_path = resource_path("SO IMPORTADOS.jpg")
try:
    image = Image.open(image_path)
    bg_image = ImageTk.PhotoImage(image)  # Definir bg_image corretamente
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    bg_image = None  # Definir bg_image como None se falhar

# Criar um Canvas e adicionar a imagem de fundo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

if bg_image:
    canvas.create_image(0, 0, image=bg_image, anchor="nw")  # Adicionar a imagem de fundo

# Associar os campos de entrada a variáveis Tkinter
preco_custo_var = tk.StringVar()
ipi_var = tk.StringVar()
st_var = tk.StringVar()
difal_var = tk.StringVar()
comissao_patrocinio_var = tk.StringVar()
frete_var = tk.StringVar()
simples_var = tk.StringVar()
comissao_ml_var = tk.StringVar()
taxa_fixa_ml_var = tk.StringVar()
margem_contribuicao_var = tk.StringVar()

# Configurar o rastreamento das alterações
preco_custo_var.trace("w", processar)
ipi_var.trace("w", processar)
st_var.trace("w", processar)
difal_var.trace("w", processar)
comissao_patrocinio_var.trace("w", processar)
frete_var.trace("w", processar)
simples_var.trace("w", processar)
comissao_ml_var.trace("w", processar)
taxa_fixa_ml_var.trace("w", processar)
margem_contribuicao_var.trace("w", processar)

# Configuração dos campos de entrada no canvas
tk.Label(canvas, text="Preço Custo (R$):").place(x=10, y=10)
entry_preco_custo = tk.Entry(canvas, textvariable=preco_custo_var)
entry_preco_custo.place(x=250, y=10)

tk.Label(canvas, text="IPI (%):").place(x=10, y=40)
entry_ipi = tk.Entry(canvas, textvariable=ipi_var)
entry_ipi.place(x=250, y=40)

tk.Label(canvas, text="ST (%):").place(x=10, y=70)
entry_st = tk.Entry(canvas, textvariable=st_var)
entry_st.place(x=250, y=70)

tk.Label(canvas, text="DIFAL (%):").place(x=10, y=100)
entry_difal = tk.Entry(canvas, textvariable=difal_var)
entry_difal.place(x=250, y=100)

tk.Label(canvas, text="Comissão Patrocínio (%):").place(x=10, y=130)
entry_comissao_patrocinio = tk.Entry(canvas, textvariable=comissao_patrocinio_var)
entry_comissao_patrocinio.place(x=250, y=130)

tk.Label(canvas, text="Frete (R$):").place(x=10, y=160)
entry_frete = tk.Entry(canvas, textvariable=frete_var)
entry_frete.place(x=250, y=160)

tk.Label(canvas, text="Simples (%):").place(x=10, y=190)
entry_simples = tk.Entry(canvas, textvariable=simples_var)
entry_simples.place(x=250, y=190)

tk.Label(canvas, text="Comissão ML (%):").place(x=10, y=220)
entry_comissao_ml = tk.Entry(canvas, textvariable=comissao_ml_var)
entry_comissao_ml.place(x=250, y=220)

tk.Label(canvas, text="Taxa Fixa ML + Frete (R$):").place(x=10, y=250)
entry_taxa_fixa_ml = tk.Entry(canvas, textvariable=taxa_fixa_ml_var)
entry_taxa_fixa_ml.place(x=250, y=250)

tk.Label(canvas, text="Margem de Contribuição (%):").place(x=10, y=280)
entry_margem_contribuicao = tk.Entry(canvas, textvariable=margem_contribuicao_var)
entry_margem_contribuicao.place(x=250, y=280)

# Labels para exibir os resultados com cores específicas
resultado_valor_custo = tk.Label(canvas, text="", bg="yellow")
resultado_valor_custo.place(x=10, y=310)

resultado_preco_venda = tk.Label(canvas, text="", bg="green")
resultado_preco_venda.place(x=10, y=340)

resultado_lucro_liquido = tk.Label(canvas, text="", bg="pink")
resultado_lucro_liquido.place(x=10, y=370)

resultado_margem_contribuicao = tk.Label(canvas, text="", bg="lightblue")
resultado_margem_contribuicao.place(x=10, y=400)

# Executar a interface
root.mainloop()
