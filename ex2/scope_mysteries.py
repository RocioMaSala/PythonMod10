
from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def incrementation() -> int:
        nonlocal count
        count += 1
        return count
    return incrementation


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(add: int) -> int:
        nonlocal power
        power += add
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulated = spell_accumulator(50)
    print(f"Base 50, add 20: {accumulated(20)}")
    print(f"Base 50, add 30: {accumulated(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
