assert snakemake.input.get("sort", "missing") == "missing"

with open(snakemake.output[0], "w") as out:
    print(1, 2, 3, file=out)
