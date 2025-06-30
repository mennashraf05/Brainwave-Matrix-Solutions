# src/features.py

import tldextract


def get_url_features(url: str) -> dict:
    """
    Return a dictionary of numerical features for the given URL:
      - url_length: length of the URL
      - num_dots: number of dots in the URL
      - num_hyphens: number of hyphens in the URL
      - has_at: presence of '@' symbol
      - num_digits: count of digits in the URL
      - subdomain_count: number of subdomains
      - suspicious_tld: indicator for suspicious top-level domains
      - domain_age_days: set to 0 (WHOIS disabled)
    """
    feats = {}
    # 1. URL length
    feats['url_length']     = len(url)
    # 2. Count dots and hyphens
    feats['num_dots']       = url.count('.')
    feats['num_hyphens']    = url.count('-')
    # 3. Presence of '@'
    feats['has_at']         = int('@' in url)
    # 4. Count of digits
    feats['num_digits']     = sum(c.isdigit() for c in url)

    # 5. Domain parsing
    parsed = tldextract.extract(url)
    feats['subdomain_count'] = len(parsed.subdomain.split('.')) if parsed.subdomain else 0

    # 6. Suspicious TLDs
    suspicious_tlds = {'.tk', '.ga', '.cf', '.ml', '.gq'}
    feats['suspicious_tld'] = int('.' + parsed.suffix in suspicious_tlds)

    # 7. Domain age disabled
    feats['domain_age_days'] = 0

    return feats
