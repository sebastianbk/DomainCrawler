DomainCrawler: Expired .dk domains
==================================

This small Python script scrapes crawlr.dk to check for expired .dk domains.

The website crawlr.dk continuously checks with DK Hostmaster to see if any of the domains in its database have expired during the past 365 days. The domains will thereby be available for re-registration.

This script will go through the index of domains and find all domains of 3 characters or less (excluding the domain ending). These domains will be saved to a collection on a local Mongo database that must be running on the default port (27017).
