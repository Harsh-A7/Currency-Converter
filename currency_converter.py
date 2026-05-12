import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

POPULAR_CURRENCIES = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "SGD", "AED", "CHF"]

def get_exchange_rates(base_currency):
    """Fetch exchange rates from the API for a given base currency."""
    try:
        response = requests.get(API_URL + base_currency)
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.exceptions.ConnectionError:
        print("\n  Error: No internet connection. Please check your network.")
        return None
    except requests.exceptions.HTTPError:
        print(f"\n  Error: Currency '{base_currency}' not found. Please try again.")
        return None
    except Exception as e:
        print(f"\n  Something went wrong: {e}")
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another using fetched rates."""
    if to_currency not in rates:
        print(f"\n  Error: Target currency '{to_currency}' is not supported.")
        return None
    converted = amount * rates[to_currency]
    return round(converted, 2)


def show_popular_rates(base_currency, rates):
    """Show exchange rates for popular currencies."""
    print(f"\n  Popular rates for 1 {base_currency}:")
    print("  " + "-" * 30)
    for currency in POPULAR_CURRENCIES:
        if currency != base_currency and currency in rates:
            print(f"  {currency:<6} = {rates[currency]:>10.4f}")
    print()


def print_banner():
    print("\n" + "=" * 45)
    print("        💱  Currency Converter  💱")
    print("    Powered by exchangerate-api.com")
    print("=" * 45)


def main():
    print_banner()

    while True:
        print("\nOptions:")
        print("  [1] Convert currency")
        print("  [2] View popular exchange rates")
        print("  [3] Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "3":
            print("\n  Goodbye! 👋\n")
            break

        elif choice == "1":
            from_currency = input("\n  From currency (e.g. USD): ").strip().upper()
            to_currency   = input("  To currency   (e.g. INR): ").strip().upper()

            try:
                amount = float(input("  Amount: ").strip())
            except ValueError:
                print("\n  Error: Please enter a valid number.")
                continue

            print(f"\n  Fetching rates for {from_currency}...")
            rates = get_exchange_rates(from_currency)

            if rates:
                result = convert_currency(amount, from_currency, to_currency, rates)
                if result is not None:
                    print(f"\n  ✅  {amount:,.2f} {from_currency}  =  {result:,.2f} {to_currency}")

        elif choice == "2":
            base = input("\n  Base currency (e.g. USD): ").strip().upper()
            print(f"\n  Fetching rates for {base}...")
            rates = get_exchange_rates(base)
            if rates:
                show_popular_rates(base, rates)

        else:
            print("\n  Invalid choice. Please enter 1, 2, or 3.")

        again = input("  Do another conversion? [Y/n]: ").strip().lower()
        if again in ("n", "no"):
            print("\n  Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()
