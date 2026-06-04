def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda a: a['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda a: f"* {a} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    total: int = sum(m['power'] for m in mages)
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(total / len(mages), 2)
    }


if __name__ == "__main__":

    artifacts = [
        {'name': 'Light Prism', 'power': 93, 'type': 'accessory'},
        {'name': 'Storm Crown', 'power': 97, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 61, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 76, 'type': 'armor'}
        ]
    mages = [
        {'name': 'Kai', 'power': 52, 'element': 'water'},
        {'name': 'Ember', 'power': 100, 'element': 'light'},
        {'name': 'Sage', 'power': 93, 'element': 'lightning'},
        {'name': 'Alex', 'power': 80, 'element': 'lightning'},
        {'name': 'Jordan', 'power': 54, 'element': 'water'}
        ]
    spells = ['tsunami', 'heal', 'lightning', 'tornado']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes "
        f"before {second['name']} ({second['power']} power)"
        )
    print()

    print("Testing power filter...")
    min_power = 80
    filtered = power_filter(mages, min_power)
    print(f"Mages with power >={min_power}: {[m['name'] for m in filtered]}")
    print()

    print("Testing spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))
    print()

    print("Testing mage stats...")
    print(f"{mage_stats(mages)}")
    print()
