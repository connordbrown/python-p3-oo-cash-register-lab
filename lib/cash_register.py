#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prev_transaction = 0

  def add_item(self, item, price, quantity=1):
    self.items.extend([item] * quantity)
    self.total += (price * quantity)
    self.prev_transaction = price * quantity
  
  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total -= (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.prev_transaction