def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)]  # Generate lowercase alphabet
    pattern = []

    # Create the top half of the pattern
    for i in range(size):
        # Build the row with letters and dashes
        left_part = alphabet[size - 1:size - i - 1:-1]  # Descending part
        right_part = alphabet[size - i - 1:size]        # Ascending part
        row = "-".join(left_part + right_part[1:])      # Combine both parts
        pattern.append(row.center(4 * size - 3, "-"))   # Center the row

    # Combine top and bottom parts of the rangoli
    full_pattern = pattern + pattern[-2::-1]  # Add the mirrored bottom part

    # Print the pattern
    print("\n".join(full_pattern))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
