"""
supplier-lead-time-predictor-skill: Client SDK
Calculates historical supply latency parameters to update reorder safety buffer margins.
"""
from __future__ import annotations
from typing import Optional


class SupplierLeadTimePredictorClient:
    """
    SDK for procurement risk mapping.
    """

    def predict_delay(self, historical_delays_days: list[int]) -> dict:
        if not historical_delays_days:
            return {"predicted_delay_days": 0.0, "reliability_status": "reliable"}

        mean = sum(historical_delays_days) / len(historical_delays_days)
        
        if mean > 5.0:
            status = "high-delay"
        elif mean > 2.0:
            status = "variable"
        else:
            status = "reliable"

        return {
            "predicted_delay_days": round(mean, 1),
            "reliability_status": status
        }
