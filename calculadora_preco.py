import tkinter as tk
from tkinter import messagebox

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
tk.Label(root, text="Preço de Custo com Impostos (R$):").grid(row=0, column=0)
entry_preco_custo = tk.Entry(root, textvariable=preco_custo_var)
entry_preco_custo.grid(row=0, column=1)

tk.Label(root, text="IPI (%):").grid(row=1, column=0)
entry_ipi = tk.Entry(root, textvariable=ipi_var)
entry_ipi.grid(row=1, column=1)

tk.Label(root, text="ST (%):").grid(row=2, column=0)
entry_st = tk.Entry(root, textvariable=st_var)
entry_st.grid(row=2, column=1)

tk.Label(root, text="DIFAL (%):").grid(row=3, column=0)
entry_difal = tk.Entry(root, textvariable=difal_var)
entry_difal.grid(row=3, column=1)

tk.Label(root, text="Comissão Patrocínio (%):").grid(row=4, column=0)
entry_comissao_patrocinio = tk.Entry(root, textvariable=comissao_patrocinio_var)
entry_comissao_patrocinio.grid(row=4, column=1)

tk.Label(root, text="Frete (R$):").grid(row=5, column=0)
entry_frete = tk.Entry(root, textvariable=frete_var)
entry_frete.grid(row=5, column=1)

tk.Label(root, text="Simples Nacional (%):").grid(row=6, column=0)
entry_simples = tk.Entry(root, textvariable=simples_var)
entry_simples.grid(row=6, column=1)

tk.Label(root, text="Comissão Mercado Livre (%):").grid(row=7, column=0)
entry_comissao_ml = tk.Entry(root, textvariable=comissao_ml_var)
entry_comissao_ml.grid(row=7, column=1)

tk.Label(root, text="Taxa Fixa ML + Frete (R$):").grid(row=8, column=0)
entry_taxa_fixa_ml = tk.Entry(root, textvariable=taxa_fixa_ml_var)
entry_taxa_fixa_ml.grid(row=8, column=1)

tk.Label(root, text="Margem de Contribuição (%):").grid(row=9, column=0)
entry_margem_contribuicao = tk.Entry(root, textvariable=margem_contribuicao_var)
entry_margem_contribuicao.grid(row=9, column=1)

# Labels para exibir os resultados
resultado_valor_custo = tk.Label(root, text="")
resultado_valor_custo.grid(row=10, column=0, columnspan=2)

resultado_preco_venda = tk.Label(root, text="")
resultado_preco_venda.grid(row=11, column=0, columnspan=2)

resultado_lucro_liquido = tk.Label(root, text="")
resultado_lucro_liquido.grid(row=12, column=0, columnspan=2)

# Iniciar a interface
root.mainloop()
