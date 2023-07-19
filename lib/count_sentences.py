import re


class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        # Using regular expression to split the value into sentences
        sentences = re.split(r"[.!?]", self.value)
        # Removing empty strings resulting from multiple consecutive sentence separators
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)


# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # Output: 3