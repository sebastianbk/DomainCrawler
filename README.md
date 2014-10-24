DomainCrawler: Expired .dk domains
==================================

This small Python script scrape crawlr.dk to check for expired .dk domains.

The website crawlr.dk continuously checks with DK Hostmaster to see if any of the domains in its database have expired and thereby available for re-registration.

This script will go through the index of domains and return all domains of 2 characters or less (excluding the domain ending).
