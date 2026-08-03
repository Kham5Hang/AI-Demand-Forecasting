def recommend_production(forecast_qty, safety_stock=0.10):

    recommended = forecast_qty * (1 + safety_stock)

    return round(recommended)
