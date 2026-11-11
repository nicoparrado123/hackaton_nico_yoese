import sys, json

def leer_stream_nico():
    sys.stdout.reconfigure(encoding="utf-8")
    pedazos_nico = {}
    tokens_in_nico = tokens_out_nico = 0
    motivo_nico = None
    for renglon in sys.stdin.read().splitlines():
        if not renglon.startswith("data:"):
            continue
        evento = json.loads(renglon[5:].strip())
        clase = evento["type"]
        if clase == "message_start":
            pedazos_nico = {}
            uso = evento["message"]["usage"]
            tokens_in_nico = uso["input_tokens"]
            tokens_out_nico = uso.get("output_tokens", 0)
            motivo_nico = None
        elif clase == "content_block_start":
            pedazos_nico[evento["index"]] = evento["content_block"].get("text", "")
        elif clase == "content_block_delta" and evento["delta"]["type"] == "text_delta":
            pos = evento["index"]
            pedazos_nico[pos] = pedazos_nico.get(pos, "") + evento["delta"]["text"]
        elif clase == "message_delta":
            motivo_nico = evento["delta"]["stop_reason"]
            tokens_out_nico = evento["usage"]["output_tokens"]
        elif clase == "message_stop":
            completo = "".join(pedazos_nico[k] for k in sorted(pedazos_nico))
            print(f"texto: {completo}")
            print(f"stop_reason: {motivo_nico}")
            print(f"input_tokens: {tokens_in_nico}")
            print(f"output_tokens: {tokens_out_nico}")

leer_stream_nico()
