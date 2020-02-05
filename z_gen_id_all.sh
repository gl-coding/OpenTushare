cat data/* | awk -F "\t" '{print $1"\t"$2}' | sort | uniq > id.all
