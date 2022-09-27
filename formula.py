def formula_with_percent(sell, buy, tax, fee):
    fee /= 100
    tax /= 100
    return (sell - buy * tax) / (1 - tax - fee)


def formula_without_percent(sell, buy, tax, fee):
    tax /= 100
    return (sell + fee - buy * tax) / (1 - tax)
