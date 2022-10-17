def formula_without_entry_fee(sell, buy, tax, fee):
    fee /= 100
    tax /= 100
    return (sell - buy * tax) / (1 - tax - fee)


def formula_with_entry_fee(Arms, Ready, Initial):
    # A - R = Final - (Final - I)*0.13
    return (Arms - Ready - 0.13*Initial) / (1-0.13)
