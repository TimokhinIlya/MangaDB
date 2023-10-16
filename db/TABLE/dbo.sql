DO $script$ 

BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM information_schema.schemata 
        WHERE schema_name = 'dbo'
    ) THEN
        CREATE SCHEMA dbo;
    END IF;

END 
$script$;