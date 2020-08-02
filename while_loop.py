STATE_TAX_RATE=0.035
FED_TAX_RATE=0.15

employee=input("Employee name:")
hours=float(input("Hours worked:"))
payRate=float(input("Pay rate:"))

wages=hours*payRate
stateTaxes=wages*STATE_TAX_RATE
fedTaxes=wages*FED_TAX_RATE
takeHome=wages-stateTaxes-fedTaxes

print("PAY REPORT")
print("Emplpyee:"+employee)
print("-----------------------------------")
print("Wages:",wages)
print("State Taxes:",stateTaxes)
print("Fed Taxes:",fedTaxes)
print("Pay:",takeHome)


