# extract nums and queries from trectext
# usage:
# bash extract_query_trectext.sh filename 


# extract all titles, remove title tag, remove empty lines, to lower, remove non-alphanumeric, remove leading and trailing whitespaces
grep -A 1 '<title>' $1 --no-group-separator | sed 's/<title>//g' | awk 'NF' | sed 's/\([A-Z]\)/\L\1/g' | sed 's/[^a-zA-Z0-9 ]/ /g' | awk '{$1=$1};1'  > ${1}_titles_lower
# extract titles, remove title, top, Number: tags, remove empty lines, remove leading and trailing whitespaces, remove non-alphanumeric, merge num and query in one line
grep -B 2 -A 1 '<title>' $1 --no-group-separator | sed -e 's/<title>//g' -e 's/<num> Number: //g' -e 's/<top>//g'| awk 'NF' | awk '{$1=$1};1'| sed 's/[^a-zA-Z0-9 ]/ /g' | sed 'N;s/\n/\t/' | sed -e 's/\([A-Z]\)/\L\1/g' > ${1}_num_query_lower
# create json for galago
python3 line2json.py ${1}_num_query_lower 
