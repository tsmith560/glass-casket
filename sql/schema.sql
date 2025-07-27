-- Table: model_versions
CREATE TABLE IF NOT EXISTS model_versions (
    id SERIAL PRIMARY KEY,
    version_name TEXT NOT NULL UNIQUE,
    notes TEXT,
    date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: predictions
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    input_text TEXT NOT NULL,
    output_text TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    model_version TEXT REFERENCES model_versions(version_name),
    confidence_score FLOAT,
    metadata JSONB
);
