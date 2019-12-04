# analysis of vocabulary Growth Curves after Baayen 2008
setwd("~/supertags/subword-nmt")

europarl  <- scan(file.choose(), what=character()) # select with the mouse your file 
length(europarl)
system.time(europarl.growth <- growth.fnc(text = europarl[1:1000000], size = 1000, nchunks = 1000)) 

plot(europarl.growth@data$data$HapaxLegomena, col = "red")

plot(Brown.growth@data$data$HapaxLegomena, col = "red")

system.time(europarl.BPE.growth <- growth.fnc(text = europarl.BPE[1:1000000], size = 1000, nchunks = 1000)) 
europarl.BPE2  <- scan(file.choose(), what=character()) # select with the mouse your file  = with no interruption
system.time(europarl.BPE2.growth <- growth.fnc(text = europarl.BPE2[1:1000000], size = 1000, nchunks = 1000)) 
plot(europarl.growth@data$data$TypeTokenRatio)
plot(europarl.growth@data$data$Types)
plot(europarl.growth@data$data$TypeTokenRatio)

head(europarl,10)

# comparisson with Brown empirical curves------
install.packages("zipfR")
library(zipfR)
##  plot the two CURVES
europarl.vgc <- growth2vgc.fnc(europarl.growth)
europarl.PBE2.vgc <- growth2vgc.fnc(europarl.BPE2.growth)
plot(europarl.vgc,europarl.PBE2.vgc,add.m=1,legend=c("Europarl","BPE-ed Europarl"), main="vocabulary growth curves")
plot(europarl.vgc,europarl.PBE2.vgc,add.m=1, main="vocabulary growth curves")

# TODO BPE for DE, BPR FR and GB trained trained together 
europarl.BPE2.lower <- tolower(europarl.BPE2)
europarl.lower <-tolower(europarl)
library(zipfR)
library(languageR)

compare.richness.fnc(europarl.lower[1:1000000],europarl.BPE2.lower[1:1000000]) # 




