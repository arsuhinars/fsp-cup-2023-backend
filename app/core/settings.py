from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        secrets_dir="/run/secrets",
        extra="allow",
        from_attributes=True,
    )

    db_url: str


settings = AppSettings(_env_file="dev.env")
