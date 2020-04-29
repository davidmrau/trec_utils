# writes all ids of queries with < 10 hits to filename_ids_less_than_10
# usage:
# bash less_than_10_hits.sh filename

awk '{print $1}' $1 | uniq -c | awk '$1 < 10' | awk '{print $2}' > ${1}_ids_less_than_10
