def carregar_mensagens():
    if not ARQUIVO_MENSAGENS.exists():
        return []


    try:
        with open(ARQUIVO_MENSAGENS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []