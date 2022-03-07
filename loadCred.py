from searchtweets import ResultStream, gen_rule_payload, load_credentials

search_args = load_credentials(filename="secret.yaml",
yaml_key="search_tweets_api",
env_overwrite=False)