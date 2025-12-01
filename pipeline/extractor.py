from utils import call_llm


with open("data/study_case.txt") as f:
    text = f.read()

prompt = f"""
Você é um extrator formal de semântica textual aplicado à engenharia de software.

Sua tarefa é analisar o texto abaixo e extrair um conjunto estruturado de elementos conceituais que representam o domínio descrito.  
Esses elementos servirão como fonte de verdade para gerar diagramas UML nas etapas seguintes do pipeline.

=== PRINCÍPIOS FUNDAMENTAIS ===

Você deve extrair SOMENTE informações que estejam explícita ou implicitamente ANCORADAS no texto.
As seguintes regras definem o que você deve e o que não deve inferir:

# PERMITIDO (INFERÊNCIA CONTROLADA)

Você pode extrair como entidades ou ações:
- participantes mencionados explicitamente;
- conceitos que aparecem no texto mesmo que não estejam formalizados como classes;
- ações descritas por frases verbais explícitas;
- interações claramente descritas entre dois elementos citados;
- regras de negócio textualmente descritas.

# PROIBIDO (INFERÊNCIA CRIATIVA)

- Inventar qualquer entidade, ator, evento ou relação não presente no texto;
- Criar nomes novos ou interpretar funcionalidades adicionais;
- Deduzir atributos, métodos ou classes não mencionados;
- Transformar conceitos genéricos em estruturas técnicas não mencionadas no texto.

// FORMATO DE SAÍDA

Retorne EXCLUSIVAMENTE um JSON válido, com a estrutura:

{
  "atores": [],               // participantes externos mencionados no texto
  "entidades": [],            // conceitos substantivos relevantes do domínio descrito no texto
  "eventos": [],              // ações explícitas nas quais alguém realiza algo
  "regras_de_negocio": [],    // condições, restrições ou políticas explicitamente mencionadas
  "relacoes_textuais": []     // interações explícitas no formato:
                              // {"de": "...", "para": "...", "acao": "..."}
}

// REGRAS FINAIS

- Não resuma o texto.
- Não explique nada.
- Não inclua comentários.
- Não altere termos ou nomes.
- Não gere nenhum conteúdo fora do JSON.
- O JSON deve ser estritamente válido.

-> TEXTO A SER ANALISADO:
{text}
"""

output = call_llm(prompt)

with open("data/root.json", "w") as f:
    f.write(output)
