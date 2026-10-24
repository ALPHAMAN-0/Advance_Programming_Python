resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def show_resource(resource):
    if resource[3] < 0:
        print(f"ID: {resource[0]}, Name: {resource[1]}, Category: {resource[2]}, Quantity: Invalid ({resource[3]})")
    else:
        print(f"ID: {resource[0]}, Name: {resource[1]}, Category: {resource[2]}, Quantity: {resource[3]}")


def display_resources(resources):
    if len(resources) == 0:
        print("No resources found")
        return
    for resource in resources:
        show_resource(resource)


def search_by_category(resources, category):
    found = False
    for resource in resources:
        if resource[2].lower() == category.lower():
            show_resource(resource)
            found = True
    if not found:
        print("No resources found in category:", category)


def find_unavailable(resources):
    unavailable = []
    for resource in resources:
        if resource[3] == 0:
            unavailable.append(resource)
    return unavailable


def find_by_id(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            return resource
    return None


print("All resources:")
display_resources(resources)

print("\nResources in Electronics category:")
search_by_category(resources, "Electronics")

print("\nUnavailable resources:")
display_resources(find_unavailable(resources))

print("\nTest 1: Unknown resource ID 999")
resource = find_by_id(resources, 999)
if resource is None:
    print("Resource with ID 999 not found")
else:
    show_resource(resource)

print("\nTest 2: Negative quantity")
display_resources([[106, "Speaker", "Audio", -4]])

print("\nTest 3: Resource with zero units")
display_resources(find_unavailable([[107, "Printer", "Electronics", 0]]))

print("\nTest 4: Empty resource list")
display_resources([])
