library(dplyr)

pd <- read.csv("drwhodata/all-scripts.csv")

count_1 <- pd %>% 
    filter(episodeid == "20-1")



print(count_1)