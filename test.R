getwd()

library(ggplot2)
library(dplyr)
library(tidyr)

# Dataset

input_df = "an/example/dataset" # insert dataset to test
# Here
input_df = "matching_introns.csv"

df = read.csv(input_df, header = T, sep = "\t")

head(df)