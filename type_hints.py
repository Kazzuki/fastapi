from typing import List, Dict

price: int = 100
tax: float = 1.1

def calc_price_include_tax(price: int, tax: float) -> int:
    return int(price*tax)

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, str] = {'username' : 'kauzki'}


if __name__ == '__main__':
    print(f'{calc_price_include_tax(price=price, tax=tax)}円')
