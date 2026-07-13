def celsius_to_fahrenheit(c):
      """Convert Celsius to Fahrenheit."""
      return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
      """Convert Fahrenheit to Celsius."""
      return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
      """Convert Celsius to Kelvin."""
      return c + 273.15


def kelvin_to_celsius(k):
      """Convert Kelvin to Celsius."""
      return k - 273.15


CONVERSIONS = {
      "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "C", "F"),
      "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "F", "C"),
      "3": ("Celsius to Kelvin",     celsius_to_kelvin,     "C", "K"),
      "4": ("Kelvin to Celsius",     kelvin_to_celsius,     "K", "C"),
}


def temperature_converter():
      """Interactive temperature unit converter."""
      print("=== Temperature Converter ===")
      for key, (label, _, src, dst) in CONVERSIONS.items():
                print(f"  {key}. {label} ({src} -> {dst})")
            choice = input("Select conversion (1-4): ").strip()
    if choice not in CONVERSIONS:
              print("Invalid choice.")
              return
          label, func, src, dst = CONVERSIONS[choice]
    value = float(input(f"Enter temperature in {src}: "))
    result = func(value)
    print(f"Result: {value} {src} = {result:.2f} {dst}")


if __name__ == "__main__":
      temperature_converter()
