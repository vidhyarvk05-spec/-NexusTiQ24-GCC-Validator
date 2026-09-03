# NexusTiQ24 - GCC Banking Document Validator
# Track: GCC + Banking - Reasoning Based Validation

def validate_document(invoice_amount, po_amount, vendor):
    print("\n--- GCC Validator Reasoning Engine ---")
    print(f"Step 1: Extracted Invoice = {invoice_amount} from {vendor}")
    print(f"Step 2: Retrieved PO Amount = {po_amount}")
    print(f"Step 3: Comparing amounts...")
    
    diff = abs(invoice_amount - po_amount)
    
    if diff == 0:
        reasoning = f"Reasoning: PERFECT MATCH. Invoice {invoice_amount} == PO {po_amount}. No fraud risk."
        status = "APPROVED"
    elif diff < 1000:
        reasoning = f"Reasoning: MINOR VARIANCE of {diff}. Within tolerance for GCC banking."
        status = "REVIEW"
    else:
        reasoning = f"Reasoning: MAJOR MISMATCH! Variance {diff}. Potential fraud."
        status = "REJECTED"
    
    print(f"Step 4: {reasoning}")
    print(f"Final Status: {status}")
    return status, reasoning

print("NexusTiQ24 Ready! GCC Doc Assistant Working")
amt = int(input("Enter invoice amount: "))
result, reason = validate_document(amt, 50000, "TATA Steel")
print(f"\nOutput: {result}")
