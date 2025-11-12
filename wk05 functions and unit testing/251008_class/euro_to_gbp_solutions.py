def convert_euro_to_gbp(amount_eur, rate):
    """
    """
    return amount_eur * rate

if __name__=="__main__":
    amount = float(input("Enter the amoount in Euros: "))
    rate = float(input("Enter the exchange rate (Euro to GBP): "))
    print(f"Converting {amount} in Euros to GBP: {convert_euro_to_gbp(amount)}")