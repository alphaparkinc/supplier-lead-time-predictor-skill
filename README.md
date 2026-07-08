# supplier-lead-time-predictor-skill

> **GenPark AI Agent Skill** -- Supplier delay predictor.

## Quick Start

```python
from client import SupplierLeadTimePredictorClient
client = SupplierLeadTimePredictorClient()
res = client.predict_delay([2, 2, 4])
print(res["reliability_status"])
```
