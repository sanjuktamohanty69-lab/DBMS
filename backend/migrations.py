# Migration Script to add MySQL triggers for automatic stock decrement and stock validation

def create_triggers(connection):
    cursor = connection.cursor()

    # Trigger for automatic stock decrement when a sale is made
    cursor.execute("""
    CREATE TRIGGER stock_decrement
    AFTER INSERT ON sales
    FOR EACH ROW
    BEGIN
        UPDATE products SET stock = stock - NEW.quantity
        WHERE id = NEW.product_id;
    END;
    """)

    # Trigger for stock validation
    cursor.execute("""
    CREATE TRIGGER stock_validation
    BEFORE INSERT ON sales
    FOR EACH ROW
    BEGIN
        DECLARE msg VARCHAR(255);
        IF NEW.quantity > (SELECT stock FROM products WHERE id = NEW.product_id) THEN
            SET msg = CONCAT('Not enough stock for product ID: ', NEW.product_id);
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
    END;
    """)

    connection.commit()
    cursor.close()