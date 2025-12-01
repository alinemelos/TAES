from utils import call_llm
import json


with open("data/root.json") as f:
    root = json.load(f)

usecase = open("data/usecase.puml").read()
classes = open("data/classes.puml").read()

prompt = f"""
Gere um diagrama de SEQUÊNCIA em PlantUML EXCLUSIVAMENTE a partir da entrada, que consiste em:
1) Um JSON contendo os elementos conceituais extraídos diretamente do texto do estudo de caso.
2) Um diagrama de CASO DE USO derivado desse JSON.
3) Um diagrama de CLASSES derivado do caso de uso e das entidades do JSON.

O diagrama de sequência deve refletir:
- o fluxo funcional indicado pelo diagrama de CASO DE USO;
- as interações possíveis dadas pelas classes, métodos e relações do diagrama de CLASSES;
- e as relações e eventos textuais presentes no JSON.

=== REGRAS ===

1. Não crie novos atores, classes, objetos ou entidades. 
Use exclusivamente os elementos presentes nas entradas.

2. Não invente métodos. 
SOMENTE use métodos já existentes no diagrama de classes.

3. Não crie mensagens, operações ou interações que não sejam compatíveis com o:
- JSON,
- diagrama de caso de uso ou
- o diagrama de classes.

4. A sequência deve representar um fluxo coerente que:
- inicia pelo ator principal do caso de uso;
- segue as ações textualmente mencionadas no JSON;
- utiliza métodos válidos das classes.

5. Preserve todos os nomes exatamente como aparecem.

6. O resultado final deve ser um diagrama UML em PlantUML válido, sem explicações adicionais.

### JSON (fonte de verdade):
{json.dumps(root, indent=2)}

### Diagrama de caso de uso:
{usecase}

### Diagrama de classes:
{classes}

Retorne SOMENTE um código PlantUML válido.
"""

puml = call_llm(prompt)

with open("data/sequence.puml", "w") as f:
    f.write(puml)