from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fire hits to {target} for {power} damage"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell Fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":

    # Higher Realm Test Data
    # Use these in your test functions:
    test_values = [12, 22, 10]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(heal, 3)
    result = amplified("Goblin", 4)
    print(f"Amplified power: {result}")

    print("\nTesting conditional caster...")
    high_power = conditional_caster(
        lambda target, power: power >= 50, fireball
        )
    print(high_power("Dragon", 12))
    print(high_power("Dragon", 55))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Dragon", 20)
    for r in results:
        print(r)
