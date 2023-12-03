class Weightconverter:
    def __init__(self, weight):
        self.weight = weight

    def kg_to_lbs(self):
        return self.weight * 2.2
    
    def lbs_to_kg(self):
        return self.weight / 2.2
    
def get_int(x):
    while True:
        try:
            user_input = float(input(x))
        except ValueError:
                print("Error: Please enter a valid number.")
        else:
                return user_input



def main():
    print("""Weight Converter:
            Kilograms(kg)
            Pounds(lbs)""")
    weight = get_int("Enter weight: ")
    unit = input("Enter unit (kg/lbs): ").lower()
    while unit not in ("kg", "lbs"):
        print("Invalid input.")
        unit = input("Enter unit (kg/lbs): ").lower()
    converter = Weightconverter(weight)
    if unit == 'kg':
         result = converter.kg_to_lbs()
         print(f"Weigh in lbs = {result}")
    elif unit == 'lbs':
         result = converter.lbs_to_kg()
         print(f"Weight in kg = {round(result):.2f}")


if __name__ == "__main__":
     main()