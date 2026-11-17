package main

import (
	"errors"
	"fmt"
)

type Item struct {
	ID       int
	Name     string
	Quantity int
	Price    float64
}

type Inventory struct {
	items []Item
}

type Summary struct {
	ItemCount  int
	TotalUnits int
	TotalValue float64
}

func NewInventory() *Inventory {
	return &Inventory{items: []Item{}}
}

func (inv *Inventory) AddItem(item Item) error {
	if item.ID <= 0 {
		return errors.New("item ID must be positive")
	}
	if item.Name == "" {
		return errors.New("item name cannot be empty")
	}
	if item.Quantity < 0 {
		return errors.New("quantity cannot be negative")
	}
	if item.Price < 0 {
		return errors.New("price cannot be negative")
	}
	for _, existing := range inv.items {
		if existing.ID == item.ID {
			return fmt.Errorf("item with ID %d already exists", item.ID)
		}
	}
	inv.items = append(inv.items, item)
	return nil
}

func (inv *Inventory) UpdateItem(id int, name string, quantity int, price float64) error {
	if id <= 0 {
		return errors.New("item ID must be positive")
	}
	if name == "" {
		return errors.New("item name cannot be empty")
	}
	if quantity < 0 {
		return errors.New("quantity cannot be negative")
	}
	if price < 0 {
		return errors.New("price cannot be negative")
	}
	for i := range inv.items {
		if inv.items[i].ID == id {
			inv.items[i].Name = name
			inv.items[i].Quantity = quantity
			inv.items[i].Price = price
			return nil
		}
	}
	return fmt.Errorf("item with ID %d not found", id)
}

func (inv *Inventory) RemoveItem(id int) error {
	if id <= 0 {
		return errors.New("item ID must be positive")
	}
	for i := range inv.items {
		if inv.items[i].ID == id {
			inv.items = append(inv.items[:i], inv.items[i+1:]...)
			return nil
		}
	}
	return fmt.Errorf("item with ID %d not found", id)
}

func (inv *Inventory) Items() []Item {
	return inv.items
}

func (inv *Inventory) SummaryAsync() <-chan Summary {
	ch := make(chan Summary, 1)
	go func() {
		var summary Summary
		for _, item := range inv.items {
			summary.ItemCount++
			summary.TotalUnits += item.Quantity
			summary.TotalValue += float64(item.Quantity) * item.Price
		}
		ch <- summary
		close(ch)
	}()
	return ch
}

func main() {
	inv := NewInventory()

	_ = inv.AddItem(Item{ID: 1, Name: "Keyboard", Quantity: 10, Price: 1500.50})
	_ = inv.AddItem(Item{ID: 2, Name: "Mouse", Quantity: 25, Price: 750.25})
	_ = inv.AddItem(Item{ID: 3, Name: "Monitor", Quantity: 5, Price: 12000})

	_ = inv.UpdateItem(2, "Wireless Mouse", 30, 899.99)
	_ = inv.RemoveItem(3)

	fmt.Println("Inventory items:")
	for _, item := range inv.Items() {
		fmt.Printf("ID: %d | Name: %s | Qty: %d | Price: %.2f\n", item.ID, item.Name, item.Quantity, item.Price)
	}

	summary := <-inv.SummaryAsync()
	fmt.Printf("Summary -> Item Count: %d | Total Units: %d | Total Value: %.2f\n",
		summary.ItemCount, summary.TotalUnits, summary.TotalValue)
}
