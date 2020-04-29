FOLDER=../results
../indexing/galago-3.10-bin/bin/galago threaded-batch-search --index=../collections/robust04_index/ ../collections/AOL_queries/AOL-queries-all_filtered.txt.json --scorer=bm25 > $RESULTS/robust04_AOL_top_1000.txt
../indexing/galago-3.10-bin/bin/galago batch-search --index=../collections/robust04_index/ ../collections/TREC_robust_test/04.testset_num_query_lower.json --scorer=bm25 --requested=2000 > $RESULTS/robust04_TREC_test_top_2000.txt
