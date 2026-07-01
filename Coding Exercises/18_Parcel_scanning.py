# Parcel Scanning System

def scan_parcels(parcel_code):
    messages = []

    for barcode in parcel_code:
        if barcode == "DAMAGED":
            messages.append("Skipped damaged parcel")
            continue

        if barcode == "STOP":
            messages.append("Critical error: Stopping scan")
            break

        messages.append(f"Scanned parcel: {barcode}")

    else:
        messages.append("All parcels scanned successfully")

    return messages

# Example
parcel_code = ["A101", "B202", "DAMAGED", "C303", "STOP", "D404"]

result = scan_parcels(parcel_code)

for message in result:
    print(message)