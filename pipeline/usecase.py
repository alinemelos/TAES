from utils import call_llm
import json


root = json.load(open("data/root.json", "r"))

prompt = f"""
Gere um diagrama de CASO DE USO em PlantUML baseado EXCLUSIVAMENTE no JSON abaixo.
NÃO adicione elementos novos.

JSON:
{json.dumps(root, indent=2)}

O resultado final deve ser um diagrama UML em PlantUML válido, sem explicações adicionais.

Retorne SOMENTE um código PlantUML válido.
"""

puml = call_llm(prompt)

open("data/usecase.puml", "w").write(puml)