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
    if previous is None:
        return None

    return current / previous - 1


def stock_adjusted_return_rate(current, previous, factor=None, dividend_yeld=None, tax=None):
    if previous is None:
        return None

    factor = factor or 1
    dividend_yeld = dividend_yeld or 0
    if tax is None or tax >= 0:
        tax = 2
    dividend_yeld = (dividend_yeld * abs(1 - tax))

    return (current * factor) / (previous - dividend_yeld) - 1


def stock_adjusted_price(adjusted, adjusted_return_rate):
    return adjusted / (1 + adjusted_return_rate)


def stock_adjusted_return_rate_check(current, previous_adjusted):
    return current / previous_adjusted - 1


def stock_event_factor(expression):
    if expression is None or len(expression) == 0:
        return None, 1

    as_float = lambda x: float(x.replace(',', '.')) if type(x) == str else float(x)
    event, factor = 'INPLIT', 0.00
    parts = expression.split(':')
    if len(parts) > 1:
        parts[0] = as_float(parts[0])
        parts[1] = as_float(parts[1])

        if parts[0] == 1.0:
            factor = parts[0] / parts[1]
        elif parts[1] == 1.0:
            event = 'SPLIT'
            factor = parts[0]

        return event, factor
    else:
        raise ValueError('Invalid expression {}'.format(expression))
