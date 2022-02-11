from faker.providers import DynamicProvider

category_provider = DynamicProvider(
    provider_name="category",
    elements=[
        "Books, Magazines, Comics",
        "Films & Videos",
        "Games, Toys, Figurines",
        "Music",
    ],
)
