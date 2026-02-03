import json

input_file = 'backend/clean_services.json'
output_file = 'backend/clean_services.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total records before: {len(data)}")

seen_images = set()
cleaned_data = []
duplicates_count = 0

for item in data:
    if item['model'] == 'services.serviceitemimage':
        service_id = item['fields']['service_item']
        image_url = item['fields']['image_url']
        
        # Create a unique key for this combination
        key = (service_id, image_url)
        
        if key in seen_images:
            duplicates_count += 1
            # Skip adding this item to cleaned_data
            continue
        else:
            seen_images.add(key)
            cleaned_data.append(item)
    else:
        # Keep non-image items as is
        cleaned_data.append(item)

print(f"Removed {duplicates_count} duplicate images.")
print(f"Total records after: {len(cleaned_data)}")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=4)

print("File updated successfully.")
