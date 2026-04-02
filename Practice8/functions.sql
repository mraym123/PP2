-- 1. Function to return matching records (Pattern matching)
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM contacts c
    WHERE c.name ILIKE '%' || pattern || '%' 
       OR c.phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Function for pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;