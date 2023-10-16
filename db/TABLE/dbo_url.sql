DO $script$
BEGIN

CREATE TABLE IF NOT EXISTS dbo.url (
	url_id INT NOT NULL,
	url_name VARCHAR(150) NOT NULL,
)
WITH (oids = false);

-- Create primary key
IF NOT EXISTS (
	SELECT 1
	FROM information_schema.table_constraints
	WHERE table_schema = 'dbo'
	AND table_name = 'url'
	AND constraint_type = 'PRIMARY KEY'
	LIMIT 1
)
THEN
	ALTER TABLE IF EXISTS dbo.url
		ADD CONSTRAINT pk_url_id
		PRIMARY KEY (url_id);
END IF;

COMMENT ON TABLE dbo.url IS 'URL - сайта для парсинга';

COMMENT ON COLUMN dbo.url_id IS 'Идентификатор сайта';
COMMENT ON COLUMN dbo.url_name IS 'URL-сайта';

END;
$script$;