"""
example_usage.py -- Demonstrates SupplierLeadTimePredictorClient
"""
from client import SupplierLeadTimePredictorClient

def main():
    client = SupplierLeadTimePredictorClient()
    result = client.predict_delay([1, 3, 2, 6, 0])
    print("[Supplier Lead Time Analysis]")
    print(f"Mean Delay: {result['predicted_delay_days']} days")
    print(f"Supplier Rating: {result['reliability_status'].upper()}")

if __name__ == "__main__":
    main()
