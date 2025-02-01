inventory = {"apple":10,"banana":5,"orange":8}
check_item = "apple"
if check_item in inventory:
    print(f"checking stock for {check_item},,,")
else:
    print("not in inventory")
if check_item in inventory:    
    for _ in range(inventory[check_item]):
        print(f"one {check_item} sold.")