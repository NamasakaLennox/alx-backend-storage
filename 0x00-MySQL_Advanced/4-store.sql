-- creates a new trigger
-- decreases  the quantity of an item after adding new order
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quatity - NEW.number WHERE name = NEW.item_name;
