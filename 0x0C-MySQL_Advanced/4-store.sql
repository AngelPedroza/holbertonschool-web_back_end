-- Decrease the quantity of a item defined in the order
create trigger decrase_quant
after insert on orders
for each row update items
set quantity = quantity - NEW.number
where NEW.item_name = name;