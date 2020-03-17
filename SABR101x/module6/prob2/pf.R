# calculate highest/lowest pf in 2013

pf_all <- read.csv(file.choose())

# Florida Marlins change team`s name to Miami Marlins. So merge them
pf_all <- within(pf_all, levels(home)[levels(home) == "FLO"] <- "MIA")
pf_all <- within(pf_all, levels(visitor)[levels(visitor) == "FLO"] <- "MIA")

# create the function for calculate pf_stat_teams
pf_stat_teams <- function(stat, data, season_year){
  data <- subset(data, year == season_year)
  
  home_stat <- paste("home", stat, sep="_")
  visitor_stat <- paste("visitor", stat, sep="_")
  pf_stat <- paste("pf", stat, season_year, sep="_")
  cols = c(home_stat, visitor_stat, "home_ab", "visitor_ab")
  
  # must include "plyr" package
  park_sums <- ddply(data, .(home), colwise(sum, cols))
  away_sums <- ddply(data, .(visitor), colwise(sum, cols))
  
  park_sums$park_ratio <- (park_sums[[home_stat]] + park_sums[[visitor_stat]]) / 
                            (park_sums[["home_ab"]] + park_sums[["visitor_ab"]])
  away_sums$away_ratio <- (away_sums[[home_stat]] + away_sums[[visitor_stat]]) / 
    (away_sums[["home_ab"]] + away_sums[["visitor_ab"]])
  
  pf <- merge(park_sums, away_sums, by.x = "home", by.y="visitor")
  pf[[pf_stat]] <- with(pf, pf$park_ratio / pf$away_ratio)
  
  pf <- rename(pf, replace = c("home"="team"))
  pf <- subset(pf, select = c("team", pf_stat))
  
  return(pf)
}

hr_2013 <- pf_stat_teams("hr", pf_all, season_year = 2013)

# check lowest double factor in MLB
double_2010 <- pf_stat_teams("2b", pf_all, season_year = 2010)

# check highest BB factor in MLB
bb_2011 <- pf_stat_teams("bb", pf_all, season_year = 2011)
