"""
BMI Calculator using Python
---------------------------
A simple program to calculate Body Mass Index (BMI)
based on user input for weight and height.

Features:
- Accepts user input (weight in kg, height in meters)
- Calculates BMI
- Displays category: Underweight, Normal, Overweight, or Obese
"""

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight / (height * height)"""
    return weight / (height ** 2)


def bmi_category(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("⚖️  BMI Calculator")
    print("-------------------------")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        if weight <= 0 or height <= 0:
            print("Please enter positive values for weight and height.")
            return

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
