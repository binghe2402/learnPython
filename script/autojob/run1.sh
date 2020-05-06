for confid in $(seq -f "%04g" 520 10 550)
do
    yhbatch -n 512 -x cn385,cn456,cn470 -p th_ft1 ./contraction$confid/run$confid.sh
    
done
