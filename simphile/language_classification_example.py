"""
Here we're classifying the language of a string based on how closely it matches
examples of other languages
"""
from simphile import CompressionSimilarity, TextProcessor

# the string where we wish to detect the language
reference = "Après la pluie, le beau temps."
# NOTE: Ideally these language examples would be large
# and representative examples of their language
language_examples = {
    "French": "Aujourd'hui, je me considère comme l'homme le plus chanceux de la terre",
    "Spanish": "Hoy me considero el hombre más afortunado sobre la faz de la tierra",
    "English": "Today, I consider myself the luckiest man on the face of the earth",
    "Korean": "oneul naneun jigusang-eseo gajang un-i joh-eun salam-ilago saeng-gaghabnida",
    "Hindi": "aaj main khud ko duniya ka sabase bhaagyashaalee aadamee maanata hoon"
}
# lower-casing all strings
processor = TextProcessor(lowercase=True)
# using compression similarity, which looks at character patterns
comparator = CompressionSimilarity(reference, processor)
# scoring the reference to each of the language strings
for language, language_example in language_examples.items():
    print(f"{language}: {comparator.score(language_example)}")
