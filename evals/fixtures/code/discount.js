export function discountedTotal(prices, discount = 0) {
  if (discount < 0 || discount > 1) throw new RangeError('discount');
  return prices.reduce((sum, price) => sum + price, 0) * (1 - discount);
}
