--  resets the attribute valid_email only when the email has been changed
delimiter //
create trigger reset_valid
before update on users
for each row
BEGIN
    if NEW.email <> OLD.email
    then set NEW.valid_email = 0;
    end if;
END //
delimiter ;