

rule dataframe:
    input: "matching_introns.csv"
    shell:
        "python test.py -i {input}"