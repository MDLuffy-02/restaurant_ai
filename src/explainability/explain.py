def explain_prediction(model, features):
    # Integrate SHAP/LIME here when the final model is selected.
    return {"model": type(model).__name__, "features": list(features.columns)}
