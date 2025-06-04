from dataclasses import dataclass
from functools import total_ordering

@dataclass(frozen=True)
class Stock:
    ticker: str
    price: float
    dividend: float = 0
    dividend_frequency: int = 4

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency

@dataclass
@total_ordering
class Position:
    stock: Stock
    shares: int

    def __eq__(self, other):
        return self.stock.price * self.shares == other.stock.price * other.shares
    
    def __gt__(self, other):
        return self.stock.price * self.shares > other.stock.price * other.shares

@dataclass
class Portfolio:
    holdings: list[Position]

    @property
    def value(self):
        return sum([pos.shares * pos.stock.price for pos in self.holdings])
        
    @property
    def portfolio_yield(self):
        return sum([pos.stock.annual_dividend * pos.shares for pos in self.holdings]) / self.value


MSFT = Stock(ticker="MSFT", price=360, dividend=0.62, dividend_frequency=4)
LMT = Stock("LMT", 360, 2.8, 4)
GOOGL = Stock("GOOGL", 2200, 0, 0)
print(LMT)
print(LMT.annual_dividend)
print(GOOGL.annual_dividend)

p1 = Position(MSFT, 100)
p2 = Position(LMT, 100)
p3 = Position(GOOGL, 10)
print(p2)
print(p1)
print(p1 == p2)
print(p1 <= p3)
portfolio = Portfolio(holdings=[p1, p2, p3])
print(portfolio.portfolio_yield)
print(f"{portfolio.portfolio_yield:.2%}")
print(portfolio.value)