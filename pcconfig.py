import pynecone as pc

class GithubwebscraperConfig(pc.Config):
    pass

config = GithubwebscraperConfig(
    app_name="github_webscraper",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)