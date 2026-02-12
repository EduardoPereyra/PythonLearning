def add_person_directory():
    directory: dict[str, dict[str, int | str]] = {}
    def add_person(name: str, age: int, city: str) -> dict[str, dict[str, int | str]]:
        directory[name] = {"age": age, "city": city} 
        return directory
    return add_person

save = add_person_directory()
directory = save("Alice", 30, "New York")
directory = save("Bob", 25, "Los Angeles")
print(directory) # Output: {'Alice': {'age': 30, 'city': 'New York'}}