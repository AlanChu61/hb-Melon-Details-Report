"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melon):
    """Print each melon with corresponding attribute information."""

    # print(f'{name}s {have_or_have_not} seeds and are ${price}')
    print(f"{melon['name']}")
    print(f"Price: {melon['price']}")
    print(f"Seedless: {melon['seedless']}")
    print(f"Flesh color: {melon['flesh_color']}")
    print(f"Rind color: {melon['rind_color']}")
    print(f"Average weight: {melon['average_weight']}")
    print("--------------------")


for i in range(len(melons)):
    print_melon(melons[i])
