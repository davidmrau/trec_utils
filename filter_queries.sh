# clean FILE_A form webpages, remove alphanumeric, remove trailing and leading whitespaces, remove empty lines
# remove queries that overlap with FILE_B
# usage:
# bash filter_queries.sh FILE_A FILE_B


grep -v -e  .*http.* -e  .*www\\..* -e .*\\.com.* -e .*\\.net.* -e .*\\.org.* -e .*\\.edu.*  $1  | sed 's/[^a-zA-Z0-9 ]//g' | awk '{$1=$1};1' | awk 'NF' > tmp.txt
awk 'NR==FNR{a[$0];next} !($0 in a)' $2 tmp.txt | sort | uniq  > ${1}_filtered
rm tmp.txt
