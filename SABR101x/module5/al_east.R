WPct_estimators =read.csv("win_estimators.csv")
#AL_EAST_estimator = WPct_estimators[WPct_estimators$teamID == 'NYA' | 
#                                    WPct_estimators$teamID == 'BOS' |
#                                    WPct_estimators$teamID == 'BAL' |
#                                    WPct_estimators$teamID == 'TOR' |
#                                    WPct_estimators$teamID == 'TBA',]

#NL_WEST_estimator = WPct_estimators[WPct_estimators$teamID == 'ARI' | 
#                                      WPct_estimators$teamID == 'COL' |
#                                      WPct_estimators$teamID == 'LAN' |
#                                      WPct_estimators$teamID == 'SDN' |
#                                      WPct_estimators$teamID == 'SFN',]

AL_EAST <- subset(WPct_estimators, teamID = c('BAL', 'BOS', 'NYA', 'TBA', 'TOR'))
NL_WEST <- subset(WPct_estimators, teamID = c('ARI', 'COL', 'LAN', 'SDN', 'SFN'))
