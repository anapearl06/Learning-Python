class CoffeeUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " water , milk , honey , coffee beans "

cleaned = CoffeeUtils.clean_ingredients(raw)
print(cleaned)