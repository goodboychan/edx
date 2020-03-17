# Read in files of Retrosheet Gamelog data
attendance_data <- read.csv(file.choose())
summary(attendance_data)
attach(attendance_data)

# column we want to scatterplot matrix, making a smaller data frame
Game_logs = attendance_data[c("attendance","game_minutes", "outs")]
splom(Game_logs, xlab = "Retrosheet gameLogs Scatterplot Matrix")

plot(outs, game_minutes)
TOGvouts = lm(game_minutes~outs)
TOGvouts
abline(TOGvouts)

plot(attendance, game_minutes)
TOGvattend = lm(game_minutes~attendance)
TOGvattend
abline(TOGvattend)

attendance_data$weekend_game <- with(attendance_data, ifelse(day == 'Sat' | day == 'Sun',1,0))
weekend_attendance <- attendance_data[attendance_data$weekend_game == 1,]

summary(attendance)
summary(weekend_attendance$attendance)

attendance_data$VerlanderPitching <- with(attendance_data, ifelse(home_starting_pitcher_name == 'Justin Verlander', 1, 0))
Verlander_attendance <- attendance_data[attendance_data$VerlanderPitching == 1,]
summary(Verlander_attendance$attendance)

Tigers_attendance <- attendance_data[home == 'DET',]
Tigers_projected_attendance <- lm(Tigers_attendance$attendance~Tigers_attendance$weekend_game + Tigers_attendance$VerlanderPitching)
Tigers_projected_attendance

confint(Tigers_projected_attendance, level = 0.95)

game_statistics <- read.csv(file.choose())
attach(game_statistics)

#game_statistics$total_runs <- with(game_statistics, home_score+visitor_score)
total_runs <- with(game_statistics, home_score+visitor_score)
game_statistics["total_runs"] <- total_runs
total_time_data <- game_statistics[c('game_minutes', 'total_runs', 'outs')]
require('lattice')
splom(total_time_data)
cor(game_minutes,outs)
cor(game_minutes, total_runs)
cor(total_runs, outs)

projected_minutes <- lm(game_minutes ~ total_runs + outs)

game_statistics$RedSox_playing <- with(game_statistics, ifelse(home == 'BOS' | visitor == 'BOS', 1, 0))
RedSox_games <- game_statistics[game_statistics$RedSox_playing == 1, ]
summary(RedSox_games)
mean(RedSox_games$total_runs)
mean(game_statistics$total_runs)
hist(RedSox_games$total_runs, breaks = 40)

game_statistics$BrianGorman <- with(game_statistics, ifelse(hp_ump_name == 'Brian Gorman', 1, 0))
BrianGorman_games <- game_statistics[game_statistics$BrianGorman == 1,]

game_statistics$JimJoyce <- with(game_statistics, ifelse(hp_ump_name == 'Jim Joyce', 1, 0))
JimJoyce_games <- game_statistics[game_statistics$JimJoyce == 1,]

game_statistics$DaleScott <- with(game_statistics, ifelse(hp_ump_name == 'Dale Scott', 1, 0))
DaleScott_games <- game_statistics[game_statistics$DaleScott == 1,]

game_statistics$TimWelke <- with(game_statistics, ifelse(hp_ump_name == 'Tim Welke', 1, 0))
TimWelke_games <- game_statistics[game_statistics$TimWelke == 1,]

mean(BrianGorman_games$total_runs)
mean(JimJoyce_games$total_runs)
mean(DaleScott_games$total_runs)
mean(TimWelke_games$total_runs)

projected_runs <- lm(game_statistics$total_runs ~ game_statistics$RedSox_playing+game_statistics$BrianGorman+game_statistics$JimJoyce+game_statistics$DaleScott+game_statistics$TimWelke)
confint(projected_runs, level = 0.95)
