def calculate_reorder_point(average_daily_demand, lead_time_days, safety_stock=0):
    return (average_daily_demand * lead_time_days) + safety_stock
