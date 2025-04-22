CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
RETURNS TABLE (user_id INT, name VARCHAR(255), surname VARCHAR(255), phone VARCHAR(255)) AS
$$ 
BEGIN
    RETURN QUERY
    SELECT p.user_id, p.name, p.surname, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || p_pattern || '%'
       OR p.surname ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE insert_or_update_user(_name TEXT, _surname TEXT, _phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = _name AND surname = _surname) THEN
        UPDATE phonebook SET phone = _phone WHERE name = _name AND surname = _surname;
    ELSE
        INSERT INTO phonebook (name, surname, phone) VALUES (_name, _surname, _phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_many_users(names text[], surnames text[], phones text[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        INSERT INTO phonebook (name, surname, phone)
        VALUES (names[i], surnames[i], phones[i]);
    END LOOP;
END;
$$;


CREATE OR REPLACE FUNCTION get_paginated_users(_limit integer, _offset integer)
RETURNS TABLE(user_id integer, name character varying, surname character varying, phone character varying) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.user_id, p.name, p.surname, p.phone
    FROM phonebook p
    ORDER BY p.user_id
    LIMIT _limit OFFSET _offset;
END;
$$;
