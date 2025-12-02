import requests

def render_with_kroki(input_path, output_path, format="png"):
    with open(input_path, "r", encoding="utf-8") as f:
        plantuml_code = f.read()

    url = f"https://kroki.io/plantuml/{format}"
    response = requests.post(url, data=plantuml_code.encode("utf-8"))

    if response.status_code != 200:
        raise RuntimeError(
            f"Error rendering {input_path} via Kroki: HTTP {response.status_code}"
        )

    with open(output_path, "wb") as out:
        out.write(response.content)

    print(f"[RENDER OK] {output_path} generated successfully!")