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

# Função para calcular automaticamente os preços com base nos campos de entrada
def calcular_precos(*args):
    try:
        # Obter os valores dos campos de entrada
        valor_custo = float(entry_valor_custo.get() or 0)
        percentual_venda = float(entry_percentual_venda.get() or 0) / 100
        taxa_shops_classico = float(entry_taxa_shops_classico.get() or 0) / 100
        taxa_shops_premium = float(entry_taxa_shops_premium.get() or 0) / 100
        taxa_ml_classico = float(entry_taxa_ml_classico.get() or 0) / 100
        taxa_ml_premium = float(entry_taxa_ml_premium.get() or 0) / 100
        taxa_site = float(entry_taxa_site.get() or 0) / 100
        taxa_cliente_fisica_oficina = float(entry_taxa_cliente_fisica_oficina.get() or 0) / 100
        valor_frete = float(entry_valor_frete.get() or 0)

        # Calcular o preço base com o percentual de venda
        preco_base = valor_custo * (1 + percentual_venda)

        # Calcular os preços para cada modalidade
        preco_shops_classico = preco_base * (1 + taxa_shops_classico) + valor_frete
        preco_shops_premium = preco_base * (1 + taxa_shops_premium) + valor_frete
        preco_ml_classico = preco_base * (1 + taxa_ml_classico) + valor_frete
        preco_ml_premium = preco_base * (1 + taxa_ml_premium) + valor_frete
        preco_site = preco_base * (1 + taxa_site) + valor_frete
        preco_cliente_fisica_oficina = preco_base * (1 + taxa_cliente_fisica_oficina) + valor_frete

        # Exibir os resultados
        resultado_shops_classico['text'] = f"Shops Clássico: R${preco_shops_classico:.2f}"
        resultado_shops_premium['text'] = f"Shops Premium: R${preco_shops_premium:.2f}"
        resultado_ml_classico['text'] = f"ML Clássico: R${preco_ml_classico:.2f}"
        resultado_ml_premium['text'] = f"ML Premium: R${preco_ml_premium:.2f}"
        resultado_site['text'] = f"Site: R${preco_site:.2f}"
        resultado_cliente_fisica_oficina['text'] = f"Cliente Física/Oficina: R${preco_cliente_fisica_oficina:.2f}"

    except ValueError:
        messagebox.showerror("Erro de Cálculo", "Verifique se todos os valores inseridos são numéricos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Preços")

# Carregar a imagem de fundo
image_path = resource_path("SO IMPORTADOS.jpg")
try:
    image = Image.open(image_path)
    bg_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    bg_image = None

# Criar um Canvas e adicionar a imagem de fundo
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

if bg_image:
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Associar os campos de entrada a variáveis Tkinter
valor_custo_var = tk.StringVar()
percentual_venda_var = tk.StringVar()
taxa_shops_classico_var = tk.StringVar()
taxa_shops_premium_var = tk.StringVar()
taxa_ml_classico_var = tk.StringVar()
taxa_ml_premium_var = tk.StringVar()
taxa_site_var = tk.StringVar()
taxa_cliente_fisica_oficina_var = tk.StringVar()
valor_frete_var = tk.StringVar()

# Configurar o rastreamento das alterações
valor_custo_var.trace("w", calcular_precos)
percentual_venda_var.trace("w", calcular_precos)
taxa_shops_classico_var.trace("w", calcular_precos)
taxa_shops_premium_var.trace("w", calcular_precos)
taxa_ml_classico_var.trace("w", calcular_precos)
taxa_ml_premium_var.trace("w", calcular_precos)
taxa_site_var.trace("w", calcular_precos)
taxa_cliente_fisica_oficina_var.trace("w", calcular_precos)
valor_frete_var.trace("w", calcular_precos)

# Configuração dos campos de entrada no Canvas
tk.Label(canvas, text="Valor Custo (R$):").place(x=10, y=10)
entry_valor_custo = tk.Entry(canvas, textvariable=valor_custo_var)
entry_valor_custo.place(x=250, y=10)

tk.Label(canvas, text="Percentual de Venda (%):").place(x=10, y=40)
entry_percentual_venda = tk.Entry(canvas, textvariable=percentual_venda_var)
entry_percentual_venda.place(x=250, y=40)

tk.Label(canvas, text="Taxa Shops Clássico (2%):").place(x=10, y=70)
entry_taxa_shops_classico = tk.Entry(canvas, textvariable=taxa_shops_classico_var)
entry_taxa_shops_classico.place(x=250, y=70)

tk.Label(canvas, text="Taxa Shops Premium 3X (8%):").place(x=10, y=100)
entry_taxa_shops_premium = tk.Entry(canvas, textvariable=taxa_shops_premium_var)
entry_taxa_shops_premium.place(x=250, y=100)

tk.Label(canvas, text="Taxa ML Clássico (12%):").place(x=10, y=130)
entry_taxa_ml_classico = tk.Entry(canvas, textvariable=taxa_ml_classico_var)
entry_taxa_ml_classico.place(x=250, y=130)

tk.Label(canvas, text="Taxa ML Premium 10X (17%):").place(x=10, y=160)
entry_taxa_ml_premium = tk.Entry(canvas, textvariable=taxa_ml_premium_var)
entry_taxa_ml_premium.place(x=250, y=160)

tk.Label(canvas, text="Taxa Site (10%):").place(x=10, y=190)
entry_taxa_site = tk.Entry(canvas, textvariable=taxa_site_var)
entry_taxa_site.place(x=250, y=190)

tk.Label(canvas, text="Taxa Cliente Física/Oficina (10%, 15%, 20%):").place(x=10, y=220)
entry_taxa_cliente_fisica_oficina = tk.Entry(canvas, textvariable=taxa_cliente_fisica_oficina_var)
entry_taxa_cliente_fisica_oficina.place(x=250, y=220)

tk.Label(canvas, text="Valor Frete (R$):").place(x=10, y=250)
entry_valor_frete = tk.Entry(canvas, textvariable=valor_frete_var)
entry_valor_frete.place(x=250, y=250)

# Labels para exibir os resultados
resultado_shops_classico = tk.Label(canvas, text="", bg="yellow")
resultado_shops_classico.place(x=10, y=290)

resultado_shops_premium = tk.Label(canvas, text="", bg="green")
resultado_shops_premium.place(x=10, y=320)

resultado_ml_classico = tk.Label(canvas, text="", bg="pink")
resultado_ml_classico.place(x=10, y=350)

resultado_ml_premium = tk.Label(canvas, text="", bg="lightblue")
resultado_ml_premium.place(x=10, y=380)

resultado_site = tk.Label(canvas, text="", bg="orange")
resultado_site.place(x=10, y=410)

resultado_cliente_fisica_oficina = tk.Label(canvas, text="", bg="lightgray")
resultado_cliente_fisica_oficina.place(x=10, y=440)

# Executar a interface
root.mainloop()
