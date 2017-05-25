Ensembl REST API
================

* [API documentation](http://rest.ensembl.org/)
* [Course web site](http://training.ensembl.org/events/2017/2017-05-25-API_Cam_May)
* [Presentation slides (pdf)](http://ftp.ebi.ac.uk/pub/databases/ensembl/training/2017/API_Cam_May/API_course_slide_deck.pdf)

Sections
--------

* [Core](basic_lookup)
    * Look up a gene symbol, get its FASTA sequence, get all transcripts,
    convert between GRCh38 and GRCh37
    ([gene_lookup.py](basic_lookup/gene_lookup.py))
    * Request a number of transcripts using a POST request
    ([seq_lookup_post.py](basic_lookup/seq_lookup_post.py))
    * Check HTML headers for rate limiting information
    ([rate_limit.py](basic_lookup/rate_limit.py))
* [Variation](variation)
    * Fetch variants in region, get its details, check overlap with transcripts
    ([variants.py](variation/variants.py))
    * Get variants associated with a trait and the frequencies in a population
    ([coffee.py](variation/coffee.py))
