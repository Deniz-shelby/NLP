from pathlib import Path
import spacy

output_dir = Path("./ner_models/")
# nlp.to_disk(output_dir)
# print("Saved correctly!")

"""

STEP 3 - TEST THE UPDATED MODEL

"""

print("Loading model...")
nlp_updated = spacy.load(output_dir)

# old sentence, old word
doc = nlp_updated("My dream is to buy a Volkswagen!.")
print("entities:", [(ent.text, ent.label_) for ent in doc.ents])

# old sentence, new word
doc = nlp_updated("My dream is to buy a Lotus!")
print("entities:", [(ent.text, ent.label_) for ent in doc.ents])

# new sentence, new word
doc = nlp_updated("I will buy a Pontiac after i get a job")
print("entities:", [(ent.text, ent.label_) for ent in doc.ents])

# new sentence, no word
doc = nlp_updated("Fabio likes full-stack development")
print("entities:", [(ent.text, ent.label_) for ent in doc.ents])
