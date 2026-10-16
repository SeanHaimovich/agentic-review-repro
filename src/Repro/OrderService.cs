using System;
using System.Collections.Generic;
using System.Linq;

namespace Repro.Orders
{
    public class OrderLine
    {
        public string Sku { get; set; }
        public int Quantity { get; set; }
        public decimal UnitPrice { get; set; }
    }

    public class OrderService
    {
        private readonly List<OrderLine> _lines = new List<OrderLine>();
        private decimal _discountRate = 0;

        public void AddLine(string sku, int quantity, decimal unitPrice)
        {
            var line = new OrderLine { Sku = sku, Quantity = quantity, UnitPrice = unitPrice };
            _lines.Add(line);
        }

        public void ApplyDiscount(decimal rate)
        {
            _discountRate = rate;
        }

        public decimal Total()
        {
            decimal total = 0;
            foreach (var line in _lines)
            {
                total += line.Quantity * line.UnitPrice;
            }
            return total - total * _discountRate;
        }

        public OrderLine FindBySku(string sku)
        {
            return _lines.Where(l => l.Sku == sku).First();
        }

        public string Summary()
        {
            return String.Format("{0} lines, total {1}", _lines.Count, Total());
        }
    }
}
