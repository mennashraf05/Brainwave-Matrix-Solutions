from src.features import get_url_features

test_urls = [
    "http://example.com",
    "https://secure-login.tk/login?user=abc",
    "http://sub.test-site.ga/path/page.html"
]

for url in test_urls:
    feats = get_url_features(url)
    print(url)
    for k, v in feats.items():
        print(f"  {k:16s}: {v}")
    print()
