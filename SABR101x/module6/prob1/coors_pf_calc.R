# Calculate Park factor in coors field

# select coors_park_factors.csv
rox <- read.csv(file.choose())

park <- subset(rox, home == "COL")
away <- subset(rox, visitor == "COL")

park_ratio <- sum(park$home_hr + park$visitor_hr) / sum(park$home_ab + park$visitor_ab)
away_ratio <- sum(away$home_hr + away$visitor_hr) / sum(away$home_ab + away$visitor_ab)

coors_hr_pf <- 100 * park_ratio / away_ratio
