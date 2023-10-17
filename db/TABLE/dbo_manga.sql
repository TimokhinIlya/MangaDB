DO $script$
BEGIN

CREATE TABLE IF NOT EXISTS dbo.manga (
	manga_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
	manga_url VARCHAR(200),
	manga_name VARCHAR(150) NOT NULL UNIQUE,
	manga_desc VARCHAR,
	current_chapter INT,
	last_chapter INT,
	last_chapter_date TIMESTAMP WITHOUT TIME ZONE
)
WITH (oids = false);

-- Create primary key
IF NOT EXISTS (
	SELECT 1
	FROM information_schema.table_constraints
	WHERE table_schema = 'dbo'
	AND table_name = 'manga'
	AND constraint_type = 'PRIMARY KEY'
	LIMIT 1
)
THEN
	ALTER TABLE IF EXISTS dbo.manga
		ADD CONSTRAINT pk_manga_id
		PRIMARY KEY (manga_id); 
END IF;

COMMENT ON TABLE dbo.manga IS 'Манга';

COMMENT ON COLUMN dbo.manga.manga_id IS 'Идентификатор манги';
COMMENT ON COLUMN dbo.manga.manga_url IS 'Адрес манги (последняя вышедшая глава)';
COMMENT ON COLUMN dbo.manga.manga_name IS 'Название манги';
COMMENT ON COLUMN dbo.manga.manga_desc IS 'Описание состояния';
COMMENT ON COLUMN dbo.manga.current_chapter IS 'Последняя прочитанная глава';
COMMENT ON COLUMN dbo.manga.last_chapter IS 'Последняя вышедшая глава';
COMMENT ON COLUMN dbo.manga.last_chapter_date IS 'Дата выхода главы';

END;
$script$;
