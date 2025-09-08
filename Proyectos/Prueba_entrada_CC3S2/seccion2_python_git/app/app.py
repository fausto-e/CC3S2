import sys

# Fix innecesario en forma de commentario

def summarize(nums):
    if not isinstance(nums, list):
        raise ValueError("nums debe ser una list.")
    if not nums:
        return {"count": 0, "sum": 0, "avg": None}
    for n in nums:
        if not isinstance(n, (int, float)):
            raise ValueError("Los numeros deben ser números.")
    total = sum(nums)
    count = len(nums)
    avg = total / count if count else None
    return {"count": count, "sum": total, "avg": avg}

def parse_input(arg):
    try:
        return [float(x) for x in arg.split(",") if x.strip()]
    except ValueError:
        raise ValueError("Todo el argumento deben ser números separados por comas.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 app.py \"1,2,3\"")
        sys.exit(1)
    try:
        nums = parse_input(sys.argv[1])
        result = summarize(nums)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)