# worked with retrosheet_sandbox.csv

# Fenway Park HR factor past five years
soxHR <- read.csv(file.choose())
view(soxHR)

# a way to do a COUNTIF, first get TRUE FALSE matrix, sum TRUEs
sum(soxHR$home == "BOS")

# Split Home (fenway) games vs. Away
park <- subset(soxHR, home == "BOS")
away <- subset(soxHR, visitor == "BOS")

# another COUNTIF after making a subset of data frame
nrow(park)

# calculate ratios of Total HR / Total AB
# Sum of Home and Visitor stats are used to avoid bias from park home team
park_ratio <- sum(park$home_hr + park$visitor_hr) / sum(soxHR$home == "BOS")
away_ratio <- sum(away$home_hr + away$visitor_hr) / sum(soxHR$visitor == "BOS")

sox_hr_pf <- 100 * park_ratio / away_ratio
sox_hr_pf

# define function

# One stat for one team function
pf_stat <- function(team, stat, data){
  park <- subset(data, home == team)
  away <- subset(data, visitor == team)
  
  # build strings for accessing proper PF stat
  home_stat = paste("home", stat, sep="_")
  visitor_stat = paste("visitor", stat, sep="_")
  
  # calculate ratios of Total stat / Total AB
  # Sum of Home and Visitor stats are used to avoid bias from park home team
  park_ratio <- sum(park[[home_stat]] + park[[visitor_stat]]) / sum(data$home == team)
  away_ratio <- sum(away[[home_stat]] + away[[visitor_stat]]) / sum(data$visitor == team)
  
  return (100 * (park_ratio / away_ratio))  
}

sox_hr_pf_2 <- pf_stat("BOS", "hr", soxHR)

# test that we get the same HR PF for the 2013 redsox as calculated before
stopifnot(sox_hr_pf == sox_hr_pf_2)

# run CLE HR PF with the function
cle_hr_pf <- pf_stat("CLE", "hr", soxHR)
