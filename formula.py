def formula_with_percent(sell, buy, tax, fee):
    return (sell - buy * tax) / (1 - tax - fee)


def formula_without_percent(sell, buy, tax, fee):
    return (sell + fee - buy * tax) / (1 - tax)
