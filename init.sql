DO $$ BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_database WHERE datname = 'sprockets'
  ) THEN
    CREATE DATABASE sprockets;
  END IF;
END $$;

\c sprockets;