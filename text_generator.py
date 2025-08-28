import random

# List of words to use in the text generation
WORDS = [
    "python", "code", "generate", "text", "simple", "example", "function", "random",
    "sentence", "words", "output", "create", "script", "easy", "project"
]

def generate_sentence(word_count=7):
    """Generate a random sentence with the specified number of words."""
    sentence = " ".join(random.choice(WORDS) for _ in range(word_count))
    return sentence.capitalize() + "."

def generate_paragraph(sentence_count=5, word_count=7):
    """Generate a paragraph with the specified number of sentences."""
    return " ".join(generate_sentence(word_count) for _ in range(sentence_count))

if __name__ == "__main__":
    print("Generated Sentence:")
    print(generate_sentence())
    print("\nGenerated Paragraph:")
    print(generate_paragraph())
