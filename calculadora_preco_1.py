import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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

        # Valor de Custo: (Preço de custo + IPI + ST + DIFAL + Frete) * 1.1
        valor_custo = (preco_custo + preco_custo * ipi + preco_custo * st + preco_custo * difal + frete) * 1.1

        # Preço de Venda: (Custo + Taxa Fixa) / (1 - Comissão ML - Margem de Contribuição - Simples)
        preco_venda = (valor_custo + taxa_fixa_ml) / (1 - comissao_ml - margem_contribuicao - simples)

        # Lucro Líquido: Preço de Venda - Custo - (Comissão ML * Preço Venda) - (Margem * Preço Venda) - Taxa Fixa
        lucro_liquido = preco_venda - valor_custo - comissao_ml * preco_venda - margem_contribuicao * preco_venda - taxa_fixa_ml

        # Exibir os resultados
        resultado_valor_custo['text'] = f"Valor de Custo: R${valor_custo:.2f}"
        resultado_preco_venda['text'] = f"Preço de Venda: R${preco_venda:.2f}"
        resultado_lucro_liquido['text'] = f"Lucro Líquido: R${lucro_liquido:.2f}"

    except ZeroDivisionError:
        # Caso a margem de contribuição seja 100%, evitar a divisão por zero
        messagebox.showerror("Erro de Cálculo", "A margem de contribuição não pode ser 100%.")

    except ValueError:
        # Quando algum valor de entrada não for numérico
        resultado_valor_custo['text'] = ""
        resultado_preco_venda['text'] = ""
        resultado_lucro_liquido['text'] = ""

# Função para processar os inputs da interface e calcular os valores automaticamente
def processar(*args):
    try:
        calcular_precos()
    except ValueError:
        # Ignorar entradas inválidas enquanto o usuário digita
        pass

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Preço e Lucro")
root.geometry("600x600")

# Carregar a imagem de fundo
image = Image.open("SO IMPORTADOS.jpg")
background_image = ImageTk.PhotoImage(image)

# Canvas para exibir a imagem de fundo
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Exibir a imagem no canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Adicionar o nome (campo onde aparece a pena)
canvas.create_text(300, 50, text="Calculadora de Preço e Lucro", font=("Arial", 24), fill="white")

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

# Configuração dos campos de entrada
canvas.create_text(150, 100, text="Preço de Custo com Impostos (R$):", font=("Arial", 12), fill="white")
entry_preco_custo = tk.Entry(root, textvariable=preco_custo_var)
canvas.create_window(400, 100, window=entry_preco_custo)

canvas.create_text(150, 130, text="IPI (%):", font=("Arial", 12), fill="white")
entry_ipi = tk.Entry(root, textvariable=ipi_var)
canvas.create_window(400, 130, window=entry_ipi)

canvas.create_text(150, 160, text="ST (%):", font=("Arial", 12), fill="white")
entry_st = tk.Entry(root, textvariable=st_var)
canvas.create_window(400, 160, window=entry_st)

canvas.create_text(150, 190, text="DIFAL (%):", font=("Arial", 12), fill="white")
entry_difal = tk.Entry(root, textvariable=difal_var)
canvas.create_window(400, 190, window=entry_difal)

canvas.create_text(150, 220, text="Comissão Patrocínio (%):", font=("Arial", 12), fill="white")
entry_comissao_patrocinio = tk.Entry(root, textvariable=comissao_patrocinio_var)
canvas.create_window(400, 220, window=entry_comissao_patrocinio)

canvas.create_text(150, 250, text="Frete (R$):", font=("Arial", 12), fill="white")
entry_frete = tk.Entry(root, textvariable=frete_var)
canvas.create_window(400, 250, window=entry_frete)

canvas.create_text(150, 280, text="Simples Nacional (%):", font=("Arial", 12), fill="white")
entry_simples = tk.Entry(root, textvariable=simples_var)
canvas.create_window(400, 280, window=entry_simples)

canvas.create_text(150, 310, text="Comissão Mercado Livre (%):", font=("Arial", 12), fill="white")
entry_comissao_ml = tk.Entry(root, textvariable=comissao_ml_var)
canvas.create_window(400, 310, window=entry_comissao_ml)

canvas.create_text(150, 340, text="Taxa Fixa ML + Frete (R$):", font=("Arial", 12), fill="white")
entry_taxa_fixa_ml = tk.Entry(root, textvariable=taxa_fixa_ml_var)
canvas.create_window(400, 340, window=entry_taxa_fixa_ml)

canvas.create_text(150, 370, text="Margem de Contribuição (%):", font=("Arial", 12), fill="white")
entry_margem_contribuicao = tk.Entry(root, textvariable=margem_contribuicao_var)
canvas.create_window(400, 370, window=entry_margem_contribuicao)

# Labels para exibir os resultados
resultado_valor_custo = tk.Label(root, text="", bg="lightgray")
canvas.create_window(300, 410, window=resultado_valor_custo)

resultado_preco_venda = tk.Label(root, text="", bg="lightgray")
canvas.create_window(300, 440, window=resultado_preco_venda)

resultado_lucro_liquido = tk.Label(root, text="", bg="lightgray")
canvas.create_window(300, 470, window=resultado_lucro_liquido)

# Iniciar a interface
root.mainloop()
