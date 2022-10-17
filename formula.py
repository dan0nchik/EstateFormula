def formula_without_entry_fee(sell, buy, tax, fee):
    fee /= 100
    tax /= 100
    return (sell - buy * tax) / (1 - tax - fee)


def formula_with_entry_fee(arms, dkp_seller, initial):
    # A - Ready = Final - (Final - I)*0.13
    arms, dkp_seller, initial = int(arms), int(dkp_seller), int(initial)
    ready = (arms - dkp_seller) * 0.13
    return (arms - ready - 0.13 * initial) / (1 - 0.13)