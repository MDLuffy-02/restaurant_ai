def customer_summary(df):
    return df.groupby("user_id").agg(
        order_count=("order_id", "count"),
        total_spend=("total_amount", "sum")
    ).reset_index()
