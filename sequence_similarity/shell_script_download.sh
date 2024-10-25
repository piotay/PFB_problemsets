#/bin/bash

listvar = "ss_rand5-200_v_qfo_BL50.txt ss_rand5-200_v_qfo_BP62.txt ss_rand5-200_v_qfo_VT10.txt ss_rand5-200_v_qfo_VT160.txt ss_rand5-200_v_qfo_VT20.txt ss_rand5-200_v_qfo_VT40.txt ss_rand5-200_v_qfo_VT80.txt ss_rand5-800_v_qfo_BL50.txt ss_rand5-800_v_qfo_BP62.txt ss_rand5-800_v_qfo_VT10.txt ss_rand5-800_v_qfo_VT160.txt ss_rand5-800_v_qfo_VT20.txt ss_rand5-800_v_qfo_VT40.txt ss_rand5-800_v_qfo_VT80.txt"

for i in listvar
do
curl -O "https://fasta.bioch.virginia.edu/mol_evol/data/"$i
done


