import os
from dataclasses import dataclass, field


@dataclass
class DatabaseConfig:
    host: str = field(default_factory=lambda: os.getenv("DB_HOST", "localhost"))
    port: int = field(default_factory=lambda: int(os.getenv("DB_PORT", "5432")))
    database: str = field(default_factory=lambda: os.getenv("DB_NAME", "postgres"))
    schema: str = field(default_factory=lambda: os.getenv("DB_SCHEMA", "asu_inventory"))
    username: str = field(default_factory=lambda: os.getenv("DB_USERNAME", "postgres"))
    password: str = field(default_factory=lambda: os.getenv("DB_PASSWORD", "CKu9LmMo"))

    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class AppConfig:
    db: DatabaseConfig = field(default_factory=DatabaseConfig)


config = AppConfig()