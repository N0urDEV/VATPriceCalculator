def calculate_price_with_VAT():
    prixHorsTaxe = float(input("Please enter the price before tax for the product: "))
    categorieTVA = input("Please enter the VAT category of the product (A, B, or C): ").upper()

    if categorieTVA == "A":
        prixTTC = prixHorsTaxe + (prixHorsTaxe * 0.07)
    elif categorieTVA == "B":
        prixTTC = prixHorsTaxe + (prixHorsTaxe * 0.20)
    elif categorieTVA == "C":
        prixTTC = prixHorsTaxe + (prixHorsTaxe * 0.25)
    else:
        print("Invalid VAT category.")
        return

    print("The price including VAT for the product is", prixTTC, "dhs.")
calculate_price_with_VAT()
