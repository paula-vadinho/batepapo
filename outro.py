def salvar_mensagens(mensagens):
    with open(ARQUIVO_MENSAGENS, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, indent=4, ensure_ascii=False)