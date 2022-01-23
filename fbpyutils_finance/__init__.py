'''
Functions to perform financial calculations.

https://clubedospoupadores.com/educacao-financeira/calculadora-taxa.html
https://www.youtube.com/watch?v=JOqK2EGdxbQ

'''

def rate_daily_to_monthly(rate: float) -> float:
    return ( 1 + rate ) ** 30 - 1


def rate_monthly_to_daily(rate: float) -> float:
    return ( 1 + rate ) ** ( 1 / 30 ) - 1
    

def rate_monthly_to_annual(rate: float) -> float:
    return ( 1 + rate ) ** 12 - 1


def rate_annual_to_monthly(rate: float) -> float:
    return ( 1 + rate ) ** ( 1 / 12 ) - 1


def rate_annual_to_daily(rate: float) -> float:
    return ( 1 + rate ) ** ( 1 / 360 ) - 1


def rate_daily_to_annual(rate: float) -> float:
    return ( 1 + rate ) ^ 360 - 1 


def stock_return_rate(current, previous):
    return current / previous - 1


def stock_adjusted_return_rate(current, previous, factor, dividend_yeld, tax=None):
    tax = tax if tax < 1 else 2
    dividend_yeld = (dividend_yeld * (1 - tax))
    return (current * factor) / (previous - dividend_yeld) - 1