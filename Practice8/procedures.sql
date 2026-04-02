-- 2. Procedure to insert or update (Upsert)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- 3. Procedure to insert many with validation (returns invalid data via RAISE NOTICE or a temp table)
-- For simplicity in a procedure, we use a basic regex for phone validation (e.g., only digits)
CREATE OR REPLACE PROCEDURE insert_many_contacts(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(names, 1) LOOP
        -- Simple validation: phone must be digits and length > 5
        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) > 5 THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid data skipped: % - %', names[i], phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 5. Procedure to delete by username or phone
CREATE OR REPLACE PROCEDURE delete_contact_by_val(p_val VARCHAR)
AS $$
BEGIN
    DELETE FROM contacts 
    WHERE name = p_val OR phone = p_val;
END;
$$ LANGUAGE plpgsql;