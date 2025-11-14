@app.get("/buscar")
def buscar_operadora(nome: str = Query(...)):
    global df
    if df is None:
        raise HTTPException(
            status_code=500,
            detail="Dados da operadora não carregados. CSV pode estar faltando."
        )

    nome = nome.strip()
    if not nome:
        return {"mensagem": "Informe um nome válido para busca."}

    try:
        nome_lower = nome.lower()
        resultados = df[df["Razao_Social"].astype(str).str.lower().str.startswith(nome_lower, na=False)]

        if resultados.empty:
            return {"mensagem": f"Nenhum resultado encontrado para '{nome}'."}

        # ----------------- AQUI -----------------
        resultados_front = resultados[['Razao_Social', 'CNPJ', 'Modalidade']].rename(
            columns={'Razao_Social': 'Operadora'}
        )
        return resultados_front.to_dict(orient="records")
        # ---------------------------------------

    except KeyError as ke:
        raise HTTPException(status_code=500, detail=f"Erro de coluna: {str(ke)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")
