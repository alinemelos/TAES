from utils import call_llm


with open("data/study_case.txt") as f:
    text = f.read()

prompt = f"""
You are a formal extractor of textual semantics applied to software engineering.

Your task is to analyze the text below and extract a structured set of conceptual elements that represent the described domain.
These elements will serve as a source of truth to generate UML diagrams in later stages of the pipeline.

# FUNDAMENTAL PRINCIPLES

You must extract ONLY information that is explicitly or implicitly ANCHORED in the text.
The following rules define what you must and must not infer:

## ALLOWED (CONTROLLED INFERENCE)

You may extract as entities or actions:
- participants explicitly mentioned;
- concepts that appear in the text even if not formalized as classes;
- actions described by explicit verbal phrases;
- interactions clearly described between two cited elements;
- business rules textually described.

## PROHIBITED (CREATIVE INFERENCE)
-Inventing any entity, actor, event, or relationship not present in the text;
- Creating new names or interpreting additional functionalities;
- Deducing attributes, methods, or classes not mentioned;
- Turning generic concepts into technical structures not mentioned in the text.

# OUTPUT FORMAT

Return EXCLUSIVELY valid JSON, with the structure:
curly-braces
"actors": [], // external participants mentioned in the text
"entities": [], // substantive concepts relevant to the domain described in the text
"events": [], // explicit actions in which someone performs something
"business_rules": [], // conditions, constraints, or policies explicitly mentioned
"textual_relations": [] // explicit interactions in the format curly-brace"from": "...", "to": "...", "action": "..."curly-brace
curly-braces

# FINAL RULES

- Do not summarize the text.
- Do not explain anything.
- Do not include comments.
- Do not alter terms or names.
- Do not generate any content outside the JSON.
- The JSON must be strictly valid.

<<TEXT TO BE ANALYZED:>>
{text}
"""

output = call_llm(prompt)

with open("data/root.json", "w") as f:
    f.write(output)
