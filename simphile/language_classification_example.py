"""
Here we're classifying the language of a string based on how closely it matches
examples of other languages
"""
from simphile import CompressionSimilarity, TextProcessor

# the string where we wish to detect the language
reference = "Tout est bien qui finit bien. Après la pluie, le beau temps."
# NOTE: Ideally these language examples would be large
# and representative examples of their language
language_examples = {
    "French": "Routes? Là où nous allons, nous n'avons pas besoin de routes.",
    "Spanish": "¿Carreteras? Donde vamos no necesitamos carreteras.",
    "English": "Roads? Where we're going we don't need roads.",
    "Korean": "dolo? uliga ganeun gos-eun dologa pil-yohaji anhseubnida.",
    "Hindi": "sadaken? ham jahaan ja rahe hain vahaan hamen sadakon kee jaroorat nahin hai."
}
# lower-casing all strings
processor = TextProcessor(lowercase=True)
# using compression similarity, which looks at character patterns
comparator = CompressionSimilarity(reference, processor)
# scoring the reference to each of the language strings
for language, language_example in language_examples.items():
    print(f"{language}: {comparator.score(language_example)}")
