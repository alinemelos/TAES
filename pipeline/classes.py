from utils import call_llm
import json


with open("data/root.json") as f:
    root = json.load(f)

usecase = open("data/usecase.puml").read()

prompt = f"""
Gere um diagrama de CLASSES em PlantUML EXCLUSIVAMENTE a partir da entrada, que consiste em:
1) Um JSON contendo os elementos conceituais extraídos diretamente do texto do estudo de caso.
2) Um diagrama de CASO DE USO derivado desse JSON.

O diagrama de classes deve derivar SOMENTE desses dois elementos.
Não adicione nada que não esteja presente no JSON ou no diagrama de caso de uso.

=== REGRAS ===

1. Classes podem ser derivadas de:
   - entidades presentes no JSON ("entidades");
   - participantes externos relevantes ("atores");
   - elementos conceituais associados a ações explícitas do JSON ("eventos").

2. Você NÃO deve:
   - inventar novas classes, atributos, métodos ou relacionamentos;
   - inferir funcionalidades não descritas no JSON;
   - reinterpretar o diagrama de caso de uso;
   - criar abstrações além das mencionadas no JSON.

3. Atributos devem ser derivados APENAS de substantivos ou informações descritivas presentes no JSON.
Não invente atributos técnicos ou generalizações.

4. Métodos devem ser derivados APENAS dos eventos ou ações explícitas no JSON.
Use nomes simples, textualmente baseados no JSON.

5. Relacionamentos entre classes devem refletir relações textuais do JSON e interações derivadas do diagrama de caso de uso.
Evite relações não mencionadas.

6. O resultado final deve ser um diagrama UML em PlantUML válido, sem explicações adicionais.

### JSON (fonte de verdade):
{json.dumps(root, indent=2)}

### Diagrama de caso de uso:
{usecase}

Retorne SOMENTE um código PlantUML válido.
"""

puml = call_llm(prompt)

with open("data/classes.puml", "w") as f:
    f.write(puml)
