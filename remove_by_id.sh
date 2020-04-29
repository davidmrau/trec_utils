# removes lines from FILE_A that exactly match lines in FILE_B
# bash remove_by_id.sh FILE_A FILE_B

#!/bin/sh
#SBATCH --job-name=pre_processing
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --time=00:30:00

# removes lines from FILE_A that exactly match lines in FILE_B
# bash remove_by_id.sh FILE_A FILE_B




#cp ${1} $OUTFILE

C_FILE=${2}_or_command
TMP=sed_command_tmp
echo -n "print unless m/\b" > $TMP
cat $2 | tr "\n" "|" | sed "s/|/\\\b|\\\b/g" | rev | cut -c 2- | rev >> $TMP
echo -n "\b/" >> $TMP

tr -d '\n' <  $TMP > $C_FILE
rm $TMP

#sed -E -i.bak -f $C_FILE $1
perl -n -i.bak -f $C_FILE $1

mv $1 ${1}.filtered
mv ${1}.bak $1
#rm $C_FILE

#IDS=`cat ${2}`


#for ID in $IDS;do
#	echo $ID
#	sed -i.bak -e '/\b${ID}\b/d' $1
#done

