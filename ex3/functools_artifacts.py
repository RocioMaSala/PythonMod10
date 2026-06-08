import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    result = functools.reduce(operations[operation], spells)
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': functools.partial(base_enchantment, 40, "Fire"),
        'ice': functools.partial(base_enchantment, 30, "Ice"),
        'lightning': functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantement(power: int, element: str, target: str) -> str:
        return f"{element} {target} (power: {power})"

    enchants = partial_enchanter(base_enchantement)
    print(enchants['fire']("Sword"))
    print(enchants['ice']("Shield"))
    print(enchants['fire']("Mario Bros"))

    print("\nTesting memoized fibonacci...")
    for n in [10]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"{memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "heal"]))
    print(dispatcher(2.5))


if __name__ == "__main__":
    main()
